from tkinter import *
root=Tk()
def leftclick(event):
    print("left is clicked")

frame=Frame(root, width=200,height=200)
frame.bind("<Button-1>",leftclick)
frame.pack()

root.mainloop()
