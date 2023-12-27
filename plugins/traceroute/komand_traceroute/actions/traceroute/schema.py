# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Returns the route used to communicate with the host"


class Input:
    COUNT = "count"
    HOST = "host"
    MAX_TTL = "max_ttl"
    PORT = "port"
    RESOLVE_HOSTNAME = "resolve_hostname"
    SET_ACK = "set_ack"
    TIME_OUT = "time_out"
    

class Output:
    IP = "ip"
    PATH = "path"
    REPLY = "reply"
    RESPONSE = "response"
    

class TracerouteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "The number of probes to be sent to each hop. The default is 3",
      "default": 3,
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "The domain name or IP of the the host to find a route to",
      "order": 1
    },
    "max_ttl": {
      "type": "integer",
      "title": "Max TTL",
      "description": "Set the maximum TTL used in outgoing packets. The default is 30",
      "default": 30,
      "order": 3
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Set the port that traceroute will try to reach e.g. set it to port 443 for a host running an HTTPS server. The default is 80",
      "default": 80,
      "order": 5
    },
    "resolve_hostname": {
      "type": "boolean",
      "title": "Resolve Hostname",
      "description": "If true traceroute will attempt to return a DNS name rather than an IP address. If false, traceroute will always return the IP address",
      "default": true,
      "order": 7
    },
    "set_ack": {
      "type": "boolean",
      "title": "Set Ack",
      "description": "If true set the TCP ACK flag in outgoing packets. By doing so, it is possible to trace through stateless firewalls which permit outgoing TCP connections",
      "default": false,
      "order": 6
    },
    "time_out": {
      "type": "integer",
      "title": "Time Out",
      "description": "Set the timeout, in seconds, to wait for a response for each probe. The default is 3",
      "default": 3,
      "order": 4
    }
  },
  "required": [
    "count",
    "host",
    "max_ttl",
    "port",
    "resolve_hostname",
    "set_ack",
    "time_out"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TracerouteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip": {
      "type": "array",
      "title": "IP",
      "description": "IP addresses",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "path": {
      "type": "array",
      "title": "Path",
      "description": "The path used to get to the host including response times",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "reply": {
      "type": "boolean",
      "title": "Reply",
      "description": "Whether a route was found to the host",
      "order": 1
    },
    "response": {
      "type": "string",
      "title": "Response",
      "description": "The full raw response from traceroute",
      "order": 2
    }
  },
  "required": [
    "ip",
    "path",
    "reply",
    "response"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
