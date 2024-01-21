from __future__ import annotations
import os
from datetime import datetime
from deep_translator import GoogleTranslator


en_to_ru = GoogleTranslator(source='english', target='russian').translate
ru_to_en = GoogleTranslator(source='russian', target='english').translate


class Logger:

    _loggers_map = dict()

    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def __call__(self, message: str):
        log(message, self.log_file_name)

    @staticmethod
    def get(log_file_name: str) -> Logger:
        logger = Logger._loggers_map.get(log_file_name, None)
        if logger is None:
            logger = Logger(log_file_name)
            Logger._loggers_map[log_file_name] = logger
        return logger


def log(message: str, log_file_name='log.txt'):
    if not os.path.exists(log_file_name):
        open(log_file_name, 'w')
    with open(log_file_name, 'a') as log_file:
        current_time = datetime.now().strftime('%d.%m %H:%M:%S')
        log_entry = f'\n{current_time} :: {message}'
        log_file.write(log_entry)



