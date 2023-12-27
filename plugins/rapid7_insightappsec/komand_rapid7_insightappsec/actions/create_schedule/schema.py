# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new schedule"


class Input:
    ENABLED = "enabled"
    FIRSTSTART = "firstStart"
    FREQUENCY = "frequency"
    LASTSTART = "lastStart"
    NAME = "name"
    RRULE = "rrule"
    SCANCONFIGID = "scanConfigId"
    

class Output:
    SUCCESS = "success"
    

class CreateScheduleInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "enabled": {
      "type": "boolean",
      "title": "Enabled",
      "description": "Whether the schedule is enabled",
      "default": true,
      "order": 3
    },
    "firstStart": {
      "type": "string",
      "title": "First Start",
      "displayType": "date",
      "description": "The first start date and time of the schedule",
      "format": "date-time",
      "order": 4
    },
    "frequency": {
      "$ref": "#/definitions/frequencyInput",
      "title": "Frequency",
      "description": "The frequency describes how (and if) the schedule should repeat. If frequency and recurrence rule are given then the recurrence rule will be used",
      "order": 6
    },
    "lastStart": {
      "type": "string",
      "title": "Last Start",
      "displayType": "date",
      "description": "The last start date and time of the schedule",
      "format": "date-time",
      "order": 5
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the schedule",
      "order": 1
    },
    "rrule": {
      "type": "string",
      "title": "Recurrence Rule",
      "description": "The recurrence rule describes how (and if) the schedule should repeat. If frequency and recurrence rule are given then the recurrence rule will be used",
      "order": 7
    },
    "scanConfigId": {
      "type": "string",
      "title": "Scan Config ID",
      "description": "The scan config ID of the schedule",
      "order": 2
    }
  },
  "required": [
    "enabled",
    "firstStart",
    "name",
    "scanConfigId"
  ],
  "definitions": {
    "frequencyInput": {
      "type": "object",
      "title": "frequencyInput",
      "properties": {
        "interval": {
          "type": "integer",
          "title": "Interval",
          "description": "The interval of the frequency",
          "default": 1,
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of the frequency",
          "default": "HOURLY",
          "enum": [
            "ONCE",
            "HOURLY",
            "DAILY",
            "WEEKLY",
            "MONTHLY"
          ],
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateScheduleOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
