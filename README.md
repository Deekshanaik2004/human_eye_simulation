#  Human Eye Vision Simulator

This project simulates **image formation in the human eye** using a GUI-based Python application. You can interactively adjust the **focal length** of the eye's lens and visually see how light rays bend and form images — just like in real eyes!

---

##  Features
-  Adjustable **focal length slider**
-  Real-time simulation of:
  - Lens
  - Retina
  - Light rays
  - Image formation
-  Detects and displays:
  - **Myopia** (Nearsightedness)
  - **Hyperopia** (Farsightedness)
  - **Normal Vision**

---

##  Physics Behind It

This project models the human eye using the **lens formula**:

\[
\frac{1}{f} = \frac{1}{v} - \frac{1}{u}
\]

- **f** = focal length of the lens  
- **u** = object distance  
- **v** = image distance (should fall on retina)

The **lens adjusts shape** to change focal length so the image always forms on the retina. If the image forms before or after the retina, the simulation labels it as **Myopia** or **Hyperopia** respectively.

---

##  How to Run

###  Requirements:
- Python 3.x
- matplotlib
- tkinter (comes pre-installed with Python)

###  Install dependencies:

```bash
pip install matplotlib
