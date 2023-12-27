# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to convert an HTML document to DOCX"


class Input:
    DOC = "doc"


class Output:
    DOCX = "docx"


class DocxInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "doc": {
      "type": "string",
      "title": "Document",
      "description": "Document to transform",
      "order": 1
    }
  },
  "required": [
    "doc"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DocxOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "docx": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Docx",
      "description": "Docx File",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)