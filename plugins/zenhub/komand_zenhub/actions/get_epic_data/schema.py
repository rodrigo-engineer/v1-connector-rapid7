# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get the ZenHub Data for a ZenHub Epic"


class Input:
    EPIC_ID = "epic_id"
    REPO_ID = "repo_id"
    

class Output:
    DATA = "data"
    

class GetEpicDataInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "epic_id": {
      "type": "integer",
      "title": "Epic ID",
      "description": "GitHub Issue Number of the ZenHub Epic",
      "order": 2
    },
    "repo_id": {
      "type": "integer",
      "title": "Repository ID",
      "description": "GitHub Repository ID e.g. 24237263",
      "order": 1
    }
  },
  "required": [
    "epic_id",
    "repo_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetEpicDataOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/epic_data",
      "title": "Epic Data",
      "description": "ZenHub Epic Data",
      "order": 1
    }
  },
  "definitions": {
    "epic_data": {
      "type": "object",
      "title": "epic_data",
      "properties": {
        "estimate_value": {
          "type": "integer",
          "title": "Estimate Value",
          "description": "Estimate value",
          "order": 3
        },
        "issues": {
          "type": "array",
          "title": "Issues",
          "description": "Issues",
          "items": {
            "$ref": "#/definitions/issue_data"
          },
          "order": 2
        },
        "pipeline_name": {
          "type": "string",
          "title": "Pipeline Name",
          "description": "Pipeline name",
          "order": 4
        },
        "total_epic_estimates_value": {
          "type": "integer",
          "title": "Total Epic Estimates Value",
          "description": "Total epic estimates value",
          "order": 1
        }
      },
      "definitions": {
        "issue_data": {
          "type": "object",
          "title": "issue_data",
          "properties": {
            "estimate_value": {
              "type": "integer",
              "title": "Estimated Value",
              "description": "Estimated value",
              "order": 6
            },
            "is_epic": {
              "type": "boolean",
              "title": "Is epic",
              "description": "Is epic",
              "order": 3
            },
            "issue_number": {
              "type": "integer",
              "title": "Issue number",
              "description": "Issue number",
              "order": 1
            },
            "pipeline_name": {
              "type": "string",
              "title": "Pipeline Name",
              "description": "Pipeline name",
              "order": 5
            },
            "plus_ones": {
              "type": "array",
              "title": "Plus One",
              "description": "Plus one",
              "items": {
                "$ref": "#/definitions/plus_one"
              },
              "order": 7
            },
            "position": {
              "type": "integer",
              "title": "Position",
              "description": "Position",
              "order": 4
            },
            "repo_id": {
              "type": "integer",
              "title": "Repo id",
              "description": "Repo id",
              "order": 2
            }
          },
          "definitions": {
            "plus_one": {
              "type": "object",
              "title": "plus_one",
              "properties": {
                "created_at": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "description": "Created at",
                  "format": "date-time",
                  "order": 2
                },
                "user_id": {
                  "type": "integer",
                  "title": "User Id",
                  "description": "User ID",
                  "order": 1
                }
              }
            }
          }
        },
        "plus_one": {
          "type": "object",
          "title": "plus_one",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "Created at",
              "format": "date-time",
              "order": 2
            },
            "user_id": {
              "type": "integer",
              "title": "User Id",
              "description": "User ID",
              "order": 1
            }
          }
        }
      }
    },
    "issue_data": {
      "type": "object",
      "title": "issue_data",
      "properties": {
        "estimate_value": {
          "type": "integer",
          "title": "Estimated Value",
          "description": "Estimated value",
          "order": 6
        },
        "is_epic": {
          "type": "boolean",
          "title": "Is epic",
          "description": "Is epic",
          "order": 3
        },
        "issue_number": {
          "type": "integer",
          "title": "Issue number",
          "description": "Issue number",
          "order": 1
        },
        "pipeline_name": {
          "type": "string",
          "title": "Pipeline Name",
          "description": "Pipeline name",
          "order": 5
        },
        "plus_ones": {
          "type": "array",
          "title": "Plus One",
          "description": "Plus one",
          "items": {
            "$ref": "#/definitions/plus_one"
          },
          "order": 7
        },
        "position": {
          "type": "integer",
          "title": "Position",
          "description": "Position",
          "order": 4
        },
        "repo_id": {
          "type": "integer",
          "title": "Repo id",
          "description": "Repo id",
          "order": 2
        }
      },
      "definitions": {
        "plus_one": {
          "type": "object",
          "title": "plus_one",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "Created at",
              "format": "date-time",
              "order": 2
            },
            "user_id": {
              "type": "integer",
              "title": "User Id",
              "description": "User ID",
              "order": 1
            }
          }
        }
      }
    },
    "plus_one": {
      "type": "object",
      "title": "plus_one",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Created at",
          "format": "date-time",
          "order": 2
        },
        "user_id": {
          "type": "integer",
          "title": "User Id",
          "description": "User ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
