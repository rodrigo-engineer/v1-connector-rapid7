# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get all domain users"


class Input:
    DOMAIN = "domain"
    

class Output:
    USERS = "users"
    

class GetAllDomainUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain to retrieve users from",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAllDomainUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "Users",
      "description": "Users in the domain",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 1
    }
  },
  "required": [
    "users"
  ],
  "definitions": {
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email address",
          "order": 1
        },
        "full_name": {
          "type": "string",
          "title": "Full Name",
          "description": "Full name of the user",
          "order": 2
        }
      },
      "required": [
        "email"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
