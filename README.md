# ui_playground

## Как работать с репозиторием на ПК:

1. Склонировать репозиторий `git clone "Clone using the web URL"`.
2. Перейти в директорию проекта.
3. Создать виртуальное окружение `python -m venv venv`.
4. Активировать виртуальное окружение для Windows: `venv\Scripts\activate.bat`; для Linux и MacOS: `source venv/bin/activate`.
5. Установить зависимости `pip install -r requirements.txt`.
6. Запустить тесты:
6. 1. Чтобы запустить тесты  с генерацией отчета Allure использовать команду `pytest -s -v --alluredir allure-results`.
7. 2. Или через Docker `docker-compose up regression`
7. Просмотреть отчет Allure
7. 1. `allure serve allure-results`.
7. 2. `allure generate allure-results --clean -o allure-report`.

## Как работать с репозиторием в Git Actions:

- Перейти во вкладку Actions репозитория. 
- Выбрать All workflows -> UI Tests("This workflow has a workflow_dispatch event trigger"). 
- Нажать на кнопку Run workflow.
- Выбрать Branch: main.
- Нажать на кнопку Run workflow.
