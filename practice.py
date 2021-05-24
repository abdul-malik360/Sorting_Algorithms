from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("second")
window.config(bg="light blue")
window.geometry("500x500")

Label(window, text="Welcome to Sorting Numbers").place(x=150, y=50)

Label(window, text="Sorted list: ").place(x=20, y= 130)
sorted_list = Entry(window, text=" ", width=25, textvariable=list, show=" ")
sorted_list.place(x=120, y=130)

Label(window, text="Enter your List: ").place(x=20, y=90)

list_ent = Entry(window, text=" ", width=25)
list_ent.place(x=120, y=90)









sh_list = Button(window, text="Show list", borderwidth="5")
sh_list.place(x=260, y=170)



window.mainloop()
