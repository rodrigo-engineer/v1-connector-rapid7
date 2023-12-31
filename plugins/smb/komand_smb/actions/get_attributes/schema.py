# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get attributes"


class Input:
    FILE_PATH = "file_path"
    SHARE_NAME = "share_name"
    TIMEOUT = "timeout"
    TIMEZONE = "timezone"
    

class Output:
    ATTRIBUTES = "attributes"
    

class GetAttributesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_path": {
      "type": "string",
      "title": "File Path",
      "description": "Path relative to share to get file attributes",
      "order": 2
    },
    "share_name": {
      "type": "string",
      "title": "Share Name",
      "description": "Name of the SMB share",
      "order": 1
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Request timeout of operation in seconds",
      "default": 30,
      "order": 4
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "description": "Timezone to be applied to datetime fields (eg. UTC, US/Eastern, US/Pacific, Europe/London). Reference https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names",
      "default": "UTC",
      "order": 3
    }
  },
  "required": [
    "file_path",
    "share_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAttributesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attributes": {
      "$ref": "#/definitions/file",
      "title": "Attributes",
      "description": "File attributes",
      "order": 1
    }
  },
  "required": [
    "attributes"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
