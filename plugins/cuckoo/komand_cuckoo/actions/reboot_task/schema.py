# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add a reboot task to database from an existing analysis ID"


class Input:
    TASK_ID = "task_id"
    

class Output:
    REBOOT_ID = "reboot_id"
    TASK_ID = "task_id"
    

class RebootTaskInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "task_id": {
      "type": "integer",
      "title": "Task ID",
      "description": "Task ID",
      "order": 1
    }
  },
  "required": [
    "task_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RebootTaskOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reboot_id": {
      "type": "integer",
      "title": "Reboot ID",
      "description": "Reboot ID",
      "order": 2
    },
    "task_id": {
      "type": "integer",
      "title": "Task ID",
      "description": "Task ID",
      "order": 1
    }
  },
  "required": [
    "reboot_id",
    "task_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
