from tkinter import *

window = Tk()
window.title("Welcome to Sorting Numbers")
window.config(bg="light blue")
window.geometry("500x500")

list_var = StringVar()

Label(window, text="numbers = [42, 12, 13, 89, 63, 11]", bg="light blue").place(x=150, y=50)

Label(window, text="Sorted list: ", bg="light blue").place(x=50, y=100)
sorted_list = Label(window, text=" ", width=25, textvariable=list_var)
sorted_list.place(x=150, y=100)


def selection_sort():
    numbers = [42, 12, 13, 89, 63, 11]
    n = len(numbers)
    for smallest in range(n-1):
        sn = smallest
        for i in range(smallest+1, n):
            if numbers[i] < numbers[sn]:
                sn = i
        numbers[smallest], numbers[sn] = numbers[sn], numbers[smallest]
    list_var.set(numbers)


def clear():
    list_var.set(" ")


def close_window():
    window.destroy()


sort = Button(window, text="Sort List", borderwidth="5", command=selection_sort, bg="sky blue")
sort.place(x=190, y=150)

clear_btn = Button(window, text="Clear", borderwidth="5", command=clear, bg="sky blue")
clear_btn.place(x=290, y=150)

close = Button(window, text="close", borderwidth="5", command=close_window, bg="sky blue")
close.place(x=290, y=200)


window.mainloop()
