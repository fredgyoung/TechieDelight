"""
Bubble sort
"""


def bubble_sort(array):

    n = len(array)

    for _ in range(n - 1):
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


if __name__ == '__main__':
    arr = [3, 5, 8, 4, 1, 9, -2]
    print(arr)
    print(bubble_sort(arr))
