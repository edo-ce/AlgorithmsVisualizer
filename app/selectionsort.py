import time


def selection_sort(arr, draw, delay):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
        draw(arr, ["blue" if x == min_index or x == i else "red" for x in range(n)])
        time.sleep(delay)
