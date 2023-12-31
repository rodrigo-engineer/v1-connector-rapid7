# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of destinations related to a destination list"


class Input:
    DESTINATIONLISTID = "destinationListId"
    

class Output:
    SUCCESS = "success"
    

class DGetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "destinationListId": {
      "type": "integer",
      "title": "Destination List ID",
      "description": "Unique ID for destination list",
      "order": 1
    }
  },
  "required": [
    "destinationListId"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DGetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "array",
      "title": "Success",
      "description": "Successful returned value",
      "items": {
        "$ref": "#/definitions/destinationsEntity"
      },
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "destinationsEntity": {
      "type": "object",
      "title": "destinationsEntity",
      "properties": {
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "Information about domain",
          "order": 4
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Timestamp for creation of entity",
          "format": "date-time",
          "order": 5
        },
        "destination": {
          "type": "string",
          "title": "Destination",
          "description": "Destination can be DOMAIN, URL or IP",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique ID of the destination",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type can be DOMAIN, URL or IPV4",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
