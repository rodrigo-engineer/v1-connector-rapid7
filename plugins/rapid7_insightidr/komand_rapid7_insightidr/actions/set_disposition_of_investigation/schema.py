# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Allows to change the disposition of the investigation with the given ID or RRN"


class Input:
    DISPOSITION = "disposition"
    ID = "id"


class Output:
    INVESTIGATION = "investigation"


class SetDispositionOfInvestigationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "disposition": {
      "type": "string",
      "title": "Disposition",
      "description": "Investigation's disposition",
      "enum": [
        "BENIGN",
        "MALICIOUS",
        "NOT_APPLICABLE"
      ],
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The ID or RNN of the investigation to change the disposition of",
      "order": 1
    }
  },
  "required": [
    "disposition",
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetDispositionOfInvestigationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "investigation": {
      "$ref": "#/definitions/investigation",
      "title": "Investigation",
      "description": "The investigation for which the disposition was set",
      "order": 1
    }
  },
  "required": [
    "investigation"
  ],
  "definitions": {
    "assignee": {
      "type": "object",
      "title": "assignee",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the assigned user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the assigned user",
          "order": 2
        }
      }
    },
    "investigation": {
      "type": "object",
      "title": "investigation",
      "properties": {
        "assignee": {
          "$ref": "#/definitions/assignee",
          "title": "Assignee",
          "description": "The user assigned to this investigation, if any",
          "order": 1
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "description": "The time the investigation was created as an ISO formatted timestamp",
          "order": 2
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "The disposition of this investigation, where possible values are BENIGN, MALICIOUS, NOT_APPLICABLE, and UNSPECIFIED",
          "order": 3
        },
        "first_alert_time": {
          "type": "string",
          "title": "First Alert Time",
          "description": "The create time of the first alert belonging to this investigation",
          "order": 4
        },
        "last_accessed": {
          "type": "string",
          "title": "Last Accessed",
          "description": "The time investigation was last viewed or modified",
          "order": 5
        },
        "latest_alert_time": {
          "type": "string",
          "title": "Latest Alert Time",
          "description": "The create time of the most recent alert belonging to this investigation",
          "order": 6
        },
        "organization_id": {
          "type": "string",
          "title": "Organization ID",
          "description": "The id of the organization that owns this investigation",
          "order": 7
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "The investigations priority, where possible values are CRITICAL, HIGH, MEDIUM, LOW, and UNKNOWN",
          "order": 8
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The RRN of the investigation",
          "order": 9
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source of this investigation",
          "order": 10
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the investigation",
          "order": 11
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Investigation title",
          "order": 12
        }
      },
      "required": [
        "created_time",
        "disposition",
        "last_accessed",
        "organization_id",
        "priority",
        "rrn",
        "source",
        "status",
        "title"
      ],
      "definitions": {
        "assignee": {
          "type": "object",
          "title": "assignee",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the assigned user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the assigned user",
              "order": 2
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