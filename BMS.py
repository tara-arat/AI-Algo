import igraph as ig
import matplotlib.pyplot as plt

def b_m_s(graph, start, end):
   

    queue = [(start, [])]
    visited = set()

    while queue:
        vertex, path = queue.pop(0)
        if vertex == end:
            return path + [vertex]
        if vertex not in visited:
            visited.add(vertex)
            try:
                for neighbor in graph.neighbors(vertex):
                    queue.append((neighbor, path + [vertex]))
            except ValueError:
                pass

    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = find_all_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Defining the Graph
nodes = {'A': (1, 1), 'B': (0, 0.5), 'C': (4, 1), 'D': (2, 2), 'E': (1, -0.5)} # Nodes

edges = [(0, 1), (1, 4), (1, 2), (4, 2), (2, 3)] #Edges

graph = ig.Graph(directed=True)
graph.add_vertices(len(nodes))
graph.add_edges(edges)

paths = find_all_paths(graph, 0, 3)  

# Creating the figure
fig, ax = plt.subplots()

# Nodes
for node, pos in nodes.items():
    ax.scatter(pos[0], pos[1], s=200, color='orange', label=node)
    ax.text(pos[0], pos[1], node, fontsize=12, ha='center')

# Edges with increased spacing
for edge in edges:
    start_node = edge[0]
    end_node = edge[1]
    start_pos = nodes[list(nodes.keys())[start_node]]
    end_pos = nodes[list(nodes.keys())[end_node]]
    ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='black', linewidth=2)

# Highlighting the paths 
for path in paths:
    for i in range(len(path) - 1):
        start_node = path[i]
        end_node = path[i + 1]
        start_pos = nodes[list(nodes.keys())[start_node]]
        end_pos = nodes[list(nodes.keys())[end_node]]
        ax.annotate('', xy=end_pos, xytext=start_pos, arrowprops={'arrowstyle': '->', 'linestyle': 'dashed', 'linewidth': 3})

# Plot
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.set_title('British Museum Search')
ax.set_xlabel('Vertex')
ax.set_ylabel('')

plt.show()