from tkinter import messagebox
from tkinter import*
root = Tk()
root.title("Test")
def box():
    #info
    messagebox.showinfo("Test - info", "This is an info box made by python.")
    #warning
    messagebox.showwarning("Test - warning", "This is a warning box made by python")
    #error
    messagebox.showerror("Test - error", "This is a warning")
    #yes or no
    m = messagebox.askyesno("ask yes or no", "message")
    if m:
       print(True)
    else:
        print(False)
        root.quit()
    #yes or no or cancel
    messagebox.askyesnocancel("ask yes or no or cancel", "message")    

    
  
Button(root, text="Click me!", command=box).pack()
root.mainloop()
