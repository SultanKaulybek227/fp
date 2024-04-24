import csv
def parse_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(map(dict, csv_reader))
            return data
    except Exception as e:
        print(f"Произошла ошибка при парсинге CSV-файла: {e}")
        return None

# Пример использования
if csv == "_main_":
    csv_file_path = "laba_8.csv"  # Путь к вашему CSV-файлу
    parsed_data = parse_csv(csv_file_path)

    if parsed_data:
        for row in parsed_data:
            print(row)
    else:
        print("Не удалось распарсить CSV-файл.")