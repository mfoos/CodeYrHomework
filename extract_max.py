from heapify import heapify # homemade module

origArr = [5, 3, 17, 10, 84, 19, 6, 22, 9]

heapify(origArr)
print("heap:",origArr)
sorted_array = []
while len(origArr) > 0:
    if len(origArr) == 1:
        sorted_array.append(origArr[0])
        break 
    else:
        sorted_array.append(origArr.pop(0))
        origArr.insert(0, origArr.pop(-1))
        heapify(origArr)
        print(origArr)
print("done", sorted_array)
