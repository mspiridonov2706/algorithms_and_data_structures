from typing import Any, List


def sum(items: List[int]) -> int:
    "Task 4.1 Напишите код для функции sum"

    if len(items) == 1:
        return items[0]
    return items[0] + sum(items[1:])


def count_list(items: list[Any]) -> int:
    "Task 4.2 Напишите рекурсивную функцию для подсчета элементов в списке."

    if len(items) == 1:
        return 1
    return 1 + count_list(items[1:])


def find_max(items: list[int]) -> int:
    "Task 4.3 Найдите наибольшее число в списке"

    if len(items) == 1:
        return items[0]
    if items[0] > find_max(items[1:]):
        return items[0]
    return find_max(items[1:])


def binary_search(items: list[int], target: int) -> bool:
    if len(items) == 0:
        return False
    mid = len(items) // 2
    guess = items[mid]
    if guess == target:
        return True
    if guess > target:
        return binary_search(items[:mid], target)
    return binary_search(items[mid + 1 :], target)


items = [1, 2, 3, 4, 5, 6]
print(f"sum of items: {sum(items)}")
print(f"count of items {count_list(items)}")
print(f"max of items: {find_max(items)}")
print(f"target has founded: {binary_search(items, 7)}")
