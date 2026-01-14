# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, separator=","):
    """
    Сначала находим общих участников среди двух групп.
    Args:
        participants_first_group: строка с участниками первой группы
        participants_second_group: строка с участниками второй группы
        separator: разделитель в строках (по умолчанию запятая)
    Returns:
        Список общих участников, отсортированных в алфавитном порядке
    """
    # Затеми разделяем строки на списки участников
    group1 = participants_first_group.split(separator)
    group2 = participants_second_group.split(separator)
    # Находим пересечение множеств участников
    common = set(group1) & set(group2)
    # Возвращаем отсортированный список
    return sorted(list(common))
# Исходные данные из задания:
participants_first_group = "Иванов Петр,Сидоров Борис"
participants_second_group = "Петров,Сидоров Борис,Смирнов"
# Вызов функции с разделителем по умолчанию (запятая)
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group
)
# Вывод результата
print("Общие участники:", common_participants)
# Для данных с вертикальной чертой в качестве разделителя
participants_first_group = "Иванов Петр|Сидоров Борис"
participants_second_group = "Петров|Сидоров Борис|Смирнов"

common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)
print("Общие участники (разделитель |):", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
