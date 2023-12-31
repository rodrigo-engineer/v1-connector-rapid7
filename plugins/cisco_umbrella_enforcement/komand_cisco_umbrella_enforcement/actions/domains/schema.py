# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Gather the lists of domains already added to the shared customer's domain list"


class Input:
    pass

class Output:
    DOMAINS = "domains"
    

class DomainsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domains": {
      "$ref": "#/definitions/domains",
      "title": "Domain List Query Results",
      "description": "Array containing domains in the domain list",
      "order": 1
    }
  },
  "definitions": {
    "data": {
      "type": "object",
      "title": "data",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Id",
          "description": "Unique ID number",
          "order": 2
        },
        "lastSeenAt": {
          "type": "integer",
          "title": "Last seen malware",
          "description": "Unix timestamp last seen",
          "order": 3
        },
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Meta",
          "description": "meta data",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Domain name",
          "order": 1
        }
      },
      "required": [
        "id",
        "lastSeenAt",
        "name"
      ],
      "definitions": {
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "limit": {
              "type": "integer",
              "title": "Limit",
              "description": "The number of results",
              "order": 2
            },
            "next": {
              "type": "boolean",
              "title": "Next",
              "description": "If next is false, this is the last available page of results. Otherwise, it will provide a query formatted to show the next set of results",
              "order": 4
            },
            "page": {
              "type": "integer",
              "title": "Page",
              "description": "The page of results is available",
              "order": 1
            },
            "prev": {
              "type": "boolean",
              "title": "Prev",
              "description": "If prev is false, this is the first available page of results. Otherwise, it will provide a query formatted to show the next set of results",
              "order": 3
            }
          },
          "required": [
            "limit",
            "next",
            "page",
            "prev"
          ]
        }
      }
    },
    "domains": {
      "type": "object",
      "title": "domains",
      "properties": {
        "data": {
          "type": "array",
          "title": "Data",
          "description": "List of domains",
          "items": {
            "$ref": "#/definitions/data"
          },
          "order": 2
        },
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Meta",
          "description": "Meta Data",
          "order": 1
        }
      },
      "required": [
        "data",
        "meta"
      ],
      "definitions": {
        "data": {
          "type": "object",
          "title": "data",
          "properties": {
            "id": {
              "type": "integer",
              "title": "Id",
              "description": "Unique ID number",
              "order": 2
            },
            "lastSeenAt": {
              "type": "integer",
              "title": "Last seen malware",
              "description": "Unix timestamp last seen",
              "order": 3
            },
            "meta": {
              "$ref": "#/definitions/meta",
              "title": "Meta",
              "description": "meta data",
              "order": 4
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Domain name",
              "order": 1
            }
          },
          "required": [
            "id",
            "lastSeenAt",
            "name"
          ],
          "definitions": {
            "meta": {
              "type": "object",
              "title": "meta",
              "properties": {
                "limit": {
                  "type": "integer",
                  "title": "Limit",
                  "description": "The number of results",
                  "order": 2
                },
                "next": {
                  "type": "boolean",
                  "title": "Next",
                  "description": "If next is false, this is the last available page of results. Otherwise, it will provide a query formatted to show the next set of results",
                  "order": 4
                },
                "page": {
                  "type": "integer",
                  "title": "Page",
                  "description": "The page of results is available",
                  "order": 1
                },
                "prev": {
                  "type": "boolean",
                  "title": "Prev",
                  "description": "If prev is false, this is the first available page of results. Otherwise, it will provide a query formatted to show the next set of results",
                  "order": 3
                }
              },
              "required": [
                "limit",
                "next",
                "page",
                "prev"
              ]
            }
          }
        },
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "limit": {
              "type": "integer",
              "title": "Limit",
              "description": "The number of results",
              "order": 2
            },
            "next": {
              "type": "boolean",
              "title": "Next",
              "description": "If next is false, this is the last available page of results. Otherwise, it will provide a query formatted to show the next set of results",
              "order": 4
            },
            "page": {
              "type": "integer",
              "title": "Page",
              "description": "The page of results is available",
              "order": 1
            },
            "prev": {
              "type": "boolean",
              "title": "Prev",
              "description": "If prev is false, this is the first available page of results. Otherwise, it will provide a query formatted to show the next set of results",
              "order": 3
            }
          },
          "required": [
            "limit",
            "next",
            "page",
            "prev"
          ]
        }
      }
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "limit": {
          "type": "integer",
          "title": "Limit",
          "description": "The number of results",
          "order": 2
        },
        "next": {
          "type": "boolean",
          "title": "Next",
          "description": "If next is false, this is the last available page of results. Otherwise, it will provide a query formatted to show the next set of results",
          "order": 4
        },
        "page": {
          "type": "integer",
          "title": "Page",
          "description": "The page of results is available",
          "order": 1
        },
        "prev": {
          "type": "boolean",
          "title": "Prev",
          "description": "If prev is false, this is the first available page of results. Otherwise, it will provide a query formatted to show the next set of results",
          "order": 3
        }
      },
      "required": [
        "limit",
        "next",
        "page",
        "prev"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
