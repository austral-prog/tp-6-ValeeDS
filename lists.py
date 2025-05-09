# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    list = list_to_remove_elements[1:4] + list_to_remove_elements[6:]
    return list


def add_elements(list_to_add_elements):
    list = ['Pink'] + list_to_add_elements + ['Yellow']
    return list


def is_empty(list_to_check):
    return list_to_check == []


def check_lists(list_to_compare1, list_to_compare2):
    el1 = list_to_compare1[2:][:1]
    el2 = list_to_compare2[2:][:1]
    return el1 == el2


def list_of_lists(list_of_lists_to_modify):
    list1 = list_of_lists_to_modify[0][:2]
    list2 = list_of_lists_to_modify[1][1:4]
    list3 = list_of_lists_to_modify[2][-2:]
    list = [list1 , list2 , list3]
    return list