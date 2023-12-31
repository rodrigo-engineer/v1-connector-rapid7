# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search a hash string for malicious threats"


class Input:
    HASH = "hash"
    

class Output:
    DOMAINS = "domains"
    FOUND = "found"
    HASHES = "hashes"
    IPS = "ips"
    PERMALINK = "permalink"
    REFERENCES = "references"
    SCANS = "scans"
    

class HashInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Search Hash",
      "description": "Hash to search - MD5 and SHA1 supported",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class HashOutput(insightconnect_plugin_runtime.Output):
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
        "type": "string"
      },
      "order": 4
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether search returned results",
      "order": 7
    },
    "hashes": {
      "$ref": "#/definitions/hash",
      "title": "Hashes",
      "description": "List of hashes",
      "order": 2
    },
    "ips": {
      "type": "array",
      "title": "IPs",
      "description": "List of IP addresses",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "permalink": {
      "type": "string",
      "title": "Permalink",
      "description": "Permalink URL",
      "order": 6
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
    "scans": {
      "type": "array",
      "title": "Scans",
      "description": "List of scans",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "found"
  ],
  "definitions": {
    "hash": {
      "type": "object",
      "title": "hash",
      "properties": {
        "md5": {
          "type": "string",
          "title": "MD5 Hash",
          "description": "MD5 hash value",
          "order": 1
        },
        "sha1": {
          "type": "string",
          "title": "SHA1 Hash",
          "description": "SHA1 hash value",
          "order": 2
        }
      },
      "required": [
        "md5",
        "sha1"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
