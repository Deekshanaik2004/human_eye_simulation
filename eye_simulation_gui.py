import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw realistic eye diagram with vision status
def draw_eye_model(focal_length):
    fig, ax = plt.subplots()
    ax.set_xlim(-80, 130)
    ax.set_ylim(-40, 40)
    ax.set_aspect('equal')
    ax.set_title("Human Eye Diagram with Lens, Retina and Ray Focus")

    # Eye shape
    eye = patches.Ellipse((60, 0), width=120, height=70, edgecolor='black',
                          facecolor='lightblue', lw=2)
    ax.add_patch(eye)

    # Lens
    lens_x = 30
    lens = patches.Ellipse((lens_x, 0), width=8, height=30, edgecolor='blue',
                           facecolor='skyblue', lw=2, label='Lens')
    ax.add_patch(lens)

    # Retina
    retina_x = 120
    ax.axvline(x=retina_x, color='red', lw=3, label='Retina')
    ax.text(retina_x + 2, 15, "Retina", color='red')

    # Object
    object_x = -50
    ax.plot(object_x, 0, 'go', label='Object')
    ax.text(object_x - 15, 5, "Object", color='green')

    # Ray from object to lens
    ax.annotate("", xy=(lens_x, 0), xytext=(object_x, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

    # Calculate image position
    try:
        u = object_x - lens_x
        f = focal_length
        v = 1 / (1 / f + 1 / abs(u))
        image_x = lens_x + v
    except:
        image_x = lens_x + 20

    # Ray from lens to image
    ax.annotate("", xy=(image_x, 0), xytext=(lens_x, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='orange'))

    # Image point
    ax.plot(image_x, 0, 'ro', label='Image Point')
    ax.text(image_x + 2, -12, f"Image ({image_x:.1f} mm)", color='red')

    # Lens label
    ax.text(lens_x + 5, 12, "Lens", color='blue')
    ax.legend()
    ax.grid(True)
    plt.xlabel("Horizontal Axis (mm)")
    plt.ylabel("Vertical Axis (mm)")

    # Show condition: Myopia / Hyperopia / Normal
    error = image_x - retina_x
    if abs(error) <= 5:
        condition = "Normal Vision"
        color = "green"
    elif image_x < retina_x:
        condition = "Myopia (Nearsighted)"
        color = "purple"
    else:
        condition = "Hyperopia (Farsighted)"
        color = "brown"

    ax.text(10, -30, f"Condition: {condition}", fontsize=12, color=color)

    plt.show()

# GUI
root = tk.Tk()
root.title("Human Eye Vision Simulator")
root.geometry("400x250")

ttk.Label(root, text="Adjust Focal Length (in mm):").pack(pady=10)

f_slider = ttk.Scale(root, from_=10, to=100, orient='horizontal')
f_slider.set(20)
f_slider.pack(pady=5)

# Live focal length display
focal_label = ttk.Label(root, text=f"Focal Length: {f_slider.get():.1f} mm")
focal_label.pack(pady=5)

def update_label(value):
    focal_label.config(text=f"Focal Length: {float(value):.1f} mm")

f_slider.config(command=update_label)

# Button action
def simulate():
    focal_length = float(f_slider.get())
    draw_eye_model(focal_length)

ttk.Button(root, text="Simulate", command=simulate).pack(pady=10)

root.mainloop()