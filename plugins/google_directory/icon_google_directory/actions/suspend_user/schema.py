# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Suspends a user account"


class Input:
    EMAIL = "email"
    

class Output:
    SUCCESS = "success"
    

class SuspendUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "User Email",
      "description": "Email of user to suspend",
      "order": 1
    }
  },
  "required": [
    "email"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SuspendUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the suspend was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
