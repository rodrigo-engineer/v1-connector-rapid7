# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Generate a shared secret to pair a scan engine to a security console"


class Input:
    TIME_TO_LIVE = "time_to_live"
    

class Output:
    SHARED_SECRET = "shared_secret"
    

class GenerateSharedSecretInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "time_to_live": {
      "type": "integer",
      "title": "Time to Live",
      "description": "Time to live in seconds for the shared secret",
      "default": 3600,
      "order": 1
    }
  },
  "required": [
    "time_to_live"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GenerateSharedSecretOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "shared_secret": {
      "type": "string",
      "title": "Shared Secret",
      "description": "Scan engine pairing shared secret",
      "order": 1
    }
  },
  "required": [
    "shared_secret"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)