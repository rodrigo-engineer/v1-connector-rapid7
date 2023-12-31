# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a new endpoint group"


class Input:
    DESCRIPTION = "description"
    ENDPOINTIDS = "endpointIds"
    NAME = "name"
    TYPE = "type"
    

class Output:
    ENDPOINTGROUP = "endpointGroup"
    

class AddEndpointGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Group description",
      "order": 3
    },
    "endpointIds": {
      "type": "array",
      "title": "Endpoint IDs",
      "description": "List of endpoint IDs that will be added to the group",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Endpoint group name",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Group type",
      "default": "computer",
      "enum": [
        "computer",
        "server"
      ],
      "order": 2
    }
  },
  "required": [
    "name",
    "type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddEndpointGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpointGroup": {
      "$ref": "#/definitions/endpointGroup",
      "title": "Endpoint Group",
      "description": "Information about the created endpoint group",
      "order": 1
    }
  },
  "definitions": {
    "endpointGroup": {
      "type": "object",
      "title": "endpointGroup",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "When the group was created",
          "order": 7
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Endpoint group description",
          "order": 3
        },
        "endpoints": {
          "$ref": "#/definitions/endpoints",
          "title": "Endpoints",
          "description": "Associated endpoints",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Endpoint group ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Endpoint group name",
          "order": 2
        },
        "tenant": {
          "$ref": "#/definitions/objectId",
          "title": "Tenant",
          "description": "Reference to a tenant",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Endpoint group type",
          "order": 4
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "When the group was last updated",
          "order": 8
        }
      },
      "definitions": {
        "endpointObject": {
          "type": "object",
          "title": "endpointObject",
          "properties": {
            "hostname": {
              "type": "string",
              "title": "Hostname",
              "description": "Endpoint hostname",
              "order": 2
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique endpoint ID",
              "order": 1
            }
          }
        },
        "endpoints": {
          "type": "object",
          "title": "endpoints",
          "properties": {
            "items": {
              "type": "array",
              "title": "Items",
              "description": "List of endpoints belonging to the group",
              "items": {
                "$ref": "#/definitions/endpointObject"
              },
              "order": 3
            },
            "itemsCount": {
              "type": "integer",
              "title": "Items Count",
              "description": "Total number of items in the list",
              "order": 2
            },
            "total": {
              "type": "integer",
              "title": "Total",
              "description": "Total number of endpoints in this group",
              "order": 1
            }
          },
          "definitions": {
            "endpointObject": {
              "type": "object",
              "title": "endpointObject",
              "properties": {
                "hostname": {
                  "type": "string",
                  "title": "Hostname",
                  "description": "Endpoint hostname",
                  "order": 2
                },
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "Unique endpoint ID",
                  "order": 1
                }
              }
            }
          }
        },
        "objectId": {
          "type": "object",
          "title": "objectId",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The ID of the referenced object",
              "order": 1
            }
          }
        }
      }
    },
    "endpointObject": {
      "type": "object",
      "title": "endpointObject",
      "properties": {
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "description": "Endpoint hostname",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique endpoint ID",
          "order": 1
        }
      }
    },
    "endpoints": {
      "type": "object",
      "title": "endpoints",
      "properties": {
        "items": {
          "type": "array",
          "title": "Items",
          "description": "List of endpoints belonging to the group",
          "items": {
            "$ref": "#/definitions/endpointObject"
          },
          "order": 3
        },
        "itemsCount": {
          "type": "integer",
          "title": "Items Count",
          "description": "Total number of items in the list",
          "order": 2
        },
        "total": {
          "type": "integer",
          "title": "Total",
          "description": "Total number of endpoints in this group",
          "order": 1
        }
      },
      "definitions": {
        "endpointObject": {
          "type": "object",
          "title": "endpointObject",
          "properties": {
            "hostname": {
              "type": "string",
              "title": "Hostname",
              "description": "Endpoint hostname",
              "order": 2
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique endpoint ID",
              "order": 1
            }
          }
        }
      }
    },
    "objectId": {
      "type": "object",
      "title": "objectId",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID of the referenced object",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
