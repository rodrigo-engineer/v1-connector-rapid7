# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    APIKEY = "apiKey"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "apiKey": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "IPQS KEY",
      "description": "IPQualityScore API Key",
      "order": 1
    }
  },
  "required": [
    "apiKey"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "required": [
        "secretKey"
      ],
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "description": "The shared secret key",
          "format": "password",
          "displayType": "password"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
