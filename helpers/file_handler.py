from typing import List

import allure
import os

from helpers.file_waiter import wait_for_file
from helpers.file_reader import FileReader


class FileHandler(FileReader):
    def __init__(self):
        self.path_to_directory = os.path.join(os.path.dirname(os.getcwd()), "data", "downloads")
        self.path_to_file = os.path.join(self.path_to_directory, "contacts.csv")

    @staticmethod
    def file_created_callback(driver):
        driver.quit()

    def wait_for_file_downloads(self) -> None:
        with allure.step('Подождать загрузки файла "contacts.csv" в директорию ../data/downloads/'):
            wait_for_file("contacts.csv", self.path_to_directory, self.file_created_callback)

    def extract_first_names_by_csv(self) -> List[str]:
        with allure.step('Получить из скаченного файла .csv значения из столбца first_name'):
            return self.read_column_from_csv(self.path_to_file, "first_name")

    def extract_last_names_by_csv(self) -> List[str]:
        with allure.step('Получить из скаченного файла .csv значения из столбца last_name'):
            return self.read_column_from_csv(self.path_to_file, "last_name")

    def extract_last_seen_by_csv(self) -> List[str]:
        with allure.step('Получить из скаченного файла .csv значения из столбца last_seen'):
            return self.read_column_from_csv(self.path_to_file, "last_seen")

    def delete_downloaded_file(self) -> None:
        with allure.step('Удалить скаченный файл и директорию "download"'):
            self.delete_file_and_directory(self.path_to_file)
