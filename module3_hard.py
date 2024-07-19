data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def parse_list(input_array):
    result_array = []
    for array_item in input_array:
        if isinstance(array_item, list) or isinstance(array_item, tuple) or isinstance(array_item, set):
            result_array.extend(parse_list(array_item))
        elif isinstance(array_item, dict):
            result_array.extend(parse_list([*array_item.items()]))
        else:
            result_array.append(array_item)
    return result_array


for item_list in parse_list(data_structure):
    count_list = [len(item_list) if isinstance(item_list, str) else item_list for item_list in
                  parse_list(data_structure)]
print(sum(count_list))

