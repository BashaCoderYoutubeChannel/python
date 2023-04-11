from tkinter import*
root = Tk()
root.title("Menu bar")
#Menu bar code
menu_var = Menu(root)
root.config(menu=menu_var)
def custom():
    pass

file= Menu(menu_var)

file_ = Menu(file)
menu_var.add_cascade(label="File", command=custom, menu=file)
menu_var.add_cascade(label = "Edit", command=custom)
file.add_command(label="New",  command=custom)
file.add_cascade(label="tools", menu=file_)
file.add_separator()
file.add_command(label="Quit", command=root.quit)

file_.add_command(label="New",  command=custom)
file_.add_separator()
file_.add_command(label="Quit", command=root.quit)
root.mainloop()