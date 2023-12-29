"""Selection sort

Time complexity: O(n^2)
Space complecity: O(1)
"""


states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {
    "kone": {"id", "nv", "ut"},
    "ktow": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"},
}


final_stations: set[str | None] = set()


while states_needed:
    best_station = None
    states_covered: set[str] = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
