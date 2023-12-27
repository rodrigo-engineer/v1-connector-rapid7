# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add a user to a group"


class Input:
    GROUP_ID = "group_id"
    ROLE = "role"
    USER_ID = "user_id"
    

class Output:
    GROUP = "group"
    

class AddUserToGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_id": {
      "type": "string",
      "title": "Group ID",
      "description": "Group ID e.g. 12345678",
      "order": 2
    },
    "role": {
      "type": "string",
      "title": "Role",
      "description": "Role",
      "enum": [
        "admin",
        "member"
      ],
      "order": 3
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID e.g. 12345678",
      "order": 1
    }
  },
  "required": [
    "group_id",
    "role",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddUserToGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group": {
      "type": "object",
      "title": "Group",
      "description": "Group",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
