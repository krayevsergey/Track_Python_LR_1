numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
idx = numbers.index(None)
clean_sum = sum(x for x in numbers if x is not None)
average = clean_sum / len(numbers)

# Форматируем число с 2 знаками после запятой
average = float(f"{average:.2f}")

numbers[idx] = average
print("Измененный список:", numbers)

