# 04:20:00

unsorted_num_list = [3, 8, 6, 2, 10]

def selection_sort(values):
    sorted_num_list = []
    print("%-25s %-25s " % (values, sorted_num_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_num_list.append(values.pop(index_to_move))
        print("%-25s %-25s " % (values, sorted_num_list))
    return sorted_num_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i

    return  min_index

print(selection_sort(unsorted_num_list))