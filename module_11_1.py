import pandas as pd
import json

# Функция для обработки JSON и добавления данных в DataFrame
def process_json_file(input_file, output_file):
    formatted_data = []

    # Чтение и обработка большого JSON файла
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            entry = json.loads(line)  # Если файл в формате "один JSON объект на одну строку"
            formatted_entry = {
                "name": entry.get("name", ""),
                "company": entry.get("company", ""),
                "phone": ", ".join(entry.get("phone", [])) if isinstance(entry.get("phone", []), list) else entry.get("phone", ""),
                "email": ", ".join(entry.get("email", [])) if isinstance(entry.get("email", []), list) else entry.get("email", "")
            }
            formatted_data.append(formatted_entry)

    # Создание DataFrame
    df = pd.DataFrame(formatted_data)

    # Сохранение в Excel
    df.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Данные успешно сохранены в файл: {output_file}")

# Пример вызова функции
process_json_file('1-50.json', 'output.xlsx')