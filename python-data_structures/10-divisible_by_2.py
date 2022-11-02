#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_check = list()
    for number in my_list:
        if number % 2 == 0:
            div_check.append(True)
        else:
            div_check.append(False)
    return(div_check)
