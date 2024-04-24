my_list = [1,2,3,4,5,6]

def find_sum(my_list):
    sum = 0
    for i in my_list:
        sum += i

    return sum

print(find_sum(my_list))

def find_average(my_list):
    return find_sum(my_list) / len(my_list)

print(find_average(my_list))
