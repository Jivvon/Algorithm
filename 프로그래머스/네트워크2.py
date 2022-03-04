def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return True


def solution(n, computers):
    from collections import defaultdict
    graph = defaultdict(list)
    visited = [False] * n

    for i, computer in enumerate(computers):
        for j, flag in enumerate(computer):
            if i != j and flag:
                graph[i].append(j)

    print(graph)
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
