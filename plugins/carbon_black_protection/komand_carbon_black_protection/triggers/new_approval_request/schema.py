# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Triggers when a new approval request is created"


class Input:
    
    POLL_RATE = "poll_rate"
    

class Output:
    
    APPROVAL_REQUEST = "approval_request"
    

class NewApprovalRequestInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "poll_rate": {
      "type": "integer",
      "title": "Poll Rate",
      "description": "How often to poll for new approval requests, in seconds",
      "default": 10,
      "order": 1
    }
  },
  "required": [
    "poll_rate"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NewApprovalRequestOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "approval_request": {
      "$ref": "#/definitions/approvalRequest",
      "title": "Approval Request",
      "description": "The new approval request",
      "order": 1
    }
  },
  "definitions": {
    "approvalRequest": {
      "type": "object",
      "title": "approvalRequest",
      "properties": {
        "computerId": {
          "type": "integer",
          "title": "Computer ID",
          "description": "Id of computer where Request Originated",
          "order": 5
        },
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "description": "Name of computer where Request Originated",
          "order": 6
        },
        "customRuleId": {
          "type": "integer",
          "title": "Custom Rule ID",
          "description": "Id of customRule that Caused File Block",
          "order": 23
        },
        "dateCreated": {
          "type": "string",
          "title": "Date Created",
          "displayType": "date",
          "description": "Datetime when Created (UTC)",
          "format": "date-time",
          "order": 7
        },
        "dateModified": {
          "type": "string",
          "title": "Date Modified",
          "displayType": "date",
          "description": "Datetime when Last Modified (UTC)",
          "format": "date-time",
          "order": 8
        },
        "enforcementLevel": {
          "type": "integer",
          "title": "Enforcement Level",
          "description": "Enforcement Level of Agent",
          "order": 10
        },
        "fileCatalogId": {
          "type": "integer",
          "title": "File Catalog ID",
          "description": "Id of fileCatalog Entry Associated with File",
          "order": 2
        },
        "fileName": {
          "type": "string",
          "title": "File Name",
          "description": "Name of file on Agent",
          "order": 20
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique approvalRequestId",
          "order": 1
        },
        "installerFileCatalogId": {
          "type": "integer",
          "title": "Installer File Catalog ID",
          "description": "Id of fileCatalog Entry Associated with Installer",
          "order": 3
        },
        "modifiedBy": {
          "type": "string",
          "title": "Modified By",
          "description": "User That Last Modified Request",
          "order": 9
        },
        "multipleBlocks": {
          "type": "boolean",
          "title": "Multiple Blocks",
          "description": "True if File Referenced Had Multiple Blocks",
          "order": 19
        },
        "pathName": {
          "type": "string",
          "title": "Path Name",
          "description": "Path of file on Agent",
          "order": 21
        },
        "policyId": {
          "type": "integer",
          "title": "Policy ID",
          "description": "Id of policy for Computer When Request Arrived",
          "order": 18
        },
        "priority": {
          "type": "integer",
          "title": "Priority",
          "description": "Priority of Request",
          "order": 15
        },
        "process": {
          "type": "string",
          "title": "Process",
          "description": "Process that Attempted to Execute file on Agent",
          "order": 22
        },
        "processFileCatalogId": {
          "type": "integer",
          "title": "Process File Catalog ID",
          "description": "Id of fileCatalog Entry Associated with Process",
          "order": 4
        },
        "requestType": {
          "type": "integer",
          "title": "Request Type",
          "description": "Type of Request",
          "order": 12
        },
        "requestorComments": {
          "type": "string",
          "title": "Requestor Comments",
          "description": "Comments by User that Created Request",
          "order": 13
        },
        "requestorEmail": {
          "type": "string",
          "title": "Requestor Email",
          "description": "Email of User that Created Request",
          "order": 14
        },
        "resolution": {
          "type": "integer",
          "title": "Resolution",
          "description": "Resolution of Request",
          "order": 11
        },
        "resolutionComments": {
          "type": "string",
          "title": "Resolution Comments",
          "description": "Comments by Request Resolver",
          "order": 16
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Request Status",
          "order": 17
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
