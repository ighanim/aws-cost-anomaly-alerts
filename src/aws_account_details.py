import json
import boto3
import base64

class AwsAccountDetails:
    def __init__(self, account_id):
        self.account_id = account_id
        
    def get_aws_account_name(self):
        #Function is used to fetch account name corresponding to an account number. The account name is used to display a meaningful name in the Slack notification. For this function to operate, proper IAM permission should be granted to the Lambda function role.
        print("Fetching Account Name corresponding to accountId:" + self.account_id)
    
        #Initialise Organisations
        client = boto3.client('organizations')
    
        #Call describe_account in order to return the account_id corresponding to the account_number. 
        response = client.describe_account(AccountId=self.account_id)
        
        accountName = response["Account"]["Name"]
        print("Fetching Account Name complete. Account Name:" + accountName)
        
        #Return the Account Name corresponding the Input Account ID.
        return response["Account"]["Name"]
