def chop(lst):
    if len(lst) > 2:
        del lst[0]
        del lst[-1]
    else:
        lst.clear()
    return None
def middle(lst):
    if len(lst) > 2:
        return lst[1:-1]
    else:
        return []


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chop(my_list)
print(my_list)  

my_other_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = middle(my_other_list)
print(new_list)  
