# TODO Напишите функцию для поиска индекса товара
# Функция для поиска товара в списке
def poisk_tovara(spisok, tovar):
    # Проходим по всем индексам списка
    for i in range(len(spisok)):
        # Если нашли нужный товар
        if spisok[i] == tovar:
            return i  # возвращаем его индекс
    # Если ничего не нашли
    return None

# Дан список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
# Проверяем три товара
for find_item in ['банан', 'груша', 'персик']:
    # Вызываем функцию
    index_item = poisk_tovara(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
