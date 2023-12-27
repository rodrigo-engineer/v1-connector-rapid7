# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Look for potential typo squatters"


class Input:
    DOMAIN = "domain"
    FLAG = "flag"
    

class Output:
    POTENTIAL_SQUATTERS = "potential_squatters"
    

class CheckForSquattersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain to check",
      "default": "example.com",
      "order": 1
    },
    "flag": {
      "type": "string",
      "title": "Flag",
      "description": "Flag to pass for dnstwist (Advanced)",
      "order": 2
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckForSquattersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "potential_squatters": {
      "type": "array",
      "title": "Potential Squatters",
      "description": "JSON representation of potential squatters",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)