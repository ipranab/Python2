import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    left = [x for x in arr if x > pivot]
    right = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]

    L = len(left)
    if k <= L:
        return quickselect(left, k)
    elif k <= L + len(equal):
        return pivot
    else:
        return quickselect(right, k - L - len(equal))

arr = [7, 10, 4, 3, 20, 15]
print(quickselect(arr, 3))
