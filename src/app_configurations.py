import json
import base64
from botocore.exceptions import ClientError
import urllib.request

class AppConfigurator:
    def __init__(self):
        self.feature_flags = ""
        self.routing_configurations = ""
    
    def get_app_configurations(self):
        ##The function reads the application configurations stored in AppConfig configuration file. AppConfig is integrated as a Layer in the solution. 
        appconfig_url = f'http://localhost:2772/applications/cost-anomaly-alerts-app/environments/cost-anomaly-alerts-env/configurations/cost-anomaly-to-slack-configurations'
        appconfig_configurations = urllib.request.urlopen(appconfig_url).read()
        config_json = json.loads(appconfig_configurations)
        
        #Feature Flags Includes features such as displayAccountName
        self.feature_flags = config_json["feature-flags"]
        
        #Routing_Configurations defines the rules based on which the notification will be routed
        self.routing_configurations = config_json["routing-configurations"]
        
        
        
        
    