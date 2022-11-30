#!/usr/bin/python3
"""A function to sperate words in python"""


def text_indentation(text):
    '''Fucntion to bring the texts'''
    if type(text) != str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)]
                )

    print("{}".format(text), end="")
