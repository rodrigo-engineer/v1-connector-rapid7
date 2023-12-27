# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a blank Google document"


class Input:
    TITLE = "title"
    

class Output:
    DOCUMENT = "document"
    

class CreateBlankDocumentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Document Title",
      "order": 1
    }
  },
  "required": [
    "title"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateBlankDocumentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "document": {
      "$ref": "#/definitions/document",
      "title": "Document",
      "description": "Created Document",
      "order": 1
    }
  },
  "required": [
    "document"
  ],
  "definitions": {
    "document": {
      "type": "object",
      "title": "document",
      "properties": {
        "body": {
          "type": "object",
          "title": "Body",
          "description": "Body",
          "order": 1
        },
        "documentId": {
          "type": "string",
          "title": "Document ID",
          "description": "Document ID",
          "order": 5
        },
        "documentStyle": {
          "type": "object",
          "title": "Document Style",
          "description": "Document Style",
          "order": 2
        },
        "namedStyles": {
          "type": "object",
          "title": "Named Styles",
          "description": "Named styles",
          "order": 7
        },
        "revisionId": {
          "type": "string",
          "title": "Revision ID",
          "description": "Revision ID",
          "order": 4
        },
        "suggestionsViewMode": {
          "type": "string",
          "title": "Suggestions View Mode",
          "description": "Suggestions view mode",
          "order": 6
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
