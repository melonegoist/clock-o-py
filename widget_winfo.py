from tkinter import * 

def winfo_w(widget):
    widget.pack()
    widget.update()
    print(f'{widget.winfo_name()} (width) = {widget.winfo_width()}')
    widget.pack_forget()

def winfo_h(widget):
    widget.pack()
    widget.update()
    print(f'{widget.winfo_name()} (height) = {widget.winfo_height()}')
    widget.pack_forget()

def winfo_all(widget):
    winfo_h(widget)
    winfo_w(widget)

def widget_w(widget):
    widget.pack()
    widget.update()
    width = widget.winfo_width()
    widget.pack_forget()
    return width

def widget_h(widget):
    widget.pack()
    widget.update()
    height = widget.winfo_height()
    widget.pack_forget()
    return height
   