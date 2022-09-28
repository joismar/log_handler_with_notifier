import requests


class DiscordNotifier:
    def __init__(self, url):
        self.url = url
        
    def notify(self, content):
        json = {
            'content': content
        }
        requests.post(self.url, json=json, params={'wait': True})
