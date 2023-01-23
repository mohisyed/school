def almost_sorted(sorted_list, new_element):
    new_list = []
    i = 1
    counter = 0

    for i in range(len(sorted_list) - 1):
        if new_element < sorted_list[i]:
            print(new_element, "is less than ", sorted_list[i])

        elif new_element >= sorted_list[i]:
            print(new_element, "is greater than ", sorted_list[i])
            counter += 1
    for i in range(len(sorted_list)):
        if i == counter:
            new_list.append(new_element)
        else:
            new_list.append(sorted_list[i])
    return print(new_list)


if __name__ == '__main__':
    almost_sorted([1, 4, 7, 9, 12, 31, 44, 71], 17)
    almost_sorted([5, 6, 7, 8], 3)
