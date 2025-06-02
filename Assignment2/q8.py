def quick_sort(arr):
    def quick_sort_helper(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            quick_sort_helper(arr, low, p - 1)
            quick_sort_helper(arr, p + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j

    quick_sort_helper(arr, 0, len(arr) - 1)

arr = [37, 2, 6, 4, 89, 8, 10, 12, 68, 45]
quick_sort(arr)
print(arr)
