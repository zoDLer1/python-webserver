from datetime import datetime
from .helpers import normalize_url
import os

try:
    from settings import DEFAULT_DEBUG_DIR
except ImportError:
    DEFAULT_DEBUG_DIR = "debug"



class Debug:

    def __init__(self) -> None:
        if not os.path.isdir(DEFAULT_DEBUG_DIR):
            os.makedirs(DEFAULT_DEBUG_DIR)

    def save_as_file(self, textdata: str, filename='debug', mode='w', ext='txt') -> None:
        now = datetime.timestamp(datetime.now())
        path = DEFAULT_DEBUG_DIR + normalize_url(filename)
        with open('.'.join([path, str(now), ext]), mode) as file:
            file.write(textdata)

