
def find_common_participants(group1, group2, separator=','):
    list1 = [name.strip() for name in group1.split(separator)]
    list2 = [name.strip() for name in group2.split(separator)]
    common = set(list1) & set(list2)
    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    '|'
)
print(f"Общие участники: {common_participants}")


