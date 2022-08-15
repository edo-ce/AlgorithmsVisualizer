from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from selectionsort import selection_sort
from insertionsort import insertion_sort
from mergesort import mergesort
from heapsort import heapsort
from quicksort import quicksort

root = Tk()
root.title("Algorithms Visualizer")
root.geometry("730x580")
root.config(bg="#576F72")
root.resizable(False, False)

algo = StringVar()
arr = []

sorting_algos = {"Bubble Sort": bubble_sort,
                 "Selection Sort": selection_sort,
                 "Insertion Sort": insertion_sort,
                 "Merge Sort": mergesort,
                 "Heap Sort": heapsort,
                 "Quick Sort": quicksort}


def generate_array():
    global arr
    low = int(lowestEntry.get())
    high = int(highestEntry.get())
    size = int(arrSize.get())
    arr = []
    for i in range(size):
        val = random.randrange(low, high+1)
        arr.append(val)

    draw(arr, ["red" for x in range(len(arr))])


def draw(arr, colors):
    canvas.delete("all")
    height = 380
    width = 600
    bar_width = width / (len(arr) + 1)
    offset = 30
    spacing = 10
    normalized_array = [i / max(arr) for i in arr]
    for i, h in enumerate(normalized_array):
        x0 = i * bar_width + offset + spacing
        y0 = height - h * 340
        x1 = (i + 1) * bar_width + offset
        y1 = height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(arr[i]))
    root.update_idletasks()


def sorting():
    global arr
    f = sorting_algos[menu.get()]
    f(arr, draw, speed.get())
    draw(arr, ["blue" for _ in range(len(arr))])


frame = Frame(root, width=700, height=300, bg="#E4DCCF")
frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=400, bg="#7D9D9C")
canvas.grid(row=1, column=0, padx=10, pady=5)

menu = ttk.Combobox(frame, textvariable=algo, values=[x for x in sorting_algos.keys()], width=10)
menu.grid(row=0, column=0, padx=5, pady=5)
menu.current(0)

Button(frame, text="New Array", command=generate_array, bg='#F0EBE3', height=2).grid(row=0, column=1, padx=10, pady=10)

Button(frame, text="Sort Array", command=sorting, bg='#F0EBE3', height=2).grid(row=0, column=2, padx=5, pady=5)

lowestEntry = Scale(frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Min Value")
lowestEntry.grid(row=1, column=0, padx=5, pady=5)

highestEntry = Scale(frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
highestEntry.grid(row=1, column=1, padx=5, pady=5)

arrSize = Scale(frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Array Size")
arrSize.grid(row=1, column=2, padx=5, pady=5)

speed = Scale(frame, from_=0.1, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Speed")
speed.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
