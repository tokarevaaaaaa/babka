# TODO Напишите функцию find_common_participants

def find_common_participants(one_group, two_group, sep = ','):
    general = []

    mas_name_group_1 = one_group.split(sep)
    mas_name_group_2 = two_group.split(sep)

    i = 0

    length_1 = len(mas_name_group_1)
    length_2 = len(mas_name_group_2)

    while( i < length_1):
        flag = 0
        j = 0
        while (j < length_2):
            if (mas_name_group_1[i] == mas_name_group_2[j]):
                if (mas_name_group_1[i] not in general):
                    general.append(mas_name_group_1[i])
            j += 1
        i += 1
    return sorted(general)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

res = find_common_participants(participants_first_group, participants_second_group, '|')

print(res)

# TODO Провеьте работу функции с разделителем отличным от запятой
