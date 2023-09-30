import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

def dfs_search(graph, start, end, visited, path):
    visited[start] = True
    path.append(start)

    if start == end:
        return path

    for neighbor in graph.neighbors(start):
        if not visited[neighbor]:
            new_path = dfs_search(graph, neighbor, end, visited, path)
            if new_path:
                return new_path

    path.pop()
    visited[start] = False
    return None


nodes = {'A': (1, 1), 'B': (0, 0.5), 'C': (4, 1), 'D': (2, 2), 'E': (1, -0.5)}
edges = [(0, 1), (1, 4), (1, 2), (4, 2), (2, 3)]


graph = ig.Graph(directed=True)
graph.add_vertices(len(nodes))
graph.add_edges(edges)


start_node = 0  
end_node = 3    

# DFS Function
visited = [False] * len(graph.vs)
path = dfs_search(graph, start_node, end_node, visited, [])

fig, ax = plt.subplots()

# nodes and edges
for node, pos in nodes.items():
    ax.scatter(pos[0], pos[1], s=200, color='orange', label=node)
    ax.text(pos[0], pos[1], node, fontsize=12, ha='center')

for edge in edges:
    start_node, end_node = edge
    start_pos = nodes[list(nodes.keys())[start_node]]
    end_pos = nodes[list(nodes.keys())[end_node]]
    ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='black', linewidth=2)

# Highlighting the DFS path
if path:
    path_coords = [nodes[list(nodes.keys())[v]] for v in path]
    path_x, path_y = zip(*path_coords)
    ax.plot(path_x, path_y, color='red', linewidth=2)
    ax.quiver(path_x[:-1], path_y[:-1], np.diff(path_x), np.diff(path_y), angles='xy', scale_units='xy', scale=1, color='red')

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.set_title('Depth First Search')
ax.set_xlabel('Vertex')
ax.set_ylabel('')
plt.show()
