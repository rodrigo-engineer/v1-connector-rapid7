# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Wipe device by device name, user ID, email address, or device ID if it is not whitelisted"


class Input:
    DEVICE = "device"
    WHITELIST = "whitelist"


class Output:
    SUCCESS = "success"


class WipeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device": {
      "type": "string",
      "title": "Device",
      "description": "Device name, user ID, email address, or device ID",
      "order": 1
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of of device names, user IDs, email addresses, or device IDs that a user can pass in that will not be wiped",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "device"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WipeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Return true if device was successfully wiped",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
