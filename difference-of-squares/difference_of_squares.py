import numpy as np


def square_of_sum(n):
    numbers = range(1, n+1)
    sum = np.sum(numbers)
    return np.power(sum, 2)


def sum_of_squares(n):
    numbers = range(1, n+1)
    squares = map((lambda x: x**2), numbers)
    sum_of_squares = np.sum(squares)
    return sum_of_squares


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)