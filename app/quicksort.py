import time


def quicksort(arr, draw, delay, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot = partition(arr, low, high, draw, delay)
        quicksort(arr, draw, delay, low, pivot - 1)
        quicksort(arr, draw, delay, pivot + 1, high)


def partition(arr, low, high, draw, delay):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw(arr, ["blue" if x == i or x == j else "red" for x in range(len(arr))])
            time.sleep(delay)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    draw(arr, ["blue" if x == i+1 or x == high else "red" for x in range(len(arr))])
    time.sleep(delay)
    return i + 1
