import sys
import turtle
import json


def draw_from_json(json_file):
    # Cargar los datos
    with open(json_file, "r", encoding="utf-8") as f:
        regions = json.load(f)

    if not regions:
        raise ValueError("El JSON no contiene regiones.")

    # Obtener todos los puntos para calcular las dimensiones
    all_points = [
        point
        for region in regions
        for point in region.get("contour", [])
        if len(point) >= 2
    ]

    if not all_points:
        raise ValueError("No se encontraron puntos para dibujar.")

    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Escala para ajustar el dibujo a la ventana
    scale = min(700 / width, 700 / height)

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    # Configurar Turtle
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("black")
    screen.title("Dibujando Sunflowers...")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    # Tamaño de cada punto en pantalla
    dot_size = max(2, round(scale * 1.15))

    # Ajustar el tamaño del dibujo a las coordenadas
    total_points = sum(
        len(region.get("contour", []))
        for region in regions
    )

    drawn = 0
    batch_size = 10000

    # Dibujar progresivamente cada región
    for region in regions:
        color_data = region.get("color", [0, 0, 0])

        # Convertir colores normalizados (0-1) a RGB (0-255)
        rgb = []
        for component in color_data[:3]:
            component = float(component)

            if 0 <= component <= 1:
                component = round(component * 255)
            else:
                component = round(component)

            rgb.append(max(0, min(255, component)))

        color = "#{:02x}{:02x}{:02x}".format(*rgb)

        # Dibujar los píxeles de esta región
        for point in region.get("contour", []):
            if len(point) < 2:
                continue

            x = (point[0] - center_x) * scale
            y = (center_y - point[1]) * scale

            t.goto(x, y)
            t.dot(dot_size, color)

            drawn += 1

            # Actualizar la pantalla por grupos
            if drawn % batch_size == 0:
                screen.title(
                    f"Dibujando Sunflowers... "
                    f"{drawn:,}/{total_points:,} puntos"
                )
                screen.update()

        # Mostrar también el avance al terminar cada región
        screen.update()

    screen.title("Sunflowers - Dibujo terminado")
    screen.update()

    print(f"Dibujo terminado: {drawn:,} puntos procesados.")

    screen.mainloop()


if __name__ == '__main__':
    draw_from_json("sunflowers.json")