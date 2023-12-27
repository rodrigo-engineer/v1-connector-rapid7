# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for known malicious antiviruses"


class Input:
    ANTIVIRUS = "antivirus"
    

class Output:
    FOUND = "found"
    HASHES = "hashes"
    PERMALINK = "permalink"
    REFERENCES = "references"
    

class AvInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "antivirus": {
      "type": "string",
      "title": "Antivirus",
      "description": "Antivirus to search",
      "order": 1
    }
  },
  "required": [
    "antivirus"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AvOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether search returned results",
      "order": 4
    },
    "hashes": {
      "type": "array",
      "title": "Hashes",
      "description": "List of hashes",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "permalink": {
      "type": "string",
      "title": "Permalink",
      "description": "Permalink URL",
      "order": 3
    },
    "references": {
      "type": "array",
      "title": "References",
      "description": "List of references",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "found"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
