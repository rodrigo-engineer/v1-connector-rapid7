# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return associated malicious domains for an IP address"


class Input:
    IP = "ip"
    

class Output:
    DOMAINS = "domains"
    

class LatestDomainsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip": {
      "type": "string",
      "title": "IP Address",
      "description": "IP Address to check for malicious domains",
      "order": 1
    }
  },
  "required": [
    "ip"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LatestDomainsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domains": {
      "type": "array",
      "title": "Domains",
      "description": "The block list domain associated with the IP",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "domains"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
