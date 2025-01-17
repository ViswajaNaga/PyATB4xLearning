#LIST
# to remove duplicates from the list-->set is used - data
my_shopping_list=["bread","butter","milk"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    new_item = input("enter new item \n")
    my_list.append(new_item)
    # my_list.insert(0,new_item)
    my_list.remove(new_item)
    return my_list

list= bring_more_food(my_shopping_list)
print(list)

