# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Save an image of a virtual machine (VM must be stopped, generalized, and be an unmanaged disk)"


class Input:
    DESTINATIONCONTAINERNAME = "destinationContainerName"
    OVERWRITEVHDS = "overwriteVhds"
    RESOURCEGROUP = "resourceGroup"
    SUBSCRIPTIONID = "subscriptionId"
    VHDPREFIX = "vhdPrefix"
    VM = "vm"
    

class Output:
    STATUS_CODE = "status_code"
    

class SaveImageVmInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "destinationContainerName": {
      "type": "string",
      "title": "Destination Container Name",
      "description": "Specifies the name of the container inside which the vhds constituting the image resides",
      "order": 5
    },
    "overwriteVhds": {
      "type": "boolean",
      "title": "VHDPrefix",
      "description": "Specifies if an existing vhd with same prefix inside the destination container is overwritten",
      "default": true,
      "order": 6
    },
    "resourceGroup": {
      "type": "string",
      "title": "Resource Group",
      "description": "The resource group that will contain the virtual machine",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "The identifier of your subscription",
      "order": 1
    },
    "vhdPrefix": {
      "type": "string",
      "title": "VHDPrefix",
      "description": "Specifies the prefix in the name of the blobs that constitute the storage profile of the image",
      "order": 4
    },
    "vm": {
      "type": "string",
      "title": "Name of Virtual Machine",
      "description": "The name of the virtual machine",
      "order": 3
    }
  },
  "required": [
    "destinationContainerName",
    "overwriteVhds",
    "resourceGroup",
    "subscriptionId",
    "vhdPrefix",
    "vm"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SaveImageVmOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status_code": {
      "type": "integer",
      "title": "Status",
      "description": "HTTP status code",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
