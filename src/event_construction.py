# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json
import boto3
import base64
from app_configurations import AppConfigurator
from aws_account_details import AwsAccountDetails
from models import AnomalyEvent, AnomalyRootCause, AnomalyRootCauseAttribute

class EventConstructor:
    def __init__(self, event):
        self.event = event
        
    def construct_event(self, app_configurations):
        ##Load Features. This will configurations from the AppConfig file that is required to construct the Anomaly Event. 
        feature_flags = app_configurations.feature_flags
        
        feature_flag_displayAccountName = feature_flags["displayAccountName"]
        
        event = self.event
        
        ##Prepare Event Header Data
        anomalyStartDate = event["anomalyStartDate"]
        anomalyEndDate = event["anomalyEndDate"]
        anomalyTotalImpact = event["impact"]["totalImpact"]
        anomalyDetailsLink = event["anomalyDetailsLink"]
        
        #Construst Anomaly Event Root Causes Objects. 
        rootCauseAttributeList = []
        rootCauseList = []
        
        for rootCause in event["rootCauses"]:
            rootCauseAttributeList = []
            for rootCauseAttribute in rootCause:
        	    if feature_flag_displayAccountName == True:
        	        if rootCauseAttribute == "linkedAccount":
        	            accountName = AwsAccountDetails(rootCause[rootCauseAttribute]).get_aws_account_name()
        	            rootCauseAttributeList.append(AnomalyRootCauseAttribute("accountName", accountName).__dict__)
        	    rootCauseAttributeList.append(AnomalyRootCauseAttribute(rootCauseAttribute,rootCause[rootCauseAttribute]).__dict__)
            rootCauseList.append(AnomalyRootCause(rootCauseAttributeList))
        
        ob_anomaly_event = AnomalyEvent(anomalyStartDate, anomalyEndDate, anomalyTotalImpact, anomalyDetailsLink, [ob.__dict__ for ob in rootCauseList])
        
        return ob_anomaly_event
        
