#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    for item in my_list:
        unique_set.add(item)
    result = sum(unique_set)
    return result
