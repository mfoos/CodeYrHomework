import math as m

origArr = [5, 3, 17, 10, 84, 19, 6, 22, 9]

start = m.floor(len(origArr)/2)-1

def left(A,i):
    return 2*(i+1)-1

def right(A,i):
    return 2*(i+1)

def parent(A,i):
    return m.floor((i+1)/2 - 1)

print(origArr)

def sortHeapWithRoot(array, root):
    print("index-indicated root", root)
    maxx = []
    idx = []
    if array[left(array, root)] > array[root]:
        if array[left(array, root)] > array[right(array, root)]:
            maxx = array[left(array, root)]
            idx = left(array, root)
            array[left(array, root)] = array[root] 
            array[root] = maxx
            
        if array[right(array, root)] > array[root]:
            maxx = array[right(array, root)]
            idx = right(array, root)
            array[right(array, root)] = array[root] 
            array[root] = maxx
    print("new root:",idx)
    if left(array, idx) > len(array) - 1:
        print("kill recursion")
        return
    sortHeapWithRoot(array, idx)

while start >= 0:
    sortHeapWithRoot(origArr, start)
    start -= 1

print(origArr)

