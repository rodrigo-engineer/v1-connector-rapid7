# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Close an existing alert from Opsgenie"


class Input:
    IDENTIFIER = "identifier"
    IDENTIFIERTYPE = "identifierType"
    NOTE = "note"
    SOURCE = "source"
    USER = "user"
    

class Output:
    ELAPSED_TIME = "elapsed_time"
    REQUESTID = "requestId"
    RESULT = "result"
    

class CloseAlertInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "identifier": {
      "type": "string",
      "title": "Alert ID, Tiny ID or Alias",
      "description": "Identifier of the alert",
      "order": 1
    },
    "identifierType": {
      "type": "string",
      "title": "Identifier Type",
      "description": "Type of the identifier that is provided as an in-line parameter. Possible values are ID, tiny ID and alias. Default value is ID",
      "default": "ID",
      "enum": [
        "",
        "ID",
        "tiny",
        "alias"
      ],
      "order": 2
    },
    "note": {
      "type": "string",
      "title": "Note",
      "description": "Additional alert note to add",
      "order": 5
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Display name of the request source",
      "order": 4
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "Display name of the request owner",
      "order": 3
    }
  },
  "required": [
    "identifier"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CloseAlertOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "elapsed_time": {
      "type": "number",
      "title": "Elapsed Time",
      "description": "Time taken to execute",
      "order": 2
    },
    "requestId": {
      "type": "string",
      "title": "Request ID",
      "description": "ID of a executed API request",
      "order": 3
    },
    "result": {
      "type": "string",
      "title": "Result",
      "description": "Result message from API",
      "order": 1
    }
  },
  "required": [
    "elapsed_time",
    "requestId",
    "result"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
