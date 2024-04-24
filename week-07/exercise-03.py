my_list = [1,2,3,4,5]

def find_median(my_list):
    sorted_list = sorted(my_list)

    if len(sorted_list) % 2 == 1:
        return sorted_list[int((len(sorted_list) - 1) / 2)]
    else:
        return (sorted_list[int((len(sorted_list)) / 2) - 1] + sorted_list[int((len(sorted_list)) / 2)]) / 2

print(find_median(my_list))
