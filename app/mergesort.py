import time


def mergesort(arr, draw, delay, first=0, last=None):
    if last is None:
        last = len(arr) - 1
    if first < last:
        mid = (first + last) // 2
        mergesort(arr, draw, delay, first, mid)
        mergesort(arr, draw, delay, mid+1, last)
        merge(arr, first, mid, last, draw, delay)


def merge(arr, first, mid, last, draw, delay):
    n1 = mid - first + 1
    n2 = last - mid
    left = [arr[first + i] for i in range(n1)]
    right = [arr[mid + j + 1] for j in range(n2)]

    i = j = 0
    k = first
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            paint(arr, k, first+i, draw, delay)
            i += 1
        else:
            arr[k] = right[j]
            paint(arr, k, mid + j + 1, draw, delay)
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        paint(arr, k, first + i, draw, delay)
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        paint(arr, k, mid + j + 1, draw, delay)
        j += 1
        k += 1


def paint(arr, i, j, draw, delay):
    draw(arr, ["blue" if x == i or x == j else "red" for x in range(len(arr))])
    time.sleep(delay)
