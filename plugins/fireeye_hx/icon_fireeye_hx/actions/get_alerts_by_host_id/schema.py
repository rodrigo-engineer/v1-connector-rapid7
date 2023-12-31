# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get alerts for a host given the host ID. To get all alerts for the host, leave the offset and limit parameters empty or set to 0"


class Input:
    HOST_ID = "host_id"
    LIMIT = "limit"
    OFFSET = "offset"
    

class Output:
    ALERTS = "alerts"
    

class GetAlertsByHostIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host_id": {
      "type": "string",
      "title": "Host ID",
      "description": "Host ID",
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Specifies how many alerts are returned",
      "default": 100,
      "order": 3
    },
    "offset": {
      "type": "integer",
      "title": "Offset",
      "description": "Specifies which alert to start with in the response",
      "order": 2
    }
  },
  "required": [
    "host_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAlertsByHostIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "Alerts",
      "items": {
        "$ref": "#/definitions/alert"
      },
      "order": 1
    }
  },
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "Agent ID",
          "order": 1
        },
        "containment_state": {
          "type": "string",
          "title": "Containment State",
          "description": "Containment state of the agent",
          "order": 2
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "Relative URL for the agent",
          "order": 3
        }
      }
    },
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "_id": {
          "type": "number",
          "title": "Alert ID",
          "description": "Alert ID",
          "order": 1
        },
        "agent": {
          "$ref": "#/definitions/agent",
          "title": "Agent",
          "description": "Agent associated with the alert",
          "order": 2
        },
        "condition": {
          "$ref": "#/definitions/condition",
          "title": "Condition",
          "description": "Condition associated with the alert",
          "order": 3
        },
        "event_at": {
          "type": "string",
          "title": "Event At",
          "displayType": "date",
          "description": "Timestamp for the alert",
          "format": "date-time",
          "order": 4
        },
        "event_id": {
          "type": "number",
          "title": "Event ID",
          "description": "ID of the event",
          "order": 5
        },
        "event_type": {
          "type": "string",
          "title": "Event Type",
          "description": "Type of alert event that occurred",
          "order": 6
        },
        "event_values": {
          "$ref": "#/definitions/event_values",
          "title": "Event Values",
          "description": "Information about the alert. These properties may/may not be available depending on the 'Event Type' property",
          "order": 7
        },
        "indicator": {
          "$ref": "#/definitions/indicator",
          "title": "Indicator",
          "description": "Alert indicator",
          "order": 8
        },
        "is_false_positive": {
          "type": "boolean",
          "title": "Is False Positive",
          "description": "Whether or not the alert is a false positive",
          "order": 9
        },
        "matched_at": {
          "type": "string",
          "title": "Matched At",
          "displayType": "date",
          "description": "When the alert rule matched",
          "format": "date-time",
          "order": 10
        },
        "matched_source_alerts": {
          "type": "array",
          "title": "Matched Source Alerts",
          "description": "Matched source alerts",
          "items": {
            "type": "object"
          },
          "order": 11
        },
        "reported_at": {
          "type": "string",
          "title": "Reported At",
          "displayType": "date",
          "description": "Timestamp for the alert report",
          "format": "date-time",
          "order": 12
        },
        "resolution": {
          "type": "string",
          "title": "Resolution",
          "description": "Resolution",
          "order": 13
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Alert source",
          "order": 14
        },
        "subtype": {
          "type": "string",
          "title": "Subtype",
          "description": "Alert subtype",
          "order": 15
        }
      },
      "definitions": {
        "agent": {
          "type": "object",
          "title": "agent",
          "properties": {
            "_id": {
              "type": "string",
              "title": "ID",
              "description": "Agent ID",
              "order": 1
            },
            "containment_state": {
              "type": "string",
              "title": "Containment State",
              "description": "Containment state of the agent",
              "order": 2
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "Relative URL for the agent",
              "order": 3
            }
          }
        },
        "condition": {
          "type": "object",
          "title": "condition",
          "properties": {
            "_id": {
              "type": "string",
              "title": "ID",
              "description": "Condition ID",
              "order": 1
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "Relative URL for the condition",
              "order": 2
            }
          }
        },
        "event_values": {
          "type": "object",
          "title": "event_values",
          "properties": {
            "dnsLookupEvent/hostname": {
              "type": "string",
              "title": "DNS Lookup Event Hostname",
              "description": "Hostname",
              "order": 27
            },
            "dnsLookupEvent/pid": {
              "type": "number",
              "title": "DNS Lookup Event PID",
              "description": "PID",
              "order": 28
            },
            "dnsLookupEvent/process": {
              "type": "string",
              "title": "DNS Lookup Event Process",
              "description": "Process",
              "order": 29
            },
            "dnsLookupEvent/processPath": {
              "type": "string",
              "title": "DNS Lookup Event Process Path",
              "description": "Process path",
              "order": 30
            },
            "dnsLookupEvent/timestamp": {
              "type": "string",
              "title": "DNS Lookup Event Timestamp",
              "displayType": "date",
              "description": "Timestamp of the DNS lookup event",
              "format": "date-time",
              "order": 31
            },
            "dnsLookupEvent/username": {
              "type": "string",
              "title": "DNS Lookup Event Username",
              "description": "Username",
              "order": 32
            },
            "fileWriteEvent/closed": {
              "type": "number",
              "title": "File Write Event Closed",
              "description": "Closed",
              "order": 8
            },
            "fileWriteEvent/dataAtLowestOffset": {
              "type": "string",
              "title": "File Write Event Data at Lowest Offset",
              "description": "Data at lowest offset, base64-encoded",
              "order": 9
            },
            "fileWriteEvent/devicePath": {
              "type": "string",
              "title": "File Write Event Device Path",
              "description": "Device path",
              "order": 10
            },
            "fileWriteEvent/drive": {
              "type": "string",
              "title": "File Write Event Drive",
              "description": "Drive",
              "order": 11
            },
            "fileWriteEvent/fileExtension": {
              "type": "string",
              "title": "File Write Event File Extension",
              "description": "File extension",
              "order": 12
            },
            "fileWriteEvent/fileName": {
              "type": "string",
              "title": "File Write Event File Name",
              "description": "File name",
              "order": 13
            },
            "fileWriteEvent/filePath": {
              "type": "string",
              "title": "File Write Event File Path",
              "description": "File path",
              "order": 14
            },
            "fileWriteEvent/fullPath": {
              "type": "string",
              "title": "File Write Event Full Path",
              "description": "Full path",
              "order": 15
            },
            "fileWriteEvent/lowestFileOffsetSeen": {
              "type": "number",
              "title": "File Write Event Lowest File Offset Seen",
              "description": "Lowest file offset seen",
              "order": 16
            },
            "fileWriteEvent/md5": {
              "type": "string",
              "title": "File Write Event MD5",
              "description": "MD5 hash",
              "order": 17
            },
            "fileWriteEvent/numBytesSeenWritten": {
              "type": "number",
              "title": "File Write Event Number of Bytes Seen Written",
              "description": "Number of bytes seen written",
              "order": 18
            },
            "fileWriteEvent/pid": {
              "type": "number",
              "title": "File Write Event PID",
              "description": "PID",
              "order": 19
            },
            "fileWriteEvent/process": {
              "type": "string",
              "title": "File Write Event Process",
              "description": "Process",
              "order": 20
            },
            "fileWriteEvent/processPath": {
              "type": "string",
              "title": "File Write Event Process Path",
              "description": "Process path",
              "order": 21
            },
            "fileWriteEvent/size": {
              "type": "number",
              "title": "File Write Event Size",
              "description": "number",
              "order": 22
            },
            "fileWriteEvent/textAtLowestOffset": {
              "type": "string",
              "title": "File Write Event Text at Lowest Offset",
              "description": "Text at lowest offset",
              "order": 23
            },
            "fileWriteEvent/timestamp": {
              "type": "string",
              "title": "File Write Event Timestamp",
              "displayType": "date",
              "description": "Timestamp of the file write event",
              "format": "date-time",
              "order": 24
            },
            "fileWriteEvent/username": {
              "type": "string",
              "title": "File Write Event Username",
              "description": "Username",
              "order": 25
            },
            "fileWriteEvent/writes": {
              "type": "number",
              "title": "File Write Event Writes",
              "description": "Amount of file writes",
              "order": 26
            },
            "ipv4NetworkEvent/localIP": {
              "type": "string",
              "title": "IPv4 Network Event Local IP Address",
              "description": "Local IP address",
              "order": 1
            },
            "ipv4NetworkEvent/localPort": {
              "type": "number",
              "title": "IPv4 Network Event Local Port",
              "description": "Local port",
              "order": 2
            },
            "ipv4NetworkEvent/pid": {
              "type": "number",
              "title": "IPv4 Network Event PID",
              "description": "PID",
              "order": 3
            },
            "ipv4NetworkEvent/protocol": {
              "type": "string",
              "title": "IPv4 Network Event Protocol",
              "description": "Protocol, e.g. 'ICMP'",
              "order": 4
            },
            "ipv4NetworkEvent/remoteIP": {
              "type": "string",
              "title": "IPv4 Network Event Remote IP Address",
              "description": "Remote IP address",
              "order": 5
            },
            "ipv4NetworkEvent/remotePort": {
              "type": "number",
              "title": "IPv4 Network Event Remote Port",
              "description": "Remote port",
              "order": 6
            },
            "ipv4NetworkEvent/timestamp": {
              "type": "string",
              "title": "IPv4 Network Event Timestamp",
              "displayType": "date",
              "description": "Event timestamp",
              "format": "date-time",
              "order": 7
            }
          }
        },
        "indicator": {
          "type": "object",
          "title": "indicator",
          "properties": {
            "_id": {
              "type": "string",
              "title": "ID",
              "description": "Indicator ID",
              "order": 1
            },
            "display_name": {
              "type": "string",
              "title": "Display Name",
              "description": "Indicator display name",
              "order": 2
            },
            "uri_name": {
              "type": "string",
              "title": "URI Name",
              "description": "URI name",
              "order": 3
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "Relative URL for the indicator",
              "order": 4
            }
          }
        }
      }
    },
    "condition": {
      "type": "object",
      "title": "condition",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "Condition ID",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "Relative URL for the condition",
          "order": 2
        }
      }
    },
    "event_values": {
      "type": "object",
      "title": "event_values",
      "properties": {
        "dnsLookupEvent/hostname": {
          "type": "string",
          "title": "DNS Lookup Event Hostname",
          "description": "Hostname",
          "order": 27
        },
        "dnsLookupEvent/pid": {
          "type": "number",
          "title": "DNS Lookup Event PID",
          "description": "PID",
          "order": 28
        },
        "dnsLookupEvent/process": {
          "type": "string",
          "title": "DNS Lookup Event Process",
          "description": "Process",
          "order": 29
        },
        "dnsLookupEvent/processPath": {
          "type": "string",
          "title": "DNS Lookup Event Process Path",
          "description": "Process path",
          "order": 30
        },
        "dnsLookupEvent/timestamp": {
          "type": "string",
          "title": "DNS Lookup Event Timestamp",
          "displayType": "date",
          "description": "Timestamp of the DNS lookup event",
          "format": "date-time",
          "order": 31
        },
        "dnsLookupEvent/username": {
          "type": "string",
          "title": "DNS Lookup Event Username",
          "description": "Username",
          "order": 32
        },
        "fileWriteEvent/closed": {
          "type": "number",
          "title": "File Write Event Closed",
          "description": "Closed",
          "order": 8
        },
        "fileWriteEvent/dataAtLowestOffset": {
          "type": "string",
          "title": "File Write Event Data at Lowest Offset",
          "description": "Data at lowest offset, base64-encoded",
          "order": 9
        },
        "fileWriteEvent/devicePath": {
          "type": "string",
          "title": "File Write Event Device Path",
          "description": "Device path",
          "order": 10
        },
        "fileWriteEvent/drive": {
          "type": "string",
          "title": "File Write Event Drive",
          "description": "Drive",
          "order": 11
        },
        "fileWriteEvent/fileExtension": {
          "type": "string",
          "title": "File Write Event File Extension",
          "description": "File extension",
          "order": 12
        },
        "fileWriteEvent/fileName": {
          "type": "string",
          "title": "File Write Event File Name",
          "description": "File name",
          "order": 13
        },
        "fileWriteEvent/filePath": {
          "type": "string",
          "title": "File Write Event File Path",
          "description": "File path",
          "order": 14
        },
        "fileWriteEvent/fullPath": {
          "type": "string",
          "title": "File Write Event Full Path",
          "description": "Full path",
          "order": 15
        },
        "fileWriteEvent/lowestFileOffsetSeen": {
          "type": "number",
          "title": "File Write Event Lowest File Offset Seen",
          "description": "Lowest file offset seen",
          "order": 16
        },
        "fileWriteEvent/md5": {
          "type": "string",
          "title": "File Write Event MD5",
          "description": "MD5 hash",
          "order": 17
        },
        "fileWriteEvent/numBytesSeenWritten": {
          "type": "number",
          "title": "File Write Event Number of Bytes Seen Written",
          "description": "Number of bytes seen written",
          "order": 18
        },
        "fileWriteEvent/pid": {
          "type": "number",
          "title": "File Write Event PID",
          "description": "PID",
          "order": 19
        },
        "fileWriteEvent/process": {
          "type": "string",
          "title": "File Write Event Process",
          "description": "Process",
          "order": 20
        },
        "fileWriteEvent/processPath": {
          "type": "string",
          "title": "File Write Event Process Path",
          "description": "Process path",
          "order": 21
        },
        "fileWriteEvent/size": {
          "type": "number",
          "title": "File Write Event Size",
          "description": "number",
          "order": 22
        },
        "fileWriteEvent/textAtLowestOffset": {
          "type": "string",
          "title": "File Write Event Text at Lowest Offset",
          "description": "Text at lowest offset",
          "order": 23
        },
        "fileWriteEvent/timestamp": {
          "type": "string",
          "title": "File Write Event Timestamp",
          "displayType": "date",
          "description": "Timestamp of the file write event",
          "format": "date-time",
          "order": 24
        },
        "fileWriteEvent/username": {
          "type": "string",
          "title": "File Write Event Username",
          "description": "Username",
          "order": 25
        },
        "fileWriteEvent/writes": {
          "type": "number",
          "title": "File Write Event Writes",
          "description": "Amount of file writes",
          "order": 26
        },
        "ipv4NetworkEvent/localIP": {
          "type": "string",
          "title": "IPv4 Network Event Local IP Address",
          "description": "Local IP address",
          "order": 1
        },
        "ipv4NetworkEvent/localPort": {
          "type": "number",
          "title": "IPv4 Network Event Local Port",
          "description": "Local port",
          "order": 2
        },
        "ipv4NetworkEvent/pid": {
          "type": "number",
          "title": "IPv4 Network Event PID",
          "description": "PID",
          "order": 3
        },
        "ipv4NetworkEvent/protocol": {
          "type": "string",
          "title": "IPv4 Network Event Protocol",
          "description": "Protocol, e.g. 'ICMP'",
          "order": 4
        },
        "ipv4NetworkEvent/remoteIP": {
          "type": "string",
          "title": "IPv4 Network Event Remote IP Address",
          "description": "Remote IP address",
          "order": 5
        },
        "ipv4NetworkEvent/remotePort": {
          "type": "number",
          "title": "IPv4 Network Event Remote Port",
          "description": "Remote port",
          "order": 6
        },
        "ipv4NetworkEvent/timestamp": {
          "type": "string",
          "title": "IPv4 Network Event Timestamp",
          "displayType": "date",
          "description": "Event timestamp",
          "format": "date-time",
          "order": 7
        }
      }
    },
    "indicator": {
      "type": "object",
      "title": "indicator",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "Indicator ID",
          "order": 1
        },
        "display_name": {
          "type": "string",
          "title": "Display Name",
          "description": "Indicator display name",
          "order": 2
        },
        "uri_name": {
          "type": "string",
          "title": "URI Name",
          "description": "URI name",
          "order": 3
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "Relative URL for the indicator",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
