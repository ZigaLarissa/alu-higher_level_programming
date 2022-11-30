#!/usr/bin/python3
"""A function that prints the sqaures"""


def print_square(size):
    '''FUnction to print the squares
    Args:
        size : must be an integer
    Returns:
        prints the square
    '''
    square_char = "#"
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print(square_char, end="")
        print()
