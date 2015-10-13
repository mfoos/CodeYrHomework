import math as m


origArr = [5, 3, 17, 10, 84, 19, 6, 22, 9]

start = m.floor(len(origArr)/2)-1
print(start)

def left(A,i):
    return 2*(i+1)-1

def right(A,i):
    return 2*(i+1)

print(origArr)
while start >= 0:
    maxx = []
    if origArr[left(origArr, start)] > origArr[start]:
        if origArr[left(origArr, start)] > origArr[right(origArr, start)]:
            maxx =  origArr[left(origArr, start)]
            origArr[left(origArr, start)] = origArr[start] 
            origArr[start] = maxx
            
        if origArr[right(origArr, start)] > origArr[start]:
            maxx =  origArr[right(origArr, start)]
            origArr[right(origArr, start)] = origArr[start] 
            origArr[start] = maxx
        print(origArr)
    start -= 1
