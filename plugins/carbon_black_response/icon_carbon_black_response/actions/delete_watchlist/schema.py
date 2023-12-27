# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Deletes a watchlist"


class Input:
    FORCE = "force"
    ID = "id"
    

class Output:
    SUCCESS = "success"
    

class DeleteWatchlistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "force": {
      "type": "boolean",
      "title": "Force",
      "description": "Force deletion of all matches if multiple matches found",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The ID of the watchlist",
      "order": 1
    }
  },
  "required": [
    "force",
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteWatchlistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the deletion was successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
