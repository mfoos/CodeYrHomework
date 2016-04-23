import math as m

def heapify(origArr):
    start = int(m.floor(len(origArr)/2)-1)

    def left(i):
        return 2*(i+1) - 1

    def right(i):
        return 2*(i+1)

    def parent(i):
        return m.floor((i+1)/2) - 1

    def sortHeapWithRoot(array, root):
        if left(root) > len(array) - 1: 
            # no children 
            return
        maxx = []
        idx = []
        if array[left(root)] > array[root]:
            # if LC > P
            if right(root) > len(array) - 1:
                # if no RC
                idx = left(root)
            elif array[left(root)] > array[right(root)]:
                # if LC > RC
                idx = left(root)
            elif array[right(root)] > array[left(root)]:
                # if RC > LC and by extension P
                idx = right(root)
            maxx = array[idx]
        elif right(root) > len(array) - 1:
            return
        elif array[right(root)] > array[root]:
            # if RC > P 
            idx = right(root)
            maxx = array[idx]
        if not (idx):
            return
        array[idx] = array[root] 
        array[root] = maxx
        sortHeapWithRoot(array, idx)

    while start >= 0:
        sortHeapWithRoot(origArr, start)
        start -= 1

    return origArr
