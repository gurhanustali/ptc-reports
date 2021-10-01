from espo_api_client import EspoAPI
import pandas as pd 
import numpy as np

client = EspoAPI('http://localhost/mandant', '35b65f45010fb5d74c6be93a88d78fea')


"""
# Create a lead

data = {
    'firstName': 'John',
    'lastName': 'Does',
    'phoneNumber': '+11111-22222-33333',
    'source': 'Web Site',
    'assignedUserId': '1',
    'industry': 'Legal',
}
print(client.request('POST', 'Lead', data))

# Update
print(client.request('PUT', 'Lead/5b3c37b74b19680f1', {'lastName': 'Alice'}))

# Get accounts
print(client.request('GET', 'Account'))
"""


# Get accounts with search params
params = {
    "select": "id,dMinute",
    "where": [
        {
            "type": "equals",
            "attribute": "serviceNo",
            "value": '6',
        },
    ],
}


services=client.request('GET', 'Service', params)["list"]
df=pd.DataFrame(services)
df['duration']=df['dMinute']/60
del df['dMinute']
print(df.groupby("serviceProvider").aggregate(['sum','mean']))


"""
# Delete an opportunity
print(client.request('DELETE', 'Opportunity/5b3b0b8c0b2b8bea5'))
"""