"""Starter code for the Graph Route Algorithms assignment."""

from collections import deque
from heapq import heappop, heappush
from math import inf
from typing import Dict, List, Tuple

Graph = Dict[str, List[Tuple[str, int]]]


def build_sample_graph() -> Graph:
    """Return a sample weighted graph with bidirectional roads."""
    graph: Graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("D", 3), ("E", 8)],
        "C": [("A", 2), ("D", 7), ("F", 1)],
        "D": [("B", 3), ("C", 7), ("E", 2), ("G", 6)],
        "E": [("B", 8), ("D", 2), ("H", 5)],
        "F": [("C", 1), ("G", 4)],
        "G": [("D", 6), ("F", 4), ("H", 1)],
        "H": [("E", 5), ("G", 1)],
    }
    return graph


def shortest_hops_route(graph: Graph, start: str, end: str) -> Tuple[List[str], int]:
    """Find the route with the fewest stops using BFS.

    Return: (path, stops)
    - path is [] if no route exists
    - stops is the number of edges in the path
    """
    # TODO: validate nodes, run BFS, reconstruct route, and return (path, stops).
    raise NotImplementedError("Implement shortest_hops_route")


def shortest_distance_route(graph: Graph, start: str, end: str) -> Tuple[List[str], float]:
    """Find the route with the minimum total distance using Dijkstra.

    Return: (path, distance)
    - path is [] if no route exists
    - distance is inf if no route exists
    """
    # TODO: validate nodes, run Dijkstra with heapq, reconstruct route, return (path, distance).
    raise NotImplementedError("Implement shortest_distance_route")


def run_queries(graph: Graph, queries: List[Tuple[str, str]]) -> None:
    """Run and print both algorithms for each query."""
    for start, end in queries:
        bfs_path, bfs_stops = shortest_hops_route(graph, start, end)
        dijkstra_path, dijkstra_distance = shortest_distance_route(graph, start, end)

        print(f"Route: {start} -> {end}")
        print(f"  BFS (fewest stops): path={bfs_path}, stops={bfs_stops}")
        print(
            "  Dijkstra (shortest distance): "
            f"path={dijkstra_path}, distance={dijkstra_distance}"
        )
        print()


def main() -> None:
    graph = build_sample_graph()
    queries = [
        ("A", "E"),
        ("A", "H"),
        ("B", "F"),
    ]

    # Complexity summary:
    # BFS: O(V + E)
    # Dijkstra (binary heap): O((V + E) log V)
    run_queries(graph, queries)


if __name__ == "__main__":
    main()
