g={
    0:[1,2],
    1:[0,3,4],
    2:[3,0],
    3:[2,1,4],
    4:[3,1]
}
#vis=[0]*5
def dfs(g,s):
    vis[s]=1
    print(s)
    for c in g[s]:
        if  not  vis[c]:
            dfs(g,c)

def bfs(g,s):
    q=[s]
    vis=[s]
    while q:
        curr=q.pop(0)
        print(curr)
        for c in g[curr]:
            if c not in vis:
                q.append(c)
                vis.append(c)
            
#dfs(g,0)
bfs(g,0)
