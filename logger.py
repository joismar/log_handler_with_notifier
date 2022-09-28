import logging
import sys


class LoggerMeta(type):

    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class Logger(metaclass=LoggerMeta):

    def __init__(self, name=None):
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s - %(funcName)s : Linha %(lineno)d - %(message)s')
        self.handler = None
        self.logger = None
        self.name = name
        self.setup()

    def setup(self):
        self.logger = logging.getLogger(self.name)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setFormatter(self.formatter)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    @property
    def log(self):
        return self.logger

    @classmethod
    def destroy(self):
        self.logger.removeHandler(self.handler)
