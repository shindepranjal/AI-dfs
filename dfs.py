# DFS Traversal
'''
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def dfs(node):
    visited.append(node)
    print(node, end=" ")

    for child in tree[node]:
        if child not in visited:
            dfs(child)

dfs('A')

'''



# DFS using User Input

tree = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    children = input("Enter children separated by space: ").split()
    tree[node] = children

start = input("Enter starting node: ")

visited = []

def dfs(node):
    visited.append(node)
    print(node, end=" ")

    for child in tree[node]:
        if child not in visited:
            dfs(child)

dfs(start)