import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

# create a canvas widget
canvas = tk.Canvas(root, width=900, height=600)
canvas.grid(columnspan=3, rowspan=4)

# Logo
logo = tk.PhotoImage(file="logo.png").subsample(8,8)  # Loading an image form the computer and resizing it 
logo_label = tk.Label(image=logo)                     # placing the logo inside a label widget
logo_label.grid(column=1, row=0)                      # placing the label in the grid


# Instructions
instructions = tk.Label(root, text="Select a PDF file from your computer to extract all its text.", font="Raleway")
instructions.grid(columnspan=3, row=1, column=0)

# button press function

def btn_click():
    btn_text.set("Loading...")
    file_open = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf files","*.pdf")])
    if file_open:
        read_pdf = PyPDF2.PdfReader(file_open)
        page = read_pdf.pages[1]
        page_content = page.extract_text()
        print(page_content)

# Browse button
btn_text = tk.StringVar()                           # creating a var for string
browse_btn = tk.Button(root,  textvariable=btn_text, bg="brown", height=2, width=10, command=btn_click)
btn_text.initialize("Browse")                       # initial text to "Browse"
browse_btn.grid(row=3, column=1)


root.mainloop()
