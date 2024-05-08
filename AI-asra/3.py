# def dijkstra(graph,start,goal):
#     unvisited={n:float('inf')for n in graph.keys()}
#     unvisited[start]=0
#     visited={}
#     while unvisited:
#         minNode=min(unvisited,key=unvisited.get)
#         visited[minNode]=unvisited[minNode]
#         for n in graph.get(minNode):
#             if n in visited:

#                 continue
#             tempDist=unvisited[minNode]+graph[minNode][n]
#             if tempDist <unvisited[n]:
#                 unvisited[n]=tempDist
#         unvisited.pop(minNode)
#     print(f'{visited}')

def dijkstra(graph,start,end):
    unvisted={n:float('inf') for n in graph.keys()}
    unvisted[start]=0
    visited={}
    while unvisted:
        minNode=min(unvisted,key=unvisted.get)
        visited[minNode]=unvisted[minNode]
        if minNode==end:
            break
        for n in graph[minNode]:
            if n in visited:
                continue
            tempDist=unvisted[minNode]+graph[minNode][n]
            if tempDist < unvisted[n]:
                unvisted[n]=tempDist
        unvisted.pop(minNode)
    print(f'{visited}')
    return visited[end]


    
    







myGraph={
    'A':{'B':2,'C':9,'F':4},
    'B':{'C':6,'E':3,'F':2},
    'C':{'D':1},
    'D':{'C':2},
    'E':{'D':5,'C':2},
    'F':{'E':3}
}
cost=dijkstra(myGraph,'A','E')
