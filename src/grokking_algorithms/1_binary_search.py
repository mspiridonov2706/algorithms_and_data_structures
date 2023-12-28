"""Binary Search

Time complexity: log(n)
"""


def binary_search(items: list[int], target: int):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [num for num in range(0, 1000000)]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
