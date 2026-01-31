import json
import os


# TODO решите задачу
def task() -> float:
    # Определяем путь к файлу относительно текущего скрипта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'input.json')

    # Читаем JSON файл
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Вычисляем сумму произведений score * weight
    total_sum = 0
    for item in data:
        # Проверяем, что оба ключа присутствуют в словаре
        if 'score' in item and 'weight' in item:
            total_sum += item['score'] * item['weight']

    # Округляем до 3 знаков после запятой
    return round(total_sum, 3)


print(task())
