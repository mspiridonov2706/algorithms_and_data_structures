"""Bridth First Search sort

Time complexity: O(V + E) V - num of vertexes, E - num of edges
"""

from collections import deque


def bfs_search(graph: dict[str, list[str]]) -> bool:
    search_queue: deque[str] = deque()
    search_queue += graph["you"]

    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"person {person} is mango seller")
                return True
            search_queue += graph[person]
            searched.add(person)
    return False


def person_is_seller(person: str) -> bool:
    return person == "Thom"


graph = {}
graph["you"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Thom"] = []
graph["Jonny"] = []


print(bfs_search(graph))
