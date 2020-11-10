from CONSTANTS import LOGGING_FORMAT_STRING
import logging


class Logger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        self.formatter = logging.Formatter(LOGGING_FORMAT_STRING)
