### Thomas Silva
### Nov 6, 2023
### ENGR 103 Studio 6 Part 2
### This program takes a list of numbers as input and prints out the avarege of all numbers.


def find_median(numbers):
    numbers.sort()

    n = len(numbers)

    if n == 0:
        raise ValueError("Empty list, median cannot be calculated.")

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[(n - 1) // 2]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

numbers = [3,45, 66, 79, -45, 97]
median = find_median(numbers)
print("Median:", median)
