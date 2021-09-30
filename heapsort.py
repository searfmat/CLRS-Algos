import math

def left(i):
    return (i << 1) + 1

def right(i):
    return (i << 1) + 2

def maxHeapify(arr, i, heapsize):
    l = left(i)
    r = right(i)
    if l <= heapsize and arr[l] > arr[i]:
        largest = l  
    else:
        largest = i
    if r <= heapsize and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, heapsize)

def buildMaxHeap(arr, heapsize):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        maxHeapify(arr, i, heapsize)

def heapsort(arr, heapsize):
    buildMaxHeap(arr, heapsize)
    print("Array after build max heap: ", arr)
    for i in range(len(arr)):
        arr[heapsize], arr[0] = arr[0], arr[heapsize]
        heapsize = heapsize - 1
        maxHeapify(arr, 0, heapsize)
 

        
arr = [22,95,35,11,17,27,18,4,5]
heapsize = len(arr) - 1
heapsort(arr, heapsize)
print(arr)
