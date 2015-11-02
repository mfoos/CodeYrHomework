import math as m

origArr = [5, 3, 17, 10, 84, 19, 6, 22, 9]

def heapify(array):

    start = m.floor(len(array)/2)-1

    def left(A,i):
        return 2*(i+1) - 1

    def right(A,i):
        return 2*(i+1)

    def parent(A,i):
        return m.floor((i+1)/2) - 1

    def sortHeapWithRoot(array, root):
        if left(array, root) > len(array) - 1: 
            # no children 
            return
        maxx = []
        idx = []
        if array[left(array, root)] > array[root]:
            # if LC > P
            if right(array, root) > len(array) - 1:
                # if no RC
                idx = left(array, root)
                maxx = array[idx]
            if array[left(array, root)] > array[right(array, root)]:
                # if LC > RC
                idx = left(array, root)
                maxx = array[idx]
            if array[right(array, root)] > array[left(array,root)]:
                # if RC > LC and by extension P
                idx = right(array, root)
                maxx = array[idx]
        elif right(array, root) > len(array) - 1:
            return
        elif array[right(array, root)] > array[root]:
            # if RC > P 
            idx = right(array, root)
            maxx = array[idx]
        if not (idx):
            return
        array[idx] = array[root] 
        array[root] = maxx
        sortHeapWithRoot(array, idx)

    while start >= 0:
        sortHeapWithRoot(origArr, start)
        start -= 1

heapify(origArr)
print("heap:",origArr)
soorted = []
while len(origArr) > 0:
    soorted.append(origArr.pop(0))
    origArr.insert(0, origArr.pop(len(origArr)-1))
    print("swapped:",origArr)
    heapify(origArr)
    print(origArr)
    print("sorted:", soorted)
print(soorted)
# gotta figure out how this scoping works
