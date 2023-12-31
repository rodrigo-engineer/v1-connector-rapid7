# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Query for an XML or PDF report for a particular sample"


class Input:
    FORMAT = "format"
    HASH = "hash"
    

class Output:
    REPORT = "report"
    

class GetReportInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "format": {
      "type": "string",
      "title": "Format",
      "description": "Report format: PDF or XML",
      "enum": [
        "pdf",
        "xml"
      ],
      "order": 2
    },
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "The MD5 or SHA-256 hash value of the sample",
      "order": 1
    }
  },
  "required": [
    "format",
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetReportOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report": {
      "type": "string",
      "title": "Report",
      "displayType": "bytes",
      "description": "Report",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "report"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
