import tkinter as tk
from tkinter import ttk

def update_animation(canvas, angle):
    canvas.delete("all")
    canvas.create_text(150, 150, text="Loading...", font=("Helvetica", 16))
    canvas.create_arc(50, 50, 250, 250, start=angle, extent=60, style=tk.ARC, width=10, outline="black")
    angle += 10
    if angle >= 360:
        angle = 0
    return angle

def loading():
    global root 
    root = tk.Tk()
    root.title("Loading Screen")
    root.geometry("700x700")
    root.configure(bg="teal")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack(pady=50)
    canvas.configure(bg="teal", highlightthickness=0, highlightbackground="teal")

    angle = 0

    def animate():
        nonlocal angle
        angle = update_animation(canvas, angle)
        root.after(50, animate)
        return 0

    a = animate()

    root.mainloop()
    return a

def loading_kill():
    root.destroy()