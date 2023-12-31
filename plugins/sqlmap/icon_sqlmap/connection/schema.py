# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_HOST = "api_host"
    API_PORT = "api_port"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_host": {
      "type": "string",
      "title": "Host",
      "description": "Host of the REST-JSON API server",
      "default": "localhost",
      "order": 1
    },
    "api_port": {
      "type": "string",
      "title": "Port",
      "description": "Port of the the REST-JSON API server",
      "default": 8775,
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
