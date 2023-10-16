from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont, ImageTk

file_name = ""


def load_image(file_name):
    image = Image.open(file_name)
    image.thumbnail((400, 400))
    photo_img = ImageTk.PhotoImage(image)


def open_explorer():
    global file_name
    file_name = askopenfilename()
    load_image(file_name=file_name)


main_window = Tk()
main_window.title("Add watermark to file")
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# replace either screen_width and screen_height to change the appropriate dimension
main_window.geometry(f"{screen_width}x{screen_height}")

upload_button = Button(
    main_window,
    text="Select image",
    relief="raised",
    borderwidth=5,
    command=lambda: open_explorer(),
)
upload_button.place(relx=0.5, rely=0.5, anchor=CENTER)


main_window.mainloop()
