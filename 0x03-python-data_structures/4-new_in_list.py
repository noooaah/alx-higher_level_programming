#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        list2 = my_list
        list2[idx] = element
        return list2
    return my_list
    
