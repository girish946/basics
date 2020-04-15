def unique_numbers(input_list):
    unique_number_list = []
    for i in input_list:
        if input_list.count(i) == 1:
            unique_number_list.append(i)
    return unique_number_list

def duplicate_numbers_count(input_list):
    duplicates = {}
    for i in input_list:
        c = input_list.count(i)
        if c > 1:
            duplicates[i] = c
    return duplicates

if __name__ == '__main__':
    l = [4, 5, 2, 3, 4, 7, 1, 1, 0, 0, 0]
    # l_unique = unique_numbers(l)
    # print(l_unique)
    dict_duplicate = duplicate_numbers_count(l)
    print(dict_duplicate)
