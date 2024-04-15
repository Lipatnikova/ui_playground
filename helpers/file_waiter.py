import os
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWaiter(FileSystemEventHandler):
    def __init__(self, filename, callback):
        super().__init__()
        self.filename = filename
        self.callback = callback

    def on_created(self, event):
        if event.src_path.endswith(self.filename):
            self.callback()
            observer.stop()
            observer.join()


def wait_for_file(filename, directory, callback):
    file_path = os.path.join(directory, filename)
    event = threading.Event()

    observer = Observer()
    observer.schedule(FileWaiter(filename, callback), path=directory)
    observer.start()
    try:
        while not os.path.exists(file_path):
            event.wait(1)
    finally:
        observer.stop()
        observer.join()
