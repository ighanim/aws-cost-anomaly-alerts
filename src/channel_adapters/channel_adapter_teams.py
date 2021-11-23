import json
from teams.models import fact, factSet, textBlock
from teams.webhook import WebhookClient

class TeamsNotification:
    def __init__(self, anomalyEvent, webhook_url):
        self.anomalyEvent = anomalyEvent
        self.webhook_url = webhook_url
    def constructMessage(self, anomalyEvent):
        
        print(json.dumps(self.anomalyEvent.__dict__))
        
        anomalyEvent = self.anomalyEvent
        
        #Initialise the Adaptive Message body. This is the container of the message to be rendered on the Adaptive Card on Teams. 
        body = []
        #Notification Header
        body.append(textBlock('Cost Anomaly Detected', False, 'Bolder'))
        
        #Notification Top Elements
        factList = []
        factList.append(fact('Total Anomaly Cost', str(anomalyEvent.anomalyTotalImpact)).__dict__)
        factList.append(fact('Anomaly Start Date', str(anomalyEvent.anomalyStartDate)).__dict__)
        factList.append(fact('Anomaly Start Date', str(anomalyEvent.anomalyEndDate)).__dict__)
        factList.append(fact('Anomaly Details Link', str(anomalyEvent.anomalyDetailsLink)).__dict__)
        
        #Append the body with the top level elements encapsulated in a factSet. 
        body.append(factSet(factList))
        
        
        #print(json.dumps([ob.__dict__ for ob in facts]))
        #print(myFactSet.__dict__)
        
        #Build MS Teams Root Causes
        body.append(textBlock('Root Causes', True, 'Bolder'))
    
        for rootCause in anomalyEvent.anomalyRootCauses:
            factList = []
            for rootCauseAttribute in rootCause["anomalyRootCauseAttributes"]:
        	    factList.append(fact(rootCauseAttribute["rootCauseAttributeName"]  + " : ",rootCauseAttribute["rootCauseAttributeValue"]).__dict__)
            body.append(factSet(factList))
        	    
        teams_message = {
            'type': 'message',
            'attachments': [ 
                {
                    'contentType': 'application/vnd.microsoft.card.adaptive',
                    'content': {
                        'type': 'AdaptiveCard',
                        'body': [ob.__dict__ for ob in body],
                        '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                        'version': '1.3'
                    }
                            }
                        ]
                    }
        
        return teams_message
    def sendMessage(self, teams_message):
        try:
            WebhookClient(teams_message, self.webhook_url).sendMessage()
        except Exception:
            raise Exception
        
        
    def createNotification(self):

        teams_message = self.constructMessage(self.anomalyEvent)
        
        try:
            response = self.sendMessage(teams_message)
            return response
        except Exception:
            raise Exception
        
        
        
        
