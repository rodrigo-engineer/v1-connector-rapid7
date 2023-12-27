# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return subnet information for IP and Netmask"


class Input:
    CIDR = "cidr"
    

class Output:
    BINARY_NETMASK = "binary_netmask"
    BROADCAST = "broadcast"
    CIDR = "cidr"
    HOST_RANGE = "host_range"
    HOSTS = "hosts"
    IP = "ip"
    IP_CLASS = "ip_class"
    NETMASK = "netmask"
    SUBNET_ID = "subnet_id"
    SUBNETS = "subnets"
    WILDCARD = "wildcard"
    

class CalculateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cidr": {
      "type": "string",
      "title": "Network",
      "description": "Network in CIDR notation, E.g. 198.51.100.0/24",
      "order": 1
    }
  },
  "required": [
    "cidr"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CalculateOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "binary_netmask": {
      "type": "string",
      "title": "Binary Netmask",
      "description": "Binary netmask",
      "order": 5
    },
    "broadcast": {
      "type": "string",
      "title": "Broadcast",
      "description": "Broadcast address",
      "order": 11
    },
    "cidr": {
      "type": "string",
      "title": "CIDR Notation",
      "description": "CIDR notation",
      "order": 4
    },
    "host_range": {
      "type": "string",
      "title": "Host Range",
      "description": "Host address range",
      "order": 10
    },
    "hosts": {
      "type": "integer",
      "title": "Hosts",
      "description": "Number of hosts",
      "order": 8
    },
    "ip": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address",
      "order": 1
    },
    "ip_class": {
      "type": "string",
      "title": "IP Class",
      "description": "IP class",
      "order": 6
    },
    "netmask": {
      "type": "string",
      "title": "Netmask",
      "description": "Subnet mask",
      "order": 2
    },
    "subnet_id": {
      "type": "string",
      "title": "Subnet ID",
      "description": "Subnet ID",
      "order": 9
    },
    "subnets": {
      "type": "integer",
      "title": "Subnets",
      "description": "Number of subnetworks",
      "order": 7
    },
    "wildcard": {
      "type": "string",
      "title": "Wildcard",
      "description": "Wildcard mask",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)