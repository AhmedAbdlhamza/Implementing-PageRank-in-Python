import networkx as nx
import matplotlib.pyplot as plt

# Load the graphs from the edgelist files
G1 = nx.read_edgelist('G1.edgelist', create_using=nx.DiGraph())
G2 = nx.read_edgelist('G2.edgelist', create_using=nx.DiGraph())

# Load the node categories from the node_info file
node_info = {}
with open('node_info.txt', 'r') as f:
    for line in f:
        node_id, category = line.strip().split()
        node_info[node_id] = category

# Define the nodes of interest
x0 = '0'
x1 = '1'

# Calculate the PageRank scores for both graphs over 200 iterations
pr1_x0 = nx.pagerank(G1, alpha=0.85, max_iter=200, personalization={n: 1 if n == x0 else 0 for n in G1.nodes()})
pr2_x0 = nx.pagerank(G2, alpha=0.85, max_iter=200, personalization={n: 1 if n == x0 else 0 for n in G2.nodes()})
pr1_x1 = nx.pagerank(G1, alpha=0.85, max_iter=200, personalization={n: 1 if n == x1 else 0 for n in G1.nodes()})
pr2_x1 = nx.pagerank(G2, alpha=0.85, max_iter=200, personalization={n: 1 if n == x1 else 0 for n in G2.nodes()})

# Plot the PageRank scores over 200 iterations for both graphs for x = 0
plt.plot(list(pr1_x0.values()), label='G1')
plt.plot(list(pr2_x0.values()), label='G2')
plt.legend()
plt.title(f'PageRank scores for node {x0}')
plt.xlabel('Iteration')
plt.ylabel('PageRank score')
plt.show()

# Plot the PageRank scores over 200 iterations for both graphs for x = 1
plt.plot(list(pr1_x1.values()), label='G1')
plt.plot(list(pr2_x1.values()), label='G2')
plt.legend()
plt.title(f'PageRank scores for node {x1}')
plt.xlabel('Iteration')
plt.ylabel('PageRank score')
plt.show()
