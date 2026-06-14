numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Находим индекс пропущенного элемента (где значение None)
index_none = None
for i in range(len(numbers)):
    if numbers[i] is None:
        index_none = i
        break

# Считаем сумму всех чисел, кроме пропуска
summa = 0
for i in range(len(numbers)):
    if numbers[i] is not None:  # пропускаем None
        summa += numbers[i]

# Считаем количество элементов (включая пропуск)
kolichestvo = len(numbers)

# Вычисляем среднее арифметическое
# Формула: сумма всех чисел / общее количество элементов
srednee = summa / kolichestvo

# Заменяем пропущенный элемент на среднее арифметическое
numbers[index_none] = srednee

print("Измененный список:", numbers)
