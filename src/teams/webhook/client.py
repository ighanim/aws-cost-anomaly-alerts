# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json
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
        
        