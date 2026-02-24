from collections import defaultdict

def solve(v1, v2, edges):
    graph = defaultdict(list)
    graph_rev = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph_rev[edge[1]].append(edge[0])

    path_v1, path_v2 = [], []

    def dfs(path):
        nonlocal path_v1, path_v2
        node = path[-1]
        if not node:
            return
        elif node == v1:
            path_v1 = path.copy()
        elif node == v2:
            path_v2 = path.copy()
        if not (path_v1 and path_v2):
            for child in graph[node]:
                path.append(child)
                dfs(path)
                path.pop()

    dfs([1])
    # print(path_v1, path_v2)
    for i in range(len(path_v1) - 1):
        if path_v1[i] == path_v2[i] and path_v1[i + 1] != path_v2[i + 1]:
            common_node = path_v1[i]
            break

    n_nodes = 0
    def dfs_v2(node):
        nonlocal n_nodes
        if not node:
            return
        n_nodes += len(graph[node])
        for child in graph[node]:
            dfs_v2(child)
    dfs_v2(common_node)
    return common_node, n_nodes + 1



import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    V, E, v1, v2 = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]
    answer = solve(v1, v2, arr)
    print(f"#{test_case} {answer[0]} {answer[1]}")