# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Download IOC packs, PCAP files, memory dumps, and other analysis artifacts"


class Input:
    ID = "id"
    

class Output:
    ARTIFACTS = "artifacts"
    

class DownloadArtifactInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "ID of an JSON artifact, such as an IOC pack, PCAP file, memory dump, or actor image. Find an artifact ID with `Get Full Report` action",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadArtifactOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "artifacts": {
      "type": "array",
      "title": "Artifacts",
      "description": "List of artifacts",
      "items": {
        "$ref": "#/definitions/artifact"
      },
      "order": 1
    }
  },
  "required": [
    "artifacts"
  ],
  "definitions": {
    "artifact": {
      "type": "object",
      "title": "artifact",
      "properties": {
        "ioc": {
          "type": "string",
          "title": "IOC",
          "description": "IOC",
          "order": 3
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
