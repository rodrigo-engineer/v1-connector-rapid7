# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get requested watchlist"


class Input:
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WATCHLISTALIAS = "watchlistAlias"
    WORKSPACENAME = "workspaceName"
    

class Output:
    WATCHLIST = "watchlist"
    

class GetWatchlistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription. The name is case insensitive",
      "order": 1
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID",
      "order": 2
    },
    "watchlistAlias": {
      "type": "string",
      "title": "Watchlist Alias",
      "description": "The watchlist alias",
      "order": 4
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 3
    }
  },
  "required": [
    "resourceGroupName",
    "subscriptionId",
    "watchlistAlias",
    "workspaceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetWatchlistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "watchlist": {
      "$ref": "#/definitions/Watchlist",
      "title": "Watchlist",
      "description": "Requested watchlist",
      "order": 1
    }
  },
  "definitions": {
    "UserInfo": {
      "type": "object",
      "title": "UserInfo",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the user",
          "order": 2
        },
        "objectId": {
          "type": "string",
          "title": "Object Identification",
          "description": "The object ID of the user",
          "order": 3
        }
      }
    },
    "Watchlist": {
      "type": "object",
      "title": "Watchlist",
      "properties": {
        "etag": {
          "type": "string",
          "title": "Etag",
          "description": "Entity tag of the resource",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Fully qualified resource ID for the resource",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Resource name (short ID)",
          "order": 4
        },
        "properties": {
          "$ref": "#/definitions/WatchlistProperties",
          "title": "Properties",
          "description": "Watchlist properties",
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Resource type",
          "order": 1
        }
      },
      "definitions": {
        "UserInfo": {
          "type": "object",
          "title": "UserInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the user",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object Identification",
              "description": "The object ID of the user",
              "order": 3
            }
          }
        },
        "WatchlistProperties": {
          "type": "object",
          "title": "WatchlistProperties",
          "properties": {
            "contentType": {
              "type": "string",
              "title": "Content Type",
              "description": "The content type of the raw content",
              "order": 1
            },
            "created": {
              "type": "string",
              "title": "Created",
              "displayType": "date",
              "description": "The time the watchlist was created",
              "format": "date-time",
              "order": 2
            },
            "createdBy": {
              "$ref": "#/definitions/UserInfo",
              "title": "Created By",
              "description": "Describes a user that created the watchlist",
              "order": 3
            },
            "defaultDuration": {
              "type": "string",
              "title": "Default Duration",
              "description": "The default duration of a watchlist (in ISO 8601 duration format)",
              "order": 4
            },
            "description": {
              "type": "string",
              "title": "Description",
              "description": "A description of the watchlist",
              "order": 5
            },
            "displayName": {
              "type": "string",
              "title": "Display Name",
              "description": "The display name of the watchlist",
              "order": 6
            },
            "isDeleted": {
              "type": "boolean",
              "title": "Is Deleted",
              "description": "A flag that indicates if the watchlist is deleted or not",
              "order": 7
            },
            "itemsSearchKey": {
              "type": "string",
              "title": "Items Search Key",
              "description": "The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address",
              "order": 8
            },
            "labels": {
              "type": "array",
              "title": "List of labels relevant to this watchlist",
              "description": "List of labels relevant to this watchlist",
              "items": {
                "type": "string"
              },
              "order": 9
            },
            "numberOfLinesToSkip": {
              "type": "integer",
              "title": "Number Of Lines To Skip",
              "description": "The number of lines in a CSV content to skip before the header",
              "order": 10
            },
            "provider": {
              "type": "string",
              "title": "Provider",
              "description": "The provider of the watchlist",
              "order": 11
            },
            "rawContent": {
              "type": "string",
              "title": "Raw Content",
              "description": "The raw content that represents to watchlist items to create",
              "order": 12
            },
            "source": {
              "type": "string",
              "title": "Source",
              "description": "The source of the watchlist",
              "order": 13
            },
            "tenantId": {
              "type": "string",
              "title": "Tenant ID",
              "description": "The tenantId where the watchlist belongs to",
              "order": 14
            },
            "updated": {
              "type": "string",
              "title": "Updated",
              "description": "The last time the watchlist was updated",
              "order": 15
            },
            "updatedBy": {
              "$ref": "#/definitions/UserInfo",
              "title": "Updated By",
              "description": "Describes a user that updated the watchlist",
              "order": 16
            },
            "uploadStatus": {
              "type": "string",
              "title": "Watchlist Upload Status",
              "description": "The status of the watchlist",
              "order": 17
            },
            "watchlistAlias": {
              "type": "string",
              "title": "Watchlist Alias",
              "description": "The alias of the watchlist",
              "order": 18
            },
            "watchlistId": {
              "type": "string",
              "title": "Watchlist ID",
              "description": "The id (a Guid) of the watchlist",
              "order": 19
            },
            "watchlistType": {
              "type": "string",
              "title": "Watchlist Type",
              "description": "The type of the watchlist",
              "order": 20
            }
          },
          "required": [
            "displayName",
            "itemsSearchKey",
            "provider",
            "source"
          ],
          "definitions": {
            "UserInfo": {
              "type": "object",
              "title": "UserInfo",
              "properties": {
                "email": {
                  "type": "string",
                  "title": "Email",
                  "description": "The email of the user",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "The name of the user",
                  "order": 2
                },
                "objectId": {
                  "type": "string",
                  "title": "Object Identification",
                  "description": "The object ID of the user",
                  "order": 3
                }
              }
            }
          }
        }
      }
    },
    "WatchlistProperties": {
      "type": "object",
      "title": "WatchlistProperties",
      "properties": {
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "The content type of the raw content",
          "order": 1
        },
        "created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "description": "The time the watchlist was created",
          "format": "date-time",
          "order": 2
        },
        "createdBy": {
          "$ref": "#/definitions/UserInfo",
          "title": "Created By",
          "description": "Describes a user that created the watchlist",
          "order": 3
        },
        "defaultDuration": {
          "type": "string",
          "title": "Default Duration",
          "description": "The default duration of a watchlist (in ISO 8601 duration format)",
          "order": 4
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "A description of the watchlist",
          "order": 5
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "The display name of the watchlist",
          "order": 6
        },
        "isDeleted": {
          "type": "boolean",
          "title": "Is Deleted",
          "description": "A flag that indicates if the watchlist is deleted or not",
          "order": 7
        },
        "itemsSearchKey": {
          "type": "string",
          "title": "Items Search Key",
          "description": "The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address",
          "order": 8
        },
        "labels": {
          "type": "array",
          "title": "List of labels relevant to this watchlist",
          "description": "List of labels relevant to this watchlist",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "numberOfLinesToSkip": {
          "type": "integer",
          "title": "Number Of Lines To Skip",
          "description": "The number of lines in a CSV content to skip before the header",
          "order": 10
        },
        "provider": {
          "type": "string",
          "title": "Provider",
          "description": "The provider of the watchlist",
          "order": 11
        },
        "rawContent": {
          "type": "string",
          "title": "Raw Content",
          "description": "The raw content that represents to watchlist items to create",
          "order": 12
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source of the watchlist",
          "order": 13
        },
        "tenantId": {
          "type": "string",
          "title": "Tenant ID",
          "description": "The tenantId where the watchlist belongs to",
          "order": 14
        },
        "updated": {
          "type": "string",
          "title": "Updated",
          "description": "The last time the watchlist was updated",
          "order": 15
        },
        "updatedBy": {
          "$ref": "#/definitions/UserInfo",
          "title": "Updated By",
          "description": "Describes a user that updated the watchlist",
          "order": 16
        },
        "uploadStatus": {
          "type": "string",
          "title": "Watchlist Upload Status",
          "description": "The status of the watchlist",
          "order": 17
        },
        "watchlistAlias": {
          "type": "string",
          "title": "Watchlist Alias",
          "description": "The alias of the watchlist",
          "order": 18
        },
        "watchlistId": {
          "type": "string",
          "title": "Watchlist ID",
          "description": "The id (a Guid) of the watchlist",
          "order": 19
        },
        "watchlistType": {
          "type": "string",
          "title": "Watchlist Type",
          "description": "The type of the watchlist",
          "order": 20
        }
      },
      "required": [
        "displayName",
        "itemsSearchKey",
        "provider",
        "source"
      ],
      "definitions": {
        "UserInfo": {
          "type": "object",
          "title": "UserInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the user",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object Identification",
              "description": "The object ID of the user",
              "order": 3
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
