import time


def bubble_sort(arr, draw, delay):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw(arr, ["blue" if x == j or x == j+1 else "red" for x in range(n)])
                time.sleep(delay)
                swapped = True
        if not swapped:
            break
