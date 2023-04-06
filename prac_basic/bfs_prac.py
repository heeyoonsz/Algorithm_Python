from collections import deque
import sys

# n_com = int(input())


# '''
graph = [
    [],
    [2, 3],
    [1, 4, 6], [1, 5, 7], [2, 6], [3], [2, 4], [1, 3]

]
# '''

visited = [False]*len(graph)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    # global count
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                # count += 1


bfs(graph, 1, visited)
# print(count)
