# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HOST = "host"
    PORT = "port"
    PREFIX = "prefix"
    PROTOCOL = "protocol"
    TCP = "tcp"
    UDP = "udp"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Statsd Host",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Statsd Port",
      "order": 2
    },
    "prefix": {
      "type": "string",
      "title": "Prefix",
      "description": "Statsd Prefix",
      "order": 4
    },
    "protocol": {
      "type": "string",
      "title": "Protocol",
      "description": "Transport Protocol",
      "enum": [
        "UDP",
        "TCP"
      ],
      "order": 3
    },
    "tcp": {
      "$ref": "#/definitions/timeout",
      "title": "TCP",
      "description": "TCP",
      "order": 5
    },
    "udp": {
      "$ref": "#/definitions/maxudpsize",
      "title": "UDP",
      "description": "UDP",
      "order": 6
    }
  },
  "required": [
    "host",
    "port",
    "protocol"
  ],
  "definitions": {
    "maxudpsize": {
      "type": "object",
      "title": "maxudpsize",
      "properties": {
        "maxudpsize": {
          "type": "integer",
          "title": "Max UDP Size",
          "description": "Max UDP Size",
          "default": 512,
          "order": 1
        }
      }
    },
    "timeout": {
      "type": "object",
      "title": "timeout",
      "properties": {
        "timeout": {
          "type": "integer",
          "title": "Timeout",
          "description": "TCP timeout",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
