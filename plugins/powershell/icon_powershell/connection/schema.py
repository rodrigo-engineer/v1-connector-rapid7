# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    AUTH = "auth"
    CREDENTIALS = "credentials"
    KERBEROS = "kerberos"
    PORT = "port"
    SCRIPT_SECRET_KEY = "script_secret_key"
    SCRIPT_USERNAME_AND_PASSWORD = "script_username_and_password"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "auth": {
      "type": "string",
      "title": "Auth Type",
      "description": "Authentication type",
      "default": "None",
      "enum": [
        "NTLM",
        "Kerberos",
        "CredSSP",
        "None"
      ],
      "order": 3
    },
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 1
    },
    "kerberos": {
      "$ref": "#/definitions/kerberos",
      "title": "Kerberos",
      "description": "Connection information required for Kerberos",
      "order": 4
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port number, defaults are 5986 for SSL and 5985 for unencrypted",
      "default": 5986,
      "order": 2
    },
    "script_secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Script Secret Key",
      "description": "Credential secret key available in script as powershell variable (`$secret_key`)",
      "order": 5
    },
    "script_username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Script Username and Password",
      "description": "Username and password available in script as powershell variables (`$username`, `$password`)",
      "order": 6
    }
  },
  "required": [
    "auth"
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
    },
    "kerberos": {
      "type": "object",
      "title": "kerberos",
      "properties": {
        "domain_name": {
          "type": "string",
          "title": "Domain Name",
          "description": "The fully qualified domain name of the remote host e.g. example.com. If Auth Type is set to None then leave this blank",
          "order": 2
        },
        "kdc": {
          "type": "string",
          "title": "KDC",
          "description": "IP address of the Active Directory server. If Auth Type is set to None then leave this blank",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
