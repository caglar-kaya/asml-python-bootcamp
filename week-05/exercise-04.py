def generate_list_all(start, end):
    my_list = []
    for i in range(start + 1, end):
        my_list.append(i)
    print(my_list)

generate_list_all(4, 30)

def generate_list_even(start, end):
    my_list = []
    for i in range(start + 1, end):
        if i % 2 == 0:
            my_list.append(i)
    print(my_list)

generate_list_even(4, 30)
