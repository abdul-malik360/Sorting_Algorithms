from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("second")
window.config(bg="light blue")
window.geometry("500x500")

Label(window, text="Welcome to Sorting Numbers").place(x=150, y=50)

Label(window, text="Sorted list: ").place(x=20, y= 130)
sorted_list = Label(window, text=" ", width=25)
sorted_list.place(x=120, y=130)

Label(window, text="numbers = [42, 12, 13, 89, 63, 11]").place(x=20, y=90)



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
sorted_list.config(text=numbers)



sh_list = Button(window, text="Show list", borderwidth="5", command=selection_sort)
sh_list.place(x=260, y=170)



window.mainloop()
