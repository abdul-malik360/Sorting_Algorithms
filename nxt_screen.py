from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to Sorting Numbers")
window.config(bg="light blue")
window.geometry("500x500")

Label(window, text="numbers = [42, 12, 13, 89, 63, 11]", bg="light blue").place(x=150, y=50)

Label(window, text="Sorted list: ", bg="light blue").place(x=50, y=100)
sorted_list = Label(window, text=" ", width=25)
sorted_list.place(x=150, y=100)


numbers = [42, 12, 13, 89, 63, 11]


def selection_sort(numbers):
    n = len(numbers)
    for smallest in range(n-1):
        sn = smallest
        for i in range(smallest+1, n):
            if numbers[i] < numbers[sn]:
                sn = i
        numbers[smallest], numbers[sn] = numbers[sn], numbers[smallest]
    return numbers


sorted_list.config(text=selection_sort(numbers), bg="sky blue")

window.mainloop()
