# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator=","):    #
    first_group_list = first_group.split(separator)
    second_group_list = second_group.split(separator)
    common_participants = sorted(set(first_group_list).intersection(set(second_group_list)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
