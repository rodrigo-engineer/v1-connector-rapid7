# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    APP_ID = "app_id"
    APP_SECRET = "app_secret"
    TENANT_ID = "tenant_id"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "The ID of the registered app that obtained the refresh token",
      "order": 2
    },
    "app_secret": {
      "$ref": "#/definitions/credential_token",
      "title": "App Secret",
      "description": "The secret of the registered app that obtained the refresh token",
      "order": 3
    },
    "tenant_id": {
      "type": "string",
      "title": "Tenant ID",
      "description": "The ID of the directory that identifies the tenant",
      "order": 1
    }
  },
  "required": [
    "app_id",
    "app_secret",
    "tenant_id"
  ],
  "definitions": {
    "credential_token": {
      "id": "credential_token",
      "type": "object",
      "title": "Credential: Token",
      "description": "A pair of a token, and an optional domain",
      "properties": {
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The domain for the token"
        },
        "token": {
          "type": "string",
          "title": "Token",
          "displayType": "password",
          "description": "The shared token",
          "format": "password"
        }
      },
      "required": [
        "token"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
