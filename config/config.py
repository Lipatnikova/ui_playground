import os


class Config:
    WAIT_TIMEOUT = 15
    DOWNLOAD_DIR = os.path.join(os.path.dirname(os.getcwd()), "data", "downloads")
