# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Change the organization for which all future API requests will be made"


class Input:
    ORGANIZATIONNAME = "organizationName"
    

class Output:
    SUCCESS = "success"
    

class SwitchOrganizationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organizationName": {
      "type": "string",
      "title": "Organization Name",
      "description": "Name of the organization",
      "order": 1
    }
  },
  "required": [
    "organizationName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SwitchOrganizationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
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
