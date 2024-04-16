import os
import time


def wait_for_file(filename, directory, timeout=3):
    """
    Ждет появления файла в указанной директории.

    Аргументы:
    filename (str): Имя файла, который нужно дождаться.
    directory (str): Путь к директории, в которой нужно искать файл.
    timeout (int, optional): Время ожидания в секундах. Если файл не будет
        найден в течение этого времени, будет выведена ошибка.
    """
    file_path = os.path.join(directory, filename)
    start_time = time.time()
    while not os.path.exists(file_path):
        if timeout is not None and time.time() - start_time > timeout:
            print(f"Ошибка: файл {filename} НЕ найден в директории {directory} в течение {timeout} секунд.")
            return
    print(f"Файл {filename} найден в директории {directory}")
