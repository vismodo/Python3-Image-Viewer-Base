# Importing
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.messagebox import showinfo
def next_func():
    welcome.destroy()
    root = Tk()
    root.title('Py Image Viewer')
# Functions
    def openfn():
            filename = filedialog.askopenfilename(title='Load Image')
            return filename
    def open_img():
        x = openfn()
        try:
            img = Image.open(x)
            width, height = img.size    
            img = img.resize((width, height), Image.ANTIALIAS)
            root.geometry(str(width)+"x"+str(height))
            img = ImageTk.PhotoImage(img)
            panel = Label(root, image=img)
            panel.image = img
            panel.pack()
        except:
            showinfo("Error", "The file you tried to open was not a supported image file.")
            root.destroy()
    open_img()
    root.mainloop()# mainloop

welcome = Tk()
welcome.title('Py Image Viewer')
img2 = ImageTk.PhotoImage(Image.open("Welcome_Screen.png"))
panel2 = Label(welcome, image = img2)
panel2.pack(side = "top", fill = "both", expand = "yes")
intro = Label(welcome, text="This program will help you to load an image", font=("Helevectica",20,'bold')).pack()
next_but = Button(welcome, text="Next", bd=4, padx=14, pady=14, bg='orange', command=next_func, font=("Courier New",16,'bold')).pack()
welcome.mainloop()
