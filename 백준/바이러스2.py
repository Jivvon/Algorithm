nodes = int(input())
edges = int(input())
graph = [[] * nodes for _ in range(nodes + 1)]
for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False] * (nodes + 1)


def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(count)
