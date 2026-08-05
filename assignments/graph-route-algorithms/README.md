# 📘 Assignment: Graph Route Algorithms

## 🎯 Objective

Model a city map as a weighted graph and implement pathfinding algorithms to solve routing problems. By the end, you will compare different strategies and justify algorithm choices based on complexity and output quality.

## 📝 Tasks

### 🛠️ Build a Graph Representation

#### Descrição
Create a graph data structure using an adjacency list where each connection stores destination and distance.

#### Requisitos
O programa concluído deve:

- Represent the map as `dict[str, list[tuple[str, int]]]`
- Include at least 8 nodes and 12 weighted edges in the provided sample map
- Support bidirectional roads by adding both directions
- Keep graph creation logic in a reusable function

### 🛠️ Implement Shortest Route by Number of Stops (BFS)

#### Descrição
Implement a breadth-first search to find the route with the fewest stops between two points.

#### Requisitos
O programa concluído deve:

- Implement a function `shortest_hops_route(graph, start, end)`
- Return both the path and number of stops
- Handle invalid nodes with a clear exception message
- Return an empty path when no route exists

### 🛠️ Implement Shortest Route by Distance (Dijkstra)

#### Descrição
Implement Dijkstra's algorithm to find the minimum total distance route.

#### Requisitos
O programa concluído deve:

- Implement a function `shortest_distance_route(graph, start, end)`
- Use a priority queue (`heapq`) for efficiency
- Return both the path and total distance
- Return an empty path and infinite distance when no route exists

### 🛠️ Compare and Explain Algorithm Behavior

#### Descrição
Run both algorithms on multiple start/end pairs and explain when each result differs and why.

#### Requisitos
O programa concluído deve:

- Execute at least 3 route queries in `main()`
- Print outputs from BFS and Dijkstra side by side
- Include a short complexity summary for BFS and Dijkstra in comments
- Include one case where the shortest-by-stops path is not the shortest-by-distance path
