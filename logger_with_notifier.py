from logging import StreamHandler


class NotifierHandler(StreamHandler):
    def __init__(self, notifier):
        StreamHandler.__init__(self)
        self.notifier = notifier

    def emit(self, record):
        msg = self.format(record)
        self.notifier.notify(msg)
