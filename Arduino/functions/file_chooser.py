from tkinter import filedialog
from tkinter import Tk

def choose_image():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )

    return file_path
