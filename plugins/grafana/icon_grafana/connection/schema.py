# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    BASIC_AUTH = "basic_auth"
    PORT = "port"
    TOKEN_AUTH = "token_auth"
    URL = "url"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "basic_auth": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Basic Authentication",
      "description": "Basic authentication via admin login credentials",
      "order": 3
    },
    "port": {
      "type": "integer",
      "title": "Grafana Port",
      "description": "Grafana Port",
      "default": 3000,
      "order": 2
    },
    "token_auth": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Token Authentication",
      "description": "Token authentication via admin API token",
      "order": 4
    },
    "url": {
      "type": "string",
      "title": "Grafana URL",
      "description": "Grafana URL/Address",
      "order": 1
    }
  },
  "required": [
    "url"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    },
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
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
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
