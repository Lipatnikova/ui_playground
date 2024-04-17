import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config import Config


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    download_directory = Config.DOWNLOAD_DIR
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    options = Options()
    prefs = {
        "download.default_directory": download_directory
    }
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
