
# 🌻 Sunflowers for Valbb

*A little sunflower, drawn one pixel at a time.*

This project is a small experiment made with Python, Turtle Graphics, and a little bit of love.

It takes a collection of coordinates and color values stored in a JSON file and progressively reconstructs a sunflower illustration on the screen.

Every point contributes to bringing the flower to life. ♡

---

## ✨ About the project

The program reads geometric regions from a JSON file, extracts their contours, and converts their coordinates into positions on a Turtle canvas.

Each point is represented as a small colored dot, allowing the original illustration to be reconstructed progressively.

### Features

- 🌻 Image reconstruction using JSON coordinate data.
- 🎨 RGB color conversion and rendering.
- 📍 Automatic coordinate scaling and centering.
- 🖥️ Progressive drawing using Python Turtle.
- ⚡ Batched screen updates for improved rendering performance.
- 💛 A little sunflower made especially for Val.

---

## 🛠️ Built with

- **Python 3**
- **Turtle Graphics** — Drawing and rendering.
- **JSON** — Storing coordinates, contours, and color information.

---

## 📂 Project structure

```text
sunflowers-for-val/
│
├── main.py
├── sunflowers.json
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Main script responsible for reconstructing the illustration. |
| `sunflowers.json` | Contains the coordinates, contours, and RGB color data. |
| `README.md` | Project documentation. |

---

## 🚀 Getting started

### Requirements

- Python 3.x
- Tkinter support for Python Turtle.

### Installation

Clone the repository:

```bash
git clone https://github.com/laetg404/sunflowers-for-val.git
```

Navigate to the project directory:

```bash
cd sunflowers-for-val
```

Run the script:

```bash
python main.py
```

Make sure `sunflowers.json` is located in the same directory as `main.py`.

---

## ⚙️ How it works

1. Loads the illustration data from `sunflowers.json`.
2. Extracts all contour coordinates.
3. Calculates the image boundaries.
4. Determines the appropriate scale to fit the canvas.
5. Converts the stored RGB values into hexadecimal colors.
6. Draws each point using Turtle Graphics.
7. Updates the canvas progressively until the illustration is complete.

---

## ♡ A little dedication

Some things are worth creating one little piece at a time.

This sunflower is one of them.

A small digital flower, made with code, patience, and lots of love.

**For Val, my princess, always. ♡**

---

<sub>Part of a collection of little projects created with love.</sub>

🌻
