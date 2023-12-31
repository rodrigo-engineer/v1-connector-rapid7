# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Queries firewall logs. This action uses a direct connection to the firewall"


class Input:
    COUNT = "count"
    DIRECTION = "direction"
    FILTER = "filter"
    INTERVAL = "interval"
    LOG_TYPE = "log_type"
    MAX_TRIES = "max_tries"
    SKIP = "skip"
    

class Output:
    RESPONSE = "response"
    

class RetrieveLogsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of logs to retrieve (Max: 500, Default: 20)",
      "default": 20,
      "order": 2
    },
    "direction": {
      "type": "string",
      "title": "Direction",
      "description": "Order in which to return the logs",
      "enum": [
        "backward",
        "forward"
      ],
      "order": 7
    },
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Search query. Format as a log filter expression",
      "order": 4
    },
    "interval": {
      "type": "number",
      "title": "Interval",
      "description": "Time interval in seconds to wait between queries for commit job completion (Default: 0.5)",
      "default": 0.5,
      "order": 5
    },
    "log_type": {
      "type": "string",
      "title": "Log Type",
      "description": "Type of log to retrieve",
      "enum": [
        "config",
        "hipmatch",
        "system",
        "threat",
        "traffic",
        "url",
        "wildfire"
      ],
      "order": 1
    },
    "max_tries": {
      "type": "integer",
      "title": "Max Tries",
      "description": "Maximum number of times to poll for job completion before timing out (Default: 25)",
      "default": 25,
      "order": 6
    },
    "skip": {
      "type": "integer",
      "title": "Skip",
      "description": "Log retrieval offset, number of entries to skip, (Default: 0)",
      "default": 0,
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RetrieveLogsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/log",
      "title": "Response",
      "description": "Response from the firewall",
      "order": 1
    }
  },
  "definitions": {
    "log": {
      "type": "object",
      "title": "log",
      "properties": {
        "data": {
          "type": "object",
          "title": "Data",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
