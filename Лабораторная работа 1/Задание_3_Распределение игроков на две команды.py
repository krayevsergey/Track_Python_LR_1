list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 # определяем количесвто игроков и делим общий список игроков пополам

first_team = list_players[:middle_index]  # первая команда - от начала до середины
second_team = list_players[middle_index:] # вторая команда - от середины и  до конца

print(first_team)
print(second_team)
