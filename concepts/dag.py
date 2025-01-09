# DAG Representation using Adjacency List
dag = {
    0: [1, 2],  # Node 0 points to Node 1 and Node 2
    1: [3],     # Node 1 points to Node 3
    2: [3],     # Node 2 points to Node 3
    3: []       # Node 3 has no outgoing edges (sink)
}

# Function to print all edges in the DAG
def print_dag_edges(graph):
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            print(f"Edge: {node} -> {neighbor}")

print("DAG Edges:")
print_dag_edges(dag)