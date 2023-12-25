def factorial(number: int) -> int:
    if number == 0:
        return 1
    if number == 1:
        return number
    return number * factorial(number - 1)


print(factorial(0))
