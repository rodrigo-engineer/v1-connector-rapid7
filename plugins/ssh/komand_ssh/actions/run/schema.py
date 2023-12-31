# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run remote command"


class Input:
    COMMAND = "command"
    HOST = "host"


class Output:
    RESULTS = "results"


class RunInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "command": {
      "type": "string",
      "description": "Command to execute on remote host",
      "order": 2
    },
    "host": {
      "type": "string",
      "description": "Host to run remote commands. If not provided, the connection host will be used",
      "order": 1
    }
  },
  "required": [
    "command"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/results",
      "title": "Results",
      "description": "Results",
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "results": {
      "type": "object",
      "title": "results",
      "properties": {
        "stdout": {
          "type": "string",
          "title": "STDOUT",
          "description": "Stdout",
          "order": 1
        },
        "stderr": {
          "type": "string",
          "title": "STDERR",
          "description": "Stderr",
          "order": 2
        },
        "all_output": {
          "type": "string",
          "title": "All Output",
          "description": "All output",
          "order": 3
        }
      },
      "required": [
        "all_output",
        "stderr",
        "stdout"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
