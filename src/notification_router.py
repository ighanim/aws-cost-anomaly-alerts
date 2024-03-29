# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json
import boto3
import base64
from botocore.exceptions import ClientError
import os
import urllib.request
from channel_adapters import TeamsNotification
from channel_adapters import SlackNotification
from models import AnomalyEvent, AnomalyRootCause, AnomalyRootCauseAttribute, TargetChannel

#NotificationRouter calculates and returns notification routes from AppConfig configurations. A route is a combination of a channel and a URL. 
class NotificationRouter:
    def __init__(self, app_configurations):
        self.app_configurations = app_configurations
                
    #Not used so far. At the moment, the URL is stored in AppConfig
    def get_secret(secret_name):
    
        region_name = os.environ['AWS_REGION']
    
        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
    
        # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
        # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        # We rethrow the exception by default.
    
        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                # An error occurred on the server side.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
        else:
            # Decrypts secret using the associated KMS CMK.
            # Depending on whether the secret is a string or binary, one of these fields will be populated.
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                return secret
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                
    def load_routing_configurations(self):
        
        routing_configurations = self.app_configurations.routing_configurations
        
        notification_routes = []
        
        for notification_route in routing_configurations[0]["target-channels"]:
            notification_routes.append(TargetChannel(notification_route["type"], notification_route["URL"]))
        
        return notification_routes
        
    def dispatch_notifications(self,anomalyEvent):
        notification_routes = self.load_routing_configurations()
        
        for notification_route in notification_routes:
            url = notification_route.channel_url
            if notification_route.channel_type == "Slack":
                response = SlackNotification(anomalyEvent, url).createNotification()
                print(json.dumps(response))
                print("Slack Webhook: " + url)
            elif notification_route.channel_type == "MS_Teams":
                response =  TeamsNotification(anomalyEvent, url).createNotification()
                print("Teams Webook: " + url)