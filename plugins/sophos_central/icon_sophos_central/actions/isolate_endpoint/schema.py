# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Turn on or off endpoint isolation for multiple endpoints"


class Input:
    COMMENT = "comment"
    ENABLED = "enabled"
    IDS = "ids"
    

class Output:
    ENDPOINTS = "endpoints"
    

class IsolateEndpointInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Reason the endpoints should be isolated or not",
      "order": 3
    },
    "enabled": {
      "type": "boolean",
      "title": "Enabled",
      "description": "Whether the endpoints should be isolated or not",
      "default": true,
      "order": 1
    },
    "ids": {
      "type": "array",
      "title": "IDs",
      "description": "List of endpoints IDs",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "enabled",
    "ids"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IsolateEndpointOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoints": {
      "type": "array",
      "title": "Endpoints",
      "description": "List of endpoints for which isolation has been updated",
      "items": {
        "$ref": "#/definitions/endpointIsolation"
      },
      "order": 1
    }
  },
  "definitions": {
    "endpointIsolation": {
      "type": "object",
      "title": "endpointIsolation",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Endpoint ID",
          "order": 1
        },
        "isolation": {
          "$ref": "#/definitions/isolation",
          "title": "Isolation",
          "description": "Isolation state of an endpoint",
          "order": 2
        }
      },
      "definitions": {
        "isolation": {
          "type": "object",
          "title": "isolation",
          "properties": {
            "comment": {
              "type": "string",
              "title": "Comment",
              "description": "Reason endpoint should be isolated or not",
              "order": 6
            },
            "enabled": {
              "type": "boolean",
              "title": "Enabled",
              "description": "Whether the endpoint should be isolated or not",
              "order": 1
            },
            "lastDisabledAt": {
              "type": "string",
              "title": "Last Disabled At",
              "description": "When isolation was last disabled for the endpoint",
              "order": 4
            },
            "lastDisabledBy": {
              "$ref": "#/definitions/user",
              "title": "Last Disabled By",
              "description": "Last disabled by",
              "order": 5
            },
            "lastEnabledAt": {
              "type": "string",
              "title": "Last Enabled At",
              "description": "When isolation was last enabled for the endpoint",
              "order": 2
            },
            "lastEnabledBy": {
              "$ref": "#/definitions/user",
              "title": "Last Enabled By",
              "description": "Last enabled by",
              "order": 3
            }
          },
          "definitions": {
            "user": {
              "type": "object",
              "title": "user",
              "properties": {
                "accountId": {
                  "type": "string",
                  "title": "Account ID",
                  "description": "ID of the account",
                  "order": 5
                },
                "accountType": {
                  "type": "string",
                  "title": "Account Type",
                  "description": "Type of the account",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "Principal email or client ID",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "User principal name",
                  "order": 3
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Principal type",
                  "order": 2
                }
              }
            }
          }
        },
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "accountId": {
              "type": "string",
              "title": "Account ID",
              "description": "ID of the account",
              "order": 5
            },
            "accountType": {
              "type": "string",
              "title": "Account Type",
              "description": "Type of the account",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Principal email or client ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "User principal name",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Principal type",
              "order": 2
            }
          }
        }
      }
    },
    "isolation": {
      "type": "object",
      "title": "isolation",
      "properties": {
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "Reason endpoint should be isolated or not",
          "order": 6
        },
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "description": "Whether the endpoint should be isolated or not",
          "order": 1
        },
        "lastDisabledAt": {
          "type": "string",
          "title": "Last Disabled At",
          "description": "When isolation was last disabled for the endpoint",
          "order": 4
        },
        "lastDisabledBy": {
          "$ref": "#/definitions/user",
          "title": "Last Disabled By",
          "description": "Last disabled by",
          "order": 5
        },
        "lastEnabledAt": {
          "type": "string",
          "title": "Last Enabled At",
          "description": "When isolation was last enabled for the endpoint",
          "order": 2
        },
        "lastEnabledBy": {
          "$ref": "#/definitions/user",
          "title": "Last Enabled By",
          "description": "Last enabled by",
          "order": 3
        }
      },
      "definitions": {
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "accountId": {
              "type": "string",
              "title": "Account ID",
              "description": "ID of the account",
              "order": 5
            },
            "accountType": {
              "type": "string",
              "title": "Account Type",
              "description": "Type of the account",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Principal email or client ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "User principal name",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Principal type",
              "order": 2
            }
          }
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "accountId": {
          "type": "string",
          "title": "Account ID",
          "description": "ID of the account",
          "order": 5
        },
        "accountType": {
          "type": "string",
          "title": "Account Type",
          "description": "Type of the account",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Principal email or client ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User principal name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Principal type",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
