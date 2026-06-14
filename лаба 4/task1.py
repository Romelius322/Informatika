# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Заголовки из первой строки (разделитель - запятая)
    headers = lines[0].strip().split(',')

    result = []

    # Обрабатываем строки с данными
    for i in range(1, len(lines)):
        if lines[i].strip() == "":
            continue

        values = lines[i].strip().split(',')

        # Создаем словарь
        row_dict = {}
        for j in range(len(headers)):
            row_dict[headers[j]] = values[j]

        result.append(row_dict)

    # Записываем JSON с отступами 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()

    # Выводим результат
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
