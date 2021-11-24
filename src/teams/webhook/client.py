import json
#from botocore.vendored import requests
import requests

class WebhookClient:
    def __init__(self, message, webhook_url):
        self.webhook_url = webhook_url
        self.message = message
    def sendMessage(self):
        try:
            web_hook_response = requests.post(self.webhook_url, json = self.message)
            return web_hook_response
        except Exception:
            print("WebhookClient Problem")
        
        