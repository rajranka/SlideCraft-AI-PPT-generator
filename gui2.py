from tkinter import *
from tkinter import PhotoImage
from tkinter import font
from PIL import Image, ImageTk

def new_window(callback, window, num, option):
    if option==1:
        def generate_2():
            result = [e.get() for e in e_n]
            n_window.destroy()
            callback(result)

        n_window = Toplevel(window)
        n_window.title("Enter Titles")
        n_window.configure(bg="cyan")
        
        title_font_2 = font.Font(family="Times New Roman", size=38, weight="bold")
        e_n = []

        frame_slide_title = Frame(n_window)
        frame_slide_title.grid(row=0, column=0, columnspan=2)
        frame_slide_title.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
        label_slide_title = Label(frame_slide_title, text="Enter the Titles of slides- ", font=title_font_2, bg="cyan", highlightthickness=0, highlightbackground="cyan", fg="Black")
        label_slide_title.pack()

        frame_slides = Frame(n_window)
        frame_slides.grid(row=1, column=0)
        frame_slides.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
        for i in range(0, num):
            label_slides = Label(frame_slides, text="Enter Slide Title "+str(i+1)+"- ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan", fg="Black")
            label_slides.grid(row=i, column=0)
            e = Entry(frame_slides, width=25, bg="cyan", highlightthickness=0, highlightbackground="cyan")
            e.grid(row=i, column=1)
            e_n.append(e)

        frame_slide_button = Frame(n_window)
        frame_slide_button.grid(row=2, column=0, columnspan=2)
        frame_slide_button.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
        n_button = Button(frame_slide_button, text="GENERATE", bg="black", fg="white", command=generate_2)
        n_button.pack()

        n_window.mainloop()
    else:
        callback(0)