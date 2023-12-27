# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Process file with Awk"


class Input:
    DATA = "data"
    EXPRESSION = "expression"
    

class Output:
    OUT = "out"
    

class ProcessFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "title": "Data",
      "displayType": "bytes",
      "description": "File to process",
      "format": "bytes",
      "order": 2
    },
    "expression": {
      "type": "string",
      "title": "Expression",
      "description": "Awk expression e.g. [pattern] { action }",
      "order": 1
    }
  },
  "required": [
    "data",
    "expression"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ProcessFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "out": {
      "type": "string",
      "title": "Out",
      "description": "Processed string",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)