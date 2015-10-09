origArr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
graph = {}

for i in range(len(origArr)):
    graph[origArr[i]] = []
    if (2*i)+1 < len(origArr):
        graph[origArr[i]].append(origArr[(2*i)+1])
    if (2*i)+2 < len(origArr):
        graph[origArr[i]].append(origArr[(2*i)+2])

print(graph)   
