from tkinter import *

## variables ##
window = None
canvas = None
x1 = None
y1 = None
x2 = None
y2 = None

## functions ##
def mouseClick(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width=5, fill="red")

## main code ##
window = Tk()
window.title("Tutorial")
canvas = Canvas(window, height=800, width=800)
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()
window.mainloop()
