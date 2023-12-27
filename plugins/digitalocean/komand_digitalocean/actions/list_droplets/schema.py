# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lists all droplets on the account"


class Input:
    pass

class Output:
    DROPLETS = "droplets"
    

class ListDropletsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListDropletsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "droplets": {
      "type": "array",
      "title": "Droplets",
      "description": "All droplets on the account",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)