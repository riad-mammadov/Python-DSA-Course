def quicksort(arr,l,r):
    if l < r:
        partition = partition(arr,l,r)
        quicksort(arr,l,partition - 1)
        quicksort(arr,r,partition + 1)

def partition(arr,l,r):
    i = l
    j = r - 1
    pivot = arr[r]
    while i < j:
        while i < r and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[r] = arr[r], arr[i]
    return i


    