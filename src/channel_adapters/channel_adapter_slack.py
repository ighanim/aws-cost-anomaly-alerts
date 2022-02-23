# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json
from slack_sdk.webhook import WebhookClient
from slack.models import Block, Text, Field

class SlackNotification:
    def __init__(self, anomalyEvent, webhook_url):
        self.anomalyEvent = anomalyEvent
        self.webhook_url = webhook_url
    def constructMessage(self, anomalyEvent):
        
        ##print(json.dumps(self.anomalyEvent.__dict__))
        
        anomalyEvent = self.anomalyEvent
        
        #Initialise the Slack blocks elements that holds the all the notification components. 
        blocks = []
        #Notification Header
        blocks.append(Block("header", text = Text("plain_text", ":warning: Cost Anomaly Detected ", emoji = True).__dict__))
        
        #Notification Top Elements
        blocks.append(Block("section", text = Text("mrkdwn", "*Total Anomaly Cost*: $" + str(anomalyEvent.anomalyTotalImpact)).__dict__))
        blocks.append(Block("section", text = Text("mrkdwn", "*Anomaly Start Date*: " + str(anomalyEvent.anomalyStartDate)).__dict__))
        blocks.append(Block("section", text = Text("mrkdwn", "*Anomaly End Date*: " + str(anomalyEvent.anomalyEndDate)).__dict__))
        blocks.append(Block("section", text = Text("mrkdwn", "*Anomaly Details Link*: " + str(anomalyEvent.anomalyDetailsLink)).__dict__))
        
        
        #Build MS Teams Root Causes
        blocks.append(Block("section", text = Text("mrkdwn", "*Root Causes* :mag:").__dict__))
    
        for rootCause in anomalyEvent.anomalyRootCauses:
            fields = []
            for rootCauseAttribute in rootCause["anomalyRootCauseAttributes"]:
        	    fields.append(Field("plain_text", rootCauseAttribute["rootCauseAttributeName"]  + " : " + rootCauseAttribute["rootCauseAttributeValue"], False).__dict__)
            blocks.append(Block("section", fields=fields))
        	    
        slack_message = [ob.__dict__ for ob in blocks]
        
        return slack_message
    
    def sendMessage(self, slack_message):
        try:
            response = WebhookClient(self.webhook_url).send(text="Anomaly Event Detected", blocks=json.dumps(slack_message))
            print(response.body)
        except SlackAdapterException:
            raise SlackAdapterException
        
    def createNotification(self):

        slack_message = self.constructMessage(self.anomalyEvent)
        
        print(slack_message)
        
        try:
            
            response = self.sendMessage(slack_message)
            
            return response
        except SlackAdapterException:
            raise SlackAdapterException
        
        
        
        
