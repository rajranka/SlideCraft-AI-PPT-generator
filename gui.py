from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from gui2 import new_window

def gui(answer):
    def generate(result):
        none = [' ']
        response = []
        topic = e.get()
        if check.get()==0:
            image = 2
        elif check.get()==1:
            image = 1
        number_slide = number.get()
        if template_option.get()==1:
            template_selected = 1
        elif template_option.get()==2:
            template_selected = 2
        elif template_option.get()==3:
            template_selected = 3
        elif template_option.get()==4:
            template_selected = 4
        if option.get()==1:
            choice = 1
            window.destroy()
            response.append(topic)
            response.append(image)
            response.append(number_slide)
            response.append(template_selected)
            response.append(choice)
            response.extend(result)
            answer(response)
        elif option.get()==2:
            choice = 2
            window.destroy()
            response.append(topic)
            response.append(image)
            response.append(number_slide)
            response.append(template_selected)
            response.append(choice)
            response.extend(none)
            answer(response)

    def checkbox():
        if check.get()==0:
            check_button.config(text="No")
        elif check.get()==1:
            check_button.config(text="Yes")
        
    def scroll_frame(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.yview_moveto(0)

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # def create_gradient_background(canvas):
    #     width = canvas.winfo_width()
    #     height = canvas.winfo_height()
    #     for i in range(width):
    #         r = int(0 + i / width * 255)
    #         g = int(128 + i / width * 127)
    #         b = int(128 + i / width * 127)
    #         color = f'#{r:02X}{g:02X}{b:02X}'
    #         canvas.create_line(i, 0, i, height, fill=color)

    window = Tk()
    window.title("SlideCraft")
    window.configure(bg="cyan")

    #Background
    # gradient_canvas = Canvas(window, bg="white", highlightthickness=0)
    # gradient_canvas.grid(row=0, column=0, columnspan=3, rowspan=11, sticky="nsew")
    # gradient_canvas.bind("<Configure>", lambda event: create_gradient_background(gradient_canvas))

    #Frame - Logo Frame
    frame_logo = Frame(window)
    frame_logo.grid(row=0, column=0)
    frame_logo.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    logo = Image.open("GUI\Project_Logo.png")
    logo = logo.resize((125, 75))
    photo = ImageTk.PhotoImage(logo)
    logo_label = Label(frame_logo, image=photo, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    logo_label.pack()

    #Frame - Title Frame
    title_font = font.Font(family="Times New Roman", size=46, weight="bold")
    frame_title = Frame(window)
    frame_title.grid(row=0, column=1)
    frame_title.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty1 = Label(frame_title, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty1.pack(side="left", padx=100)
    label_title = Label(frame_title, text="SlideCraft", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan", fg="Black")
    label_title.pack(side="right", padx=200)

    #Frame - Empty Frame
    frame_empty8 = Frame(window)
    frame_empty8.grid(row=0, column=2)
    frame_empty8.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty9 = Label(frame_empty8, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty9.pack(side="right", padx=100)

    #Frame - Empty Frame
    frame_empty = Frame(window)
    frame_empty.grid(row=1, column=0)
    frame_empty.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty2 = Label(frame_empty, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty2.pack()

    #Frame - Sub Title Frame
    frame_subtitle = Frame(window)
    frame_subtitle.grid(row=1, column=1)
    frame_subtitle.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty3 = Label(frame_subtitle, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty3.pack(side="left", padx=100)
    label_subtitle = Label(frame_subtitle, text="Automatic PPT Generator", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_subtitle.pack(side="right", padx=200)

    #Frame - Empty Frame
    frame_empty2 = Frame(window, height=5, width=15)
    frame_empty2.grid(row=2, column=0)
    frame_empty2.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty4 = Label(frame_empty2, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty4.pack()

    #Frame - Dot Frame
    frame_dot = Frame(window)
    frame_dot.grid(row=3, column=0)
    frame_dot.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot1 = Label(frame_dot, text="●", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot1.pack(side="left")

    #Frame - Topic Frame
    frame_topic = Frame(window)
    frame_topic.grid(row=3, column=1)
    frame_topic.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_topic = Label(frame_topic, text="Enter the Topic of the Presentation- ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_topic.pack(side="left", padx=20)
    e = Entry(frame_topic, width=25, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    e.pack(side="right")

    #Frame - Empty Frame
    frame_empty3 = Frame(window, height=5, width=15)
    frame_empty3.grid(row=4, column=0)
    frame_empty3.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty5 = Label(frame_empty3, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty5.pack()

    #Frame - Dot Frame
    frame_dot2 = Frame(window)
    frame_dot2.grid(row=5, column=0)
    frame_dot2.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot2 = Label(frame_dot2, text="●", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot2.pack(side="left")

    #Frame - Image Frame
    frame_image = Frame(window)
    frame_image.grid(row=5, column=1)
    frame_image.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    check = IntVar()
    label_image = Label(frame_image, text="Do you want images in the Presentation- ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_image.pack(side="left", padx=20)
    check_button = Checkbutton(frame_image, text="No", variable=check, width=25, bg="cyan", highlightthickness=0, highlightbackground="cyan", command=checkbox)
    check_button.pack(side="right")

    #Frame - Empty Frame
    frame_dot7 = Frame(window)
    frame_dot7.grid(row=6, column=0)
    frame_dot7.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot7 = Label(frame_dot7, text=" ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot7.pack(side="right")

    #Frame - Dot Frame
    frame_dot5 = Frame(window)
    frame_dot5.grid(row=7, column=0)
    frame_dot5.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot5 = Label(frame_dot5, text="●", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot5.pack(side="right")

    #Frame - Slide Number Frame
    number = IntVar()
    frame_number = Frame(window)
    frame_number.grid(row=7, column=1)
    frame_number.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_number = Label(frame_number, text="Enter the Number of Slides of the Presentation- ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_number.pack(side="left", padx=20)
    Radiobutton(frame_number, text="3", variable=number, value=3, bg="cyan", highlightthickness=0, highlightbackground="cyan").pack(side="left")
    Radiobutton(frame_number, text="6", variable=number, value=6, bg="cyan", highlightthickness=0, highlightbackground="cyan").pack(side="left")
    Radiobutton(frame_number, text="9", variable=number, value=9, bg="cyan", highlightthickness=0, highlightbackground="cyan").pack(side="left")

    #Frame - Dot Frame
    frame_dot5 = Frame(window)
    frame_dot5.grid(row=8, column=0)
    frame_dot5.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot5 = Label(frame_dot5, text="●", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot5.pack(side="right")

    #Frame - Template Frame
    frame_temp = Frame(window)
    frame_temp.grid(row=8, column=1)
    frame_temp.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_temp = Label(frame_temp, text="Select the template you like- ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_temp.pack(side="left")

    #Frame - Scrolling Frame
    frame_scroll = Frame(window)
    frame_scroll.grid(row=8, column=2)
    frame_scroll.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")

    canvas = Canvas(frame_scroll)
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar = Scrollbar(frame_scroll, orient="horizontal", command=canvas.xview, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    scrollbar.grid(row=1, column=0, sticky="ew", rowspan=1)
    canvas.configure(xscrollcommand=scrollbar.set, bg="cyan", highlightthickness=0, highlightbackground="cyan")

    frame_inside = Frame(canvas)
    frame_inside.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    canvas.create_window((0, 0), window=frame_inside, anchor="nw")

    photo_list = []
    template_option = IntVar()
    for i in range(1, 6):
        template = Image.open("Template_"+str(i)+".png")
        template = template.resize((150, 200))
        photo2 = ImageTk.PhotoImage(template)
        photo_list.append(photo2)   
        template_label = Label(frame_inside, image=photo_list[i-1], bg="cyan", highlightthickness=0, highlightbackground="cyan")
        template_label.grid(row=0, column=i-1)
        Radiobutton(frame_inside, text="Template "+str(i)+" ", variable=template_option, value=i, bg="cyan", highlightthickness=0, highlightbackground="cyan").grid(row=1, column=i-1)
    frame_inside.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", scroll_frame)
    label_empty10 = Label(frame_scroll, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_empty10.grid(row=0, column=1, padx=50)

    #Frame - Dot Frame
    frame_dot3 = Frame(window)
    frame_dot3.grid(row=9, column=0)
    frame_dot3.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot3 = Label(frame_dot3, text="●", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot3.pack(side="left")

    #Frame - Auto Generate Frame
    option = IntVar()
    frame_auto = Frame(window)
    frame_auto.grid(row=9, column=1)
    frame_auto.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_auto = Label(frame_auto, text="Do you wish to- ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_auto.pack(side="left", padx=20)
    Radiobutton(frame_auto, text="Provide the Slide Topics ", variable=option, value=1, bg="cyan", highlightthickness=0, highlightbackground="cyan").pack(side="left")
    Radiobutton(frame_auto, text="Auto-Generate the Slide Topics ", variable=option, value=2, bg="cyan", highlightthickness=0, highlightbackground="cyan").pack(side="left")

    #Frame - Empty Frame
    frame_dot4 = Frame(window)
    frame_dot4.grid(row=10, column=0)
    frame_dot4.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot4 = Label(frame_dot4, text="  ", font="helvetica", bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_dot4.pack(side="left")

    #Frame - Generate Button Frame
    frame_button = Frame(window)
    frame_button.grid(row=10, column=1)
    frame_button.configure(bg="cyan", highlightthickness=0, highlightbackground="cyan")
    button = Button(frame_button, text="GENERATE", bg="black", fg="white", command=lambda: new_window(generate, window, number.get(), option.get()))
    button.pack(side="left")
    label_submit = Label(frame_button, text=" ", font=title_font, bg="cyan", highlightthickness=0, highlightbackground="cyan")
    label_submit.pack(side="right")

    window.mainloop()