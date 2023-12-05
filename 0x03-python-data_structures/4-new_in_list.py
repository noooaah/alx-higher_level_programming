#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list.copy()
    if 0 <= idx < len(list2):
        list2[idx] = element
        return list2
    return my_list
    
