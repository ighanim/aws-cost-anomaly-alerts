import json
from event_construction import EventConstructor
from app_configurations import AppConfigurator
from notification_router import NotificationRouter
import boto3
import base64
from botocore.exceptions import ClientError
import os

    
def lambda_handler(event, context):
    
    snsEventMessage = json.loads(event["Records"][0]["Sns"]["Message"])

    ##Read AppConfig Configurations file including Feature Flags as well as Routing Notifications. 
    ob_app_configurator = AppConfigurator()
    ob_app_configurator.get_app_configurations()
    
    ## Call EventConstructor to build the generic notification structure that is sent across different distribution channels. 
    anomalyEvent = EventConstructor(snsEventMessage).construct_event(ob_app_configurator)
    
    ## Call NotificationRouter that is responsible to distribute the notification to different channels. 
    ob_router = NotificationRouter(ob_app_configurator)
    ob_router.dispatch_notifications(anomalyEvent)
    

    return {
        'statusCode': 200
    }
