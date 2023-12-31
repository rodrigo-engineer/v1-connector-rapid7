# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search a domain for malicious threats"


class Input:
    DOMAIN = "domain"
    

class Output:
    DOMAINS = "domains"
    EMAILS = "emails"
    FOUND = "found"
    HASHES = "hashes"
    MALICIOUS = "malicious"
    PERMALINK = "permalink"
    REFERENCES = "references"
    SUBDOMAINS = "subdomains"
    

class DomainInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain to search",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domains": {
      "type": "array",
      "title": "Domains",
      "description": "List of domains",
      "items": {
        "$ref": "#/definitions/resolutions"
      },
      "order": 1
    },
    "emails": {
      "type": "array",
      "title": "Emails",
      "description": "List of emails",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether search returned results",
      "order": 8
    },
    "hashes": {
      "type": "array",
      "title": "Hashes",
      "description": "List of hashes",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "malicious": {
      "type": "string",
      "title": "Malicious",
      "description": "Category",
      "order": 6
    },
    "permalink": {
      "type": "string",
      "title": "Permalink",
      "description": "Permalink URL",
      "order": 7
    },
    "references": {
      "type": "array",
      "title": "References",
      "description": "List of references",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "subdomains": {
      "type": "array",
      "title": "Sub Domains",
      "description": "List of subdomains",
      "items": {
        "type": "string"
      },
      "order": 4
    }
  },
  "required": [
    "found"
  ],
  "definitions": {
    "resolutions": {
      "type": "object",
      "title": "resolutions",
      "properties": {
        "ip_address": {
          "type": "string",
          "title": "IP Address",
          "description": "IP address",
          "order": 1
        },
        "last_resolved": {
          "type": "string",
          "title": "Last Resolved",
          "description": "Last resolved",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
