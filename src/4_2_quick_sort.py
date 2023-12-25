"""Selection sort

Time complexity: O(nlogn), O(n^2) - worst
Space complecity: O(logn)
"""


def quick_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items
    pivot = items[0]
    lt_items = [item for item in items[1:] if item < pivot]
    ge_items = [item for item in items[1:] if item >= pivot]
    return quick_sort(lt_items) + [pivot] + quick_sort(ge_items)


print(quick_sort([1, 4, 2, 6, 10, 5, 4]))
