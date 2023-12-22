"""Selection sort

Time complexity: n^2
Space complecity: O(1)
"""


def selection_sort(items: list[int]):
    size = len(items)

    for idx in range(0, size):
        min_idx = idx

        for idx_2 in range(idx + 1, size):
            if items[idx_2] < items[min_idx]:
                min_idx = idx_2

        items[idx], items[min_idx] = items[min_idx], items[idx]


my_list = [5, 3, 6, 2, 10]
selection_sort(my_list)

print(my_list)
