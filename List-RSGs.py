# Import the needed credential and management objects from the libraries.
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
import os

rg_names = ["rg-python1", "rg-python2"]

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

groups = resource_client.resource_groups.list()

for group in groups:

    if group.name.startswith("rg-"):
       print(f" Resource Group Name: {group.name}")
       print(f" Location: {group.location}\n")
    elif group.location == "centralus":
        print(f" Name is {group.name} and Location is {group.location}\n")
