"""
Bubble sort
"""


def bubble_sort(array):

    n = len(array)

    for count in range(n - 1):
        swaps = False
        for i in range(n - 1 - count):
            print(count, i)
            if array[i] > array[i + 1]:
                swaps = True
                array[i], array[i + 1] = array[i + 1], array[i]
        if not swaps:
            break

    return array


if __name__ == '__main__':
    arr = [3, 5, 8, 4, 1, 9, -2]
    arr = [-2, 1, 3, 4, 5, 8, 9]
    print(arr)
    print(bubble_sort(arr))
