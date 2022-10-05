from logging import ERROR
from logger_with_notifier import NotifierHandler
from discord_notifier import DiscordNotifier
from logger import Logger


class LoggerWithDiscordNotifier(Logger):
    
    def __init__(self, *args, **kargs):
        Logger.__init__(self, *args, **kargs)
        discord_notifier = DiscordNotifier('DISCORD_WEBHOOK_URL')
        notifier_handler = NotifierHandler(discord_notifier)
        notifier_handler.setLevel(ERROR)
        
        self.logger.propagate = False
        self.logger.addHandler(notifier_handler)
