# Import necessary packages

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window

window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1) 

# Function to Open a file

def open_file():
    """Open file for editing"""
    filepath = askopenfilename(filetypes = [("Text Files" , "*.txt" ) , ("All Files" , "*.*")])
    if not filepath:
        return
    
    text_edit.delete(1.0 , END)
    with open(filepath , "r") as input_file:
        text = input_file.read()
        text_edit.insert(END , text)
        input_file.close()
    window.title("Codingal's Text Editor - {filepath}")
    
def save_file():
    filepath = asksaveasfilename(defaultextionsion = "txt" , filetypes = [("Text Files" , "*.txt" ) , ("All Files" , "*.*")])
    if not filepath:
        return
    with open(filepath , "w") as output_file:
        text = txt_edit.get(1.0 , END)
        output_file.write(text)
    window.title("Codingal's Text Editor - {filepath}")

#add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window,relief = RAISED , bd = 2)
btn_open = Button(fr_buttons , text = "Open" , command = open_file)
btn_save = Button(fr_buttons , text = "Save" , command = save_file)
btn_open.grid(row = 0 , column = 0 , padx = 5)
btn_open.grid(row = 1 , column = 0 , padx = 5)
fr_buttons.grid(row = 0 , columns = 0)
txt_edit.grid(row = 0 , columns = 1)

window.mainloop()


    