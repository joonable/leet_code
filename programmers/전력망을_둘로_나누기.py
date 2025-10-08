from collections import defaultdict
def solution(n, wires):
    def dfs(node, visited, graph):
        visited.add(node)
        count = 1
        for next_node in graph[node]:
            if next_node not in visited:
                count += dfs(next_node, visited, graph)
        return count

    min_abs = float("inf")
    for i in range(n - 1):
        visited = set()
        graph = defaultdict(list)
        for x, y in wires[:i] + wires[i + 1:]:
            graph[x].append(y)
            graph[y].append(x)
        count = dfs(wires[0][0], visited, graph)
        min_abs = min(abs(count - (n - count)), min_abs)
    return min_abs