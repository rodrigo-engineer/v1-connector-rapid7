# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Deactivate an activity monitor"


class Input:
    ACTIVITY_MONITOR_ID = "activity_monitor_id"
    

class Output:
    ACTIVITY_MONITOR = "activity_monitor"
    

class DeactivateActivityMonitorInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activity_monitor_id": {
      "type": "integer",
      "title": "Activity Monitor ID",
      "description": "Activity Monitor identifier",
      "order": 1
    }
  },
  "required": [
    "activity_monitor_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeactivateActivityMonitorOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activity_monitor": {
      "$ref": "#/definitions/activity_monitor",
      "title": "Activity Monitor",
      "description": "Deactivated activity monitor",
      "order": 1
    }
  },
  "definitions": {
    "activity_monitor": {
      "type": "object",
      "title": "activity_monitor",
      "properties": {
        "attributes": {
          "$ref": "#/definitions/activity_monitor_attributes",
          "title": "Attributes",
          "description": "Attributes of the resource",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique identifier of the activity_monitor",
          "order": 2
        },
        "links": {
          "$ref": "#/definitions/activity_monitor_links",
          "title": "Links",
          "description": "Resources associated with this object",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 1
        }
      },
      "definitions": {
        "activity_monitor_attributes": {
          "type": "object",
          "title": "activity_monitor_attributes",
          "properties": {
            "active": {
              "type": "boolean",
              "title": "Active",
              "description": "If the activity monitor is active and identifying matches",
              "order": 2
            },
            "file_modification_types_monitored": {
              "type": "array",
              "title": "File Modification Types Monitored",
              "description": "Types of file modifications this monitor will trigger upon",
              "items": {
                "type": "string"
              },
              "order": 4
            },
            "file_paths_monitored": {
              "type": "array",
              "title": "File Paths Monitored",
              "description": "List of case insensitive file path globstrings this monitor will trigger upon",
              "items": {
                "type": "string"
              },
              "order": 5
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type of the activity monitor, such as file_modification",
              "order": 3
            },
            "usernames_excluded": {
              "type": "array",
              "title": "Usernames Excluded",
              "description": "List of case insensitive globstrings that select which usernames this monitor will filter out",
              "items": {
                "type": "string"
              },
              "order": 7
            },
            "usernames_matched": {
              "type": "array",
              "title": "Usernames Matched",
              "description": "List of case insensitive globstrings that select which usernames this monitor will match against",
              "items": {
                "type": "string"
              },
              "order": 6
            }
          }
        },
        "activity_monitor_links": {
          "type": "object",
          "title": "activity_monitor_links",
          "properties": {
            "matches": {
              "$ref": "#/definitions/resource_link",
              "title": "Matches",
              "description": "Matches",
              "order": 2
            },
            "self": {
              "$ref": "#/definitions/resource_link",
              "title": "Self",
              "description": "Self",
              "order": 1
            }
          },
          "definitions": {
            "resource_link": {
              "type": "object",
              "title": "resource_link",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "description": "Link to a resource",
                  "order": 1
                }
              }
            }
          }
        },
        "resource_link": {
          "type": "object",
          "title": "resource_link",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Link to a resource",
              "order": 1
            }
          }
        }
      }
    },
    "activity_monitor_attributes": {
      "type": "object",
      "title": "activity_monitor_attributes",
      "properties": {
        "active": {
          "type": "boolean",
          "title": "Active",
          "description": "If the activity monitor is active and identifying matches",
          "order": 2
        },
        "file_modification_types_monitored": {
          "type": "array",
          "title": "File Modification Types Monitored",
          "description": "Types of file modifications this monitor will trigger upon",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "file_paths_monitored": {
          "type": "array",
          "title": "File Paths Monitored",
          "description": "List of case insensitive file path globstrings this monitor will trigger upon",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the activity monitor, such as file_modification",
          "order": 3
        },
        "usernames_excluded": {
          "type": "array",
          "title": "Usernames Excluded",
          "description": "List of case insensitive globstrings that select which usernames this monitor will filter out",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "usernames_matched": {
          "type": "array",
          "title": "Usernames Matched",
          "description": "List of case insensitive globstrings that select which usernames this monitor will match against",
          "items": {
            "type": "string"
          },
          "order": 6
        }
      }
    },
    "activity_monitor_links": {
      "type": "object",
      "title": "activity_monitor_links",
      "properties": {
        "matches": {
          "$ref": "#/definitions/resource_link",
          "title": "Matches",
          "description": "Matches",
          "order": 2
        },
        "self": {
          "$ref": "#/definitions/resource_link",
          "title": "Self",
          "description": "Self",
          "order": 1
        }
      },
      "definitions": {
        "resource_link": {
          "type": "object",
          "title": "resource_link",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Link to a resource",
              "order": 1
            }
          }
        }
      }
    },
    "resource_link": {
      "type": "object",
      "title": "resource_link",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Link to a resource",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
