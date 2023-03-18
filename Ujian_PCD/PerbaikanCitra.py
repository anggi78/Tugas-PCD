#Nama  : Aisyah Rahmadani Pohontu
#Nim   : F55121054
#Kelas : B

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageOps
from tkinter import filedialog

root = tk.Tk()
root.title("GUI Aplikasi Penerapan Perbaikan Citra")

original_image = None
enhanced_image = None

def open_image():
    global original_image, enhanced_image
    
    file_path = filedialog.askopenfilename()
    
    original_image = Image.open(file_path)
    original_image = original_image.convert("RGB")
    image = ImageTk.PhotoImage(original_image)
    panel1.config(image=image)
    panel1.image = image
    
    panel2.config(image=None)
    panel2.image = None
    
    enhanced_image = None

def method1():
    global original_image, enhanced_image
    
    if original_image is not None:
        enhanced_image = original_image.filter(ImageFilter.BLUR)
        
        image = ImageTk.PhotoImage(enhanced_image)
        panel2.config(image=image)
        panel2.image = image

def method2():
    global original_image, enhanced_image
    
    if original_image is not None:
        enhanced_image = ImageOps.equalize(original_image)
       
        image = ImageTk.PhotoImage(enhanced_image)
        panel2.config(image=image)
        panel2.image = image

panel1 = tk.Label(root)
panel1.pack(side="left", padx=5, pady=5)

panel2 = tk.Label(root)
panel2.pack(side="right", padx=5, pady=5)

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(side="top", padx=5, pady=5)

method1_button = tk.Button(root, text="Method 1", command=method1)
method1_button.pack(side="left", padx=3, pady=3)

method2_button = tk.Button(root, text="Method 2", command=method2)
method2_button.pack(side="right", padx=3, pady=3)

root.mainloop()