import csv
import os


class FileReader:
    @staticmethod
    def read_column_from_csv(path_to_file, column_header):

        column_values = []
        with open(path_to_file, encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")
            for row in file_reader:
                if column_header in row:
                    column_values.append(row[column_header])

        return column_values

    @staticmethod
    def delete_file_and_directory(path_to_file):
        try:
            if os.path.exists(path_to_file):
                os.remove(path_to_file)

                directory = os.path.dirname(path_to_file)
                if not os.listdir(directory):  # проверяем, пуст ли каталог
                    os.rmdir(directory)  # если каталог пустой, удаляем его
            else:
                print(f"Файл {path_to_file} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла {path_to_file}: {e}")
