import time


def heapsort(arr, draw, delay):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        draw(arr, ["blue" if x == 0 or x == i else "red" for x in range(n)])
        time.sleep(delay)
        heapify(arr, i, 0)


def heapify(arr, n, i):
    max_val = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[max_val] < arr[l]:
        max_val = l
    if r < n and arr[max_val] < arr[r]:
        max_val = r
    if max_val != i:
        arr[i], arr[max_val] = arr[max_val], arr[i]
        heapify(arr, n, max_val)
