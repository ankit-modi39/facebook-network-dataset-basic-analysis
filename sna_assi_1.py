

import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.read_csv(
    "/content/facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

df

#Returns a graph from Pandas DataFrame containing an edge list.
G = nx.from_pandas_edgelist(df, "start_node", "end_node")

plot_options = {"node_size": 10, "with_labels": False, "width": 0.15}
pos = nx.spring_layout(G, iterations=15, seed=1721)
fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
nx.draw_networkx(G, pos=pos, ax=ax, **plot_options)

"""1. Node Count, Edge Count, Average Degree

"""

G.number_of_nodes()

G.number_of_edges()

G.degree()

#average degree in the graph using numpy
np.mean([i for _,i in G.degree()])

"""2. Degree distribution


"""

degrees = dict(G.degree())
min_degree=min(degrees.values())
max_degree=max(degrees.values())
print("minimum degree:",min_degree)
print("maximum degree:",max_degree)

# Count the frequency of each degree
degree_values = list(degrees.values())
degree_freq = {degree: degree_values.count(degree) for degree in set(degree_values)}

# Plot the degree distribution
plt.bar(degree_freq.keys(), degree_freq.values())
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

"""3. No of Triangles

"""

# variable t returns a dictionary with each node denoting the no of triangle it belongs to, so for 1 triangle 3 nodes are counted
t=nx.triangles(G)
no_of_triangles=sum(t.values())//3
print(no_of_triangles)

"""4. Diameter
"""

nx.diameter(G)

"""5. No of components

"""

nx.number_connected_components(G)

"""6. Size of largest connected components

"""

cc=list(nx.connected_components(G))
component_sizes=[len(c) for c in cc]
largestConnectedComponent=max(component_sizes)
print("the size of largest connected components is :",largestConnectedComponent)
#also it can be seen that as there is only one component then that would be the largest so it constitutes of all the nodes i.e. 4039

"""7. Clustering Coefficient

"""

#clustering coefficient of each node
nx.clustering(G)

# average clustering coefficient of the graph
nx.average_clustering(G)

plt.figure(figsize=(15, 8))
plt.hist(nx.clustering(G).values(), bins=50,edgecolor="white")
plt.title("Clustering Coefficient Histogram ", fontdict={"size": 35}, loc="center")
plt.xlabel("Clustering Coefficient", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})

"""8. **Centrality of the vertices**

---

# Degree centrality

"""

degrees=nx.degree_centrality(G)
print(degrees)

sortedNodes=sorted(degrees.items(),key=lambda x:x[1],reverse=True)
#print top 10 nodes with highest degree centrality
print("Top 10 nodes by degree centrality:")
for node, centrality in sortedNodes[:10]:
    print("Node:", node, "Degree Centrality:", centrality)

#no of neighbours of each highest degree centrality nodes
(sorted(G.degree, key=lambda item: item[1], reverse=True))[:10]

plt.figure(figsize=(15, 8))
plt.hist(degrees.values(), bins=25,edgecolor="white")
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
plt.title("Degree Centrality Histogram ", fontdict={"size": 35}, loc="center")
plt.xlabel("Degree Centrality", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})

"""#Eigenvector Centrality"""

eigenVectorCentrality=nx.eigenvector_centrality(G)
print(eigenVectorCentrality)

(sorted(eigenVectorCentrality.items(), key=lambda item: item[1], reverse=True))[:10]

plt.figure(figsize=(15, 8))
plt.hist(eigenVectorCentrality.values(), bins=25,edgecolor="white")
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
plt.title("Eigenvector Centrality Histogram ", fontdict={"size": 35}, loc="center")
plt.xlabel("Eigenvector Centrality", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})

"""#katz centrality"""

kz=nx.katz_centrality_numpy(G)
print(kz)

(sorted(kz.items(),key=lambda item:item[1],reverse=True))[:10]

plt.figure(figsize=(15, 8))
plt.hist(kz.values(), bins=25,edgecolor="white")
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
plt.title("katz Centrality Histogram ", fontdict={"size": 35}, loc="center")
plt.xlabel("katz Centrality", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})

"""#PageRank Centrality"""

pr=nx.pagerank(G)
print(pr)

(sorted(pr.items(),key=lambda item:item[1],reverse=True))[:10]

plt.figure(figsize=(15, 8))
plt.hist(pr.values(), bins=25,edgecolor="white")
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
plt.title("Pagerank Centrality Histogram ", fontdict={"size": 35}, loc="center")
plt.xlabel("Pagerank Centrality", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})

"""#Betweenness Centrality"""

bc=nx.betweenness_centrality(G)
print(bc)

(sorted(pr.items(),key=lambda item:item[1],reverse=True))[:10]

plt.figure(figsize=(15, 8))
plt.hist(bc.values(), bins=25,edgecolor="white")
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
plt.title("Betweeness Centrality Histogram ", fontdict={"size": 35}, loc="center")
plt.xlabel("Betweenness Centrality", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})

"""9. For a random k between 0-20 find all the k-cores in the network.


"""

#take k=15
kc=nx.k_core(G,k=15)
print(f"k-Core for k = {15}: {kc.nodes()}")

nx.draw(kc, with_labels=False, node_color='skyblue', node_size=500, edge_color='black')
# plt.subplot(122)
# nx.draw(kc)
plt.show()

"""10. Report the number and size of the maximum and minimum clique

"""

# Find all cliques in the graph
all_cliques = list(nx.find_cliques(G))

# Find the maximum and minimum cliques
max_clique = max(all_cliques, key=len)
min_clique = min(all_cliques, key=len)

# Report the number and size of the maximum and minimum cliques
print(f"Number of cliques: {len(all_cliques)}")
print(f"Maximum clique: {max_clique}, Size: {len(max_clique)}")
print(f"Minimum clique: {min_clique}, Size: {len(min_clique)}")