data = [
    ("Elon Musk", 433.9), ("Jeff Bezos", 239.4), ("Mark Zuckerberg", 211.8),
    ("Larry Ellison", 204.6), ("Bernard Arnault & Family", 181.3), ("Larry Page", 161.4)
]

# a. Selection Sort
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if lst[j][1] < lst[min_i][1]:
                min_i = j
        lst[i], lst[min_i] = lst[min_i], lst[i]

# b. Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j][1] > lst[j + 1][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# c. Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j][1] > key[1]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

from copy import deepcopy

for sort_fn in [selection_sort, bubble_sort, insertion_sort]:
    temp = deepcopy(data)
    sort_fn(temp)
    print({name: worth for name, worth in temp})
