import time


def insertion_sort(arr, draw, delay):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            draw(arr, ["blue" if x == j+1 else "red" for x in range(n)])
            time.sleep(delay)
            j -= 1

        arr[j+1] = key
        draw(arr, ["blue" if x == j + 1 else "red" for x in range(n)])
        time.sleep(delay)
