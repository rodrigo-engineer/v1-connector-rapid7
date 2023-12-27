# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gets the data for a single ticket, not including the history and comments"


class Input:
    TICKET_ID = "ticket_id"
    

class Output:
    TICKET = "Ticket"
    

class TicketPropertiesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID e.g. 3",
      "order": 1
    }
  },
  "required": [
    "ticket_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TicketPropertiesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Ticket": {
      "$ref": "#/definitions/Ticket",
      "title": "Ticket",
      "description": "Ticket",
      "order": 1
    }
  },
  "definitions": {
    "Ticket": {
      "type": "object",
      "title": "Ticket",
      "properties": {
        "AdminCc": {
          "type": "string",
          "title": "AdminCc",
          "order": 10
        },
        "Cc": {
          "type": "string",
          "title": "Cc",
          "order": 9
        },
        "Created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "format": "date-time",
          "order": 11
        },
        "Creator": {
          "type": "string",
          "title": "Creator",
          "order": 3
        },
        "Due": {
          "type": "string",
          "title": "Due",
          "order": 14
        },
        "FinalPriority": {
          "type": "string",
          "title": "FinalPriority",
          "order": 7
        },
        "InitialPriority": {
          "type": "string",
          "title": "InitialPriority",
          "order": 6
        },
        "Owner": {
          "type": "string",
          "title": "Owner",
          "order": 2
        },
        "Priority": {
          "type": "string",
          "title": "Priority",
          "order": 5
        },
        "Queue": {
          "type": "string",
          "title": "Queue",
          "order": 1
        },
        "Requestors": {
          "type": "array",
          "title": "Requestors",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "Resolved": {
          "type": "string",
          "title": "Resolved",
          "order": 15
        },
        "Started": {
          "type": "string",
          "title": "Started",
          "displayType": "date",
          "format": "date-time",
          "order": 13
        },
        "Starts": {
          "type": "string",
          "title": "Starts",
          "displayType": "date",
          "format": "date-time",
          "order": 12
        },
        "Subject": {
          "type": "string",
          "title": "Subject",
          "order": 4
        },
        "TimeEstimated": {
          "type": "string",
          "title": "TimeEstimated",
          "order": 17
        },
        "TimeLeft": {
          "type": "string",
          "title": "TimeLeft",
          "order": 19
        },
        "TimeWorked": {
          "type": "string",
          "title": "TimeWorked",
          "order": 18
        },
        "Told": {
          "type": "string",
          "title": "Told",
          "order": 16
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
