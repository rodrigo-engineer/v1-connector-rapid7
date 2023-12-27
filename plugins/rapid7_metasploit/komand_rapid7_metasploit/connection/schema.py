# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    PORT = "port"
    SERVER = "server"
    SSL = "ssl"
    URI = "uri"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Username and password",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port",
      "default": 55553,
      "order": 3
    },
    "server": {
      "type": "string",
      "title": "Server",
      "description": "Remote server IP",
      "order": 4
    },
    "ssl": {
      "type": "boolean",
      "title": "SSL",
      "description": "Use SSL",
      "default": true,
      "order": 5
    },
    "uri": {
      "type": "string",
      "title": "URI",
      "description": "The msfrpcd URI",
      "default": "/api/",
      "order": 2
    }
  },
  "required": [
    "credentials"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)