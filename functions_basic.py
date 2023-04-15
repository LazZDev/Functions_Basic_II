def countdown(number):
    countdown_list = []
    for i in range(number, -1, -1):
        countdown_list.append(i)
    return countdown_list


result = countdown(5)
print(result)


def two_nums_list(list):
    print(list[0])

    return list[1]


result = two_nums_list([1, 2])
print(result)


def first_plus_length(my_list):
    return my_list[0] + len(my_list)


result = first_plus_length([1, 2, 3, 4, 5])
print(result)


def values_greater_than_second(list):
    if len(list) < 2:
        return False

    second_val = list[1]

    new_list = []

    for val in list:
        if val > second_val:
            new_list.append(val)

    print(len(new_list))
    return new_list


result1 = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result1)


def length_and_value(size, value):
    new_list = [value] * size

    return new_list


result = length_and_value(4, 7)
print(result)

result2 = length_and_value(6, 2)
print(result2)
