#!/usr/bin/python3
"""Fucntion that provideds a list of pascal number lists."""


def pascal_triangle(n):
    """Fucntion that provideds a list of pascal number lists."""

    if n <= 0:
        return([])

    else:
        my_list = []
        """number of rows"""

        for i in range(n):
            """number of columns"""
            temp_list = []

            for j in range(i+1):

                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    temp_list.append(my_list[i-1][j-1] + my_list[i-1][j])
            my_list.append(temp_list)
        return(my_list)
