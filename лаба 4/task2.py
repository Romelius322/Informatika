# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = lines[0].strip().split(',')

    result = []
    for i in range(1, len(lines)):
        if lines[i].strip() == "":
            continue

        values = lines[i].strip().split(',')
        row_dict = {}
        for j in range(len(headers)):
            row_dict[headers[j]] = values[j]

        result.append(row_dict)
    ...  # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
