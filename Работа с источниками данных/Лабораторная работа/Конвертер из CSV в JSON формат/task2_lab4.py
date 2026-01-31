# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    data = []

    # Читаем CSV файл
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        # Создаем reader для чтения CSV
        csv_reader = csv.DictReader(csv_file)

        # Преобразуем каждую строку в словарь
        for row in csv_reader:
            data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        # Записываем в JSON с отступами
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
