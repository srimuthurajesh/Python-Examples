from tkinter import *

def does():
    pass

root=Tk()
menu= Menu(root)
root.config(menu=menu)

#menu bar
filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New" ,command=does)
filemenu.add_separator()
filemenu.add_command(label="Open",command=does)
editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="tools",command=does)

#tool bar
toolbar=Frame(root, bg="blue")
insertbutton= Button(toolbar, text="insert", command=does)
insertbutton.pack(side=LEFT, padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

#status bar
status=Label(root, text="status bar", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
