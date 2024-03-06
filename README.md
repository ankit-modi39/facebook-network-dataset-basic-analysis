facebook network dataset is used to dedeuce the network properties

1. Node Count, Edge Count, Average Degree:
- Theory
 - Node count refers to the total number of nodes or vertices present in the network.
 - Edge count refers to the total number of edges or connections between nodes in the 
network.
 - Average degree is the average number of edges connected to each node in the network.
-Output Explanation: The network contains 4039 nodes and 88234 edges, with an average 
degree of approximately 43.69.
2. Degree Distribution:
- Theory:
 - Degree distribution describes the distribution of node degrees, which represents the 
number of edges incident to a node.
 - It provides insights into the connectivity patterns of the network.
- Output Explanation: The minimum degree in the network is 1, and the maximum degree is 
1045. The degree distribution plot visualizes the frequency of nodes at different degree levels.
3. Number of Triangles:
- Theory:
 - A triangle in a network refers to a set of three nodes that are fully interconnected.
 - Counting triangles helps in understanding the presence of closed loops or triadic 
relationships in the network.
- Output Explanation: The network contains a total of 1,612,010 triangles.
4. Diameter:
- Theory:
 - The diameter of a network is the maximum shortest path length between any pair of nodes.
 - It provides a measure of the network's overall reachability and efficiency of information 
flow.
- Output Explanation: The diameter of the network is 8.
5. Number of Components:
- Theory:
 - Connected components are disjoint subgraphs within a network where every pair of nodes 
is connected by at least one path.
 - The number of components indicates the network's overall connectivity structure.
- Output Explanation: The network consists of a single connected component.
6. Size of Largest Connected Component:
- Theory:
 - The size of the largest connected component is the number of nodes contained in the 
largest connected subgraph of the network.
 - It represents the extent of network cohesion and connectivity.
- Output Explanation: The largest connected component contains all 4039 nodes in the 
network.
7. Clustering Coefficient:
- Theory:
 - Clustering coefficient measures the degree to which nodes in a network tend to cluster 
together.
 - It quantifies the presence of cohesive subgroups or communities within the network.
- Output Explanation: The average clustering coefficient of the network is approximately 
0.61.
8. Centrality of the Vertices:
-Theory:
-Centrality measures assess the relative importance or influence of nodes within a network.
Different centrality metrics capture various aspects of node centrality, such as connectivity, 
control over information flow, and influence.
-Output Explanation:
The top 10 nodes by degree centrality, eigenvector centrality, Katz centrality, and PageRank 
centrality are listed, along with their respective centrality scores.
9. K-Cores in the Network:
-Theory:
-K-Cores represent the maximal subgraphs in which each node has a degree of at least k.
Finding k-cores helps identify densely connected regions or communities within the network.
-Output Explanation:
The k-core for a random k value between 0 and 20 is identified, showing the nodes within the 
k-core subgraph.
10. Number and Size of Cliques:
-Theory:
Cliques are subsets of nodes in which every node is directly connected to every other node.
Identifying cliques helps in understanding cohesive substructures or tightly-knit communities 
within the network.
-Output Explanation:
The total number of cliques, along with the sizes of the maximum and minimum cliques, are 
reported.
