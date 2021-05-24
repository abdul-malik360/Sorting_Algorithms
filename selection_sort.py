# naming your unsorted list numbers
numbers = [42, 12, 13, 89, 63, 11]


# defining the function of sorting numbers and putting the variable numbers in
def selection_sort(numbers):

    # giving the length of numbers the variable name n
    n = len(numbers)

    # to look for the position of the smallest number in the range of the list
    # for every element in the range
    for smallest in range(n-1):

        # giving the smallest number a variable sn, initially the lowest number
        sn = smallest

        # to look at each element's position in the list (to the right)
        for i in range(smallest+1, n):

            # this is the smaller number
            if numbers[i] < numbers[sn]:

                # replacing the smallest number
                sn = i

        # smallest number will move to the left and bigger number will move to the right
        numbers[smallest], numbers[sn] = numbers[sn], numbers[smallest]

    # completes the function
    return numbers

# displays your sorted list in ascending order
print(selection_sort(numbers))
