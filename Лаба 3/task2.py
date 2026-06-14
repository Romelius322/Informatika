# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, razdelitel=","):
    # Разбиваем строки на списки по разделителю
    # strip() убирает лишние пробелы (если вдруг они есть)
    spisok1 = str1.split(razdelitel)
    spisok2 = str2.split(razdelitel)
    # Очищаем каждый элемент от пробелов (на всякий случай)
    spisok1 = [imya.strip() for imya in spisok1]
    spisok2 = [imya.strip() for imya in spisok2]
    # Создаем пустой список для общих участников
    obschie = []
    # Проверяем каждого из первого списка
    for chelovek in spisok1:
        # Если есть во втором списке и еще не добавляли
        if chelovek in spisok2 and chelovek not in obschie:
            obschie.append(chelovek)
    # Сортируем список по алфавиту
    obschie.sort()
    # Возвращаем результат
    return obschie
# Данные для проверки
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
# Вызываем функцию, указываем разделитель "|"
result = find_common_participants(participants_first_group, participants_second_group, "|")

# Выводим результат
print("Общие участники:", result)
