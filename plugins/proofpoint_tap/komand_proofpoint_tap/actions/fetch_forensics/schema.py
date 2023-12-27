# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch Forensics allows users to pull detailed forensic evidence about individual threats or campaigns"


class Input:
    CAMPAIGNID = "campaignId"
    INCLUDECAMPAIGNFORENSICS = "includeCampaignForensics"
    THREATID = "threatId"
    

class Output:
    GENERATED = "generated"
    REPORTS = "reports"
    

class FetchForensicsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "campaignId": {
      "type": "string",
      "title": "Campaign ID",
      "description": "Campaign identifier",
      "order": 2
    },
    "includeCampaignForensics": {
      "type": "boolean",
      "title": "Include Campaign Forensics",
      "description": "Include campaign forensics in threats. This parameter works only with Threat ID",
      "order": 3
    },
    "threatId": {
      "type": "string",
      "title": "Threat ID",
      "description": "Threat identifier",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FetchForensicsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "generated": {
      "type": "string",
      "title": "Generated",
      "description": "ISO8601-formatted datetime corresponding to the time this report was generated",
      "order": 1
    },
    "reports": {
      "type": "array",
      "title": "Reports",
      "description": "Reported threats",
      "items": {
        "$ref": "#/definitions/report"
      },
      "order": 2
    }
  },
  "required": [
    "generated",
    "reports"
  ],
  "definitions": {
    "evidence": {
      "type": "object",
      "title": "evidence",
      "properties": {
        "display": {
          "type": "string",
          "title": "Display",
          "description": "Friendly display string",
          "order": 2
        },
        "malicious": {
          "type": "boolean",
          "title": "Malicious",
          "description": "Whether the evidence was used to reach a malicious verdict",
          "order": 3
        },
        "platforms": {
          "type": "array",
          "title": "Platforms",
          "description": "Array of Platform objects",
          "items": {
            "$ref": "#/definitions/platform"
          },
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The evidence type",
          "order": 1
        },
        "what": {
          "$ref": "#/definitions/evidenceType",
          "title": "What",
          "description": "Map of values associated with the specific evidence type",
          "order": 4
        }
      },
      "definitions": {
        "evidenceType": {
          "type": "object",
          "title": "evidenceType",
          "properties": {
            "action": {
              "type": "string",
              "title": "Action",
              "description": "Action performed",
              "order": 7
            },
            "blacklisted": {
              "type": "boolean",
              "title": "Blacklisted",
              "description": "Optional, whether the file or URL was blacklisted",
              "order": 2
            },
            "cnames": {
              "type": "array",
              "title": "Canonical Names",
              "description": "Optional, an array of CNAMEs which were associated with the hostname",
              "items": {
                "type": "string"
              },
              "order": 12
            },
            "domain": {
              "type": "string",
              "title": "Domain",
              "description": "Which domain set the cookie",
              "order": 8
            },
            "host": {
              "type": "string",
              "title": "Host",
              "description": "The hostname being resolved",
              "order": 11
            },
            "httpStatus": {
              "type": "integer",
              "title": "HTTP Status",
              "description": "Optional, the HTTP status code which was produced when our sandbox visited the URL",
              "order": 23
            },
            "ip": {
              "type": "string",
              "title": "Remote IP Address",
              "description": "The remote IP address being contacted",
              "order": 20
            },
            "ips": {
              "type": "array",
              "title": "Resolved IP Addresses",
              "description": "Optional, an array of IP addresses which were resolved to the hostname",
              "items": {
                "type": "string"
              },
              "order": 13
            },
            "key": {
              "type": "string",
              "title": "Key",
              "description": "The location of the registry key being modified or the name of the cookie being set or deleted",
              "order": 9
            },
            "md5": {
              "type": "string",
              "title": "MD5",
              "description": "Optional, the MD5 sum of the item's content",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the related item",
              "order": 18
            },
            "nameservers": {
              "type": "array",
              "title": "Nameservers",
              "description": "Optional, the nameservers responsible for the hostname's domain",
              "items": {
                "type": "string"
              },
              "order": 14
            },
            "nameserversList": {
              "type": "array",
              "title": "Nameservers List",
              "description": "Optional, the nameservers responsible for the hostname's domain",
              "items": {
                "type": "string"
              },
              "order": 15
            },
            "offset": {
              "type": "integer",
              "title": "Offset",
              "description": "Optional, the offset in bytes where the malicious content or URL was found",
              "order": 4
            },
            "path": {
              "type": "string",
              "title": "Path",
              "description": "Path to the file",
              "order": 16
            },
            "port": {
              "type": "integer",
              "title": "Port",
              "description": "The remote IP port being contacted",
              "order": 21
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "description": "Optional, the name of the static rule inside the sandbox which identified the related item",
              "order": 5
            },
            "sha256": {
              "type": "string",
              "title": "SHA256",
              "description": "The SHA256 hash of the item's content",
              "order": 1
            },
            "signatureId": {
              "type": "integer",
              "title": "Signature ID",
              "description": "The identifier of the IDs rule which observed the malicious traffic",
              "order": 19
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "description": "Optional, the size in bytes of the file content",
              "order": 6
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The protocol being used - TCP or UDP",
              "order": 22
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "URL",
              "order": 17
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "The content of the cookie or registry key being set",
              "order": 10
            }
          }
        },
        "platform": {
          "type": "object",
          "title": "platform",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of platform",
              "order": 1
            },
            "os": {
              "type": "string",
              "title": "OS",
              "description": "Operating system",
              "order": 2
            },
            "version": {
              "type": "string",
              "title": "Version",
              "description": "Version of operating system",
              "order": 3
            }
          }
        }
      }
    },
    "evidenceType": {
      "type": "object",
      "title": "evidenceType",
      "properties": {
        "action": {
          "type": "string",
          "title": "Action",
          "description": "Action performed",
          "order": 7
        },
        "blacklisted": {
          "type": "boolean",
          "title": "Blacklisted",
          "description": "Optional, whether the file or URL was blacklisted",
          "order": 2
        },
        "cnames": {
          "type": "array",
          "title": "Canonical Names",
          "description": "Optional, an array of CNAMEs which were associated with the hostname",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "Which domain set the cookie",
          "order": 8
        },
        "host": {
          "type": "string",
          "title": "Host",
          "description": "The hostname being resolved",
          "order": 11
        },
        "httpStatus": {
          "type": "integer",
          "title": "HTTP Status",
          "description": "Optional, the HTTP status code which was produced when our sandbox visited the URL",
          "order": 23
        },
        "ip": {
          "type": "string",
          "title": "Remote IP Address",
          "description": "The remote IP address being contacted",
          "order": 20
        },
        "ips": {
          "type": "array",
          "title": "Resolved IP Addresses",
          "description": "Optional, an array of IP addresses which were resolved to the hostname",
          "items": {
            "type": "string"
          },
          "order": 13
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "The location of the registry key being modified or the name of the cookie being set or deleted",
          "order": 9
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "Optional, the MD5 sum of the item's content",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the related item",
          "order": 18
        },
        "nameservers": {
          "type": "array",
          "title": "Nameservers",
          "description": "Optional, the nameservers responsible for the hostname's domain",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "nameserversList": {
          "type": "array",
          "title": "Nameservers List",
          "description": "Optional, the nameservers responsible for the hostname's domain",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "offset": {
          "type": "integer",
          "title": "Offset",
          "description": "Optional, the offset in bytes where the malicious content or URL was found",
          "order": 4
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "Path to the file",
          "order": 16
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "The remote IP port being contacted",
          "order": 21
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "description": "Optional, the name of the static rule inside the sandbox which identified the related item",
          "order": 5
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "The SHA256 hash of the item's content",
          "order": 1
        },
        "signatureId": {
          "type": "integer",
          "title": "Signature ID",
          "description": "The identifier of the IDs rule which observed the malicious traffic",
          "order": 19
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "Optional, the size in bytes of the file content",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The protocol being used - TCP or UDP",
          "order": 22
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 17
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "The content of the cookie or registry key being set",
          "order": 10
        }
      }
    },
    "platform": {
      "type": "object",
      "title": "platform",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of platform",
          "order": 1
        },
        "os": {
          "type": "string",
          "title": "OS",
          "description": "Operating system",
          "order": 2
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version of operating system",
          "order": 3
        }
      }
    },
    "report": {
      "type": "object",
      "title": "report",
      "properties": {
        "forensics": {
          "type": "array",
          "title": "Forensics",
          "description": "Array of Evidence objects",
          "items": {
            "$ref": "#/definitions/evidence"
          },
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The identifier associated with the campaign or individual threat",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The malicious URL, SHA256 hash of the malicious attachment, or campaign name",
          "order": 1
        },
        "scope": {
          "type": "string",
          "title": "Scope",
          "description": "Whether the report scope covers a campaign or an individual threat",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The threat type",
          "order": 3
        }
      },
      "definitions": {
        "evidence": {
          "type": "object",
          "title": "evidence",
          "properties": {
            "display": {
              "type": "string",
              "title": "Display",
              "description": "Friendly display string",
              "order": 2
            },
            "malicious": {
              "type": "boolean",
              "title": "Malicious",
              "description": "Whether the evidence was used to reach a malicious verdict",
              "order": 3
            },
            "platforms": {
              "type": "array",
              "title": "Platforms",
              "description": "Array of Platform objects",
              "items": {
                "$ref": "#/definitions/platform"
              },
              "order": 5
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The evidence type",
              "order": 1
            },
            "what": {
              "$ref": "#/definitions/evidenceType",
              "title": "What",
              "description": "Map of values associated with the specific evidence type",
              "order": 4
            }
          },
          "definitions": {
            "evidenceType": {
              "type": "object",
              "title": "evidenceType",
              "properties": {
                "action": {
                  "type": "string",
                  "title": "Action",
                  "description": "Action performed",
                  "order": 7
                },
                "blacklisted": {
                  "type": "boolean",
                  "title": "Blacklisted",
                  "description": "Optional, whether the file or URL was blacklisted",
                  "order": 2
                },
                "cnames": {
                  "type": "array",
                  "title": "Canonical Names",
                  "description": "Optional, an array of CNAMEs which were associated with the hostname",
                  "items": {
                    "type": "string"
                  },
                  "order": 12
                },
                "domain": {
                  "type": "string",
                  "title": "Domain",
                  "description": "Which domain set the cookie",
                  "order": 8
                },
                "host": {
                  "type": "string",
                  "title": "Host",
                  "description": "The hostname being resolved",
                  "order": 11
                },
                "httpStatus": {
                  "type": "integer",
                  "title": "HTTP Status",
                  "description": "Optional, the HTTP status code which was produced when our sandbox visited the URL",
                  "order": 23
                },
                "ip": {
                  "type": "string",
                  "title": "Remote IP Address",
                  "description": "The remote IP address being contacted",
                  "order": 20
                },
                "ips": {
                  "type": "array",
                  "title": "Resolved IP Addresses",
                  "description": "Optional, an array of IP addresses which were resolved to the hostname",
                  "items": {
                    "type": "string"
                  },
                  "order": 13
                },
                "key": {
                  "type": "string",
                  "title": "Key",
                  "description": "The location of the registry key being modified or the name of the cookie being set or deleted",
                  "order": 9
                },
                "md5": {
                  "type": "string",
                  "title": "MD5",
                  "description": "Optional, the MD5 sum of the item's content",
                  "order": 3
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "The name of the related item",
                  "order": 18
                },
                "nameservers": {
                  "type": "array",
                  "title": "Nameservers",
                  "description": "Optional, the nameservers responsible for the hostname's domain",
                  "items": {
                    "type": "string"
                  },
                  "order": 14
                },
                "nameserversList": {
                  "type": "array",
                  "title": "Nameservers List",
                  "description": "Optional, the nameservers responsible for the hostname's domain",
                  "items": {
                    "type": "string"
                  },
                  "order": 15
                },
                "offset": {
                  "type": "integer",
                  "title": "Offset",
                  "description": "Optional, the offset in bytes where the malicious content or URL was found",
                  "order": 4
                },
                "path": {
                  "type": "string",
                  "title": "Path",
                  "description": "Path to the file",
                  "order": 16
                },
                "port": {
                  "type": "integer",
                  "title": "Port",
                  "description": "The remote IP port being contacted",
                  "order": 21
                },
                "rule": {
                  "type": "string",
                  "title": "Rule",
                  "description": "Optional, the name of the static rule inside the sandbox which identified the related item",
                  "order": 5
                },
                "sha256": {
                  "type": "string",
                  "title": "SHA256",
                  "description": "The SHA256 hash of the item's content",
                  "order": 1
                },
                "signatureId": {
                  "type": "integer",
                  "title": "Signature ID",
                  "description": "The identifier of the IDs rule which observed the malicious traffic",
                  "order": 19
                },
                "size": {
                  "type": "integer",
                  "title": "Size",
                  "description": "Optional, the size in bytes of the file content",
                  "order": 6
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "The protocol being used - TCP or UDP",
                  "order": 22
                },
                "url": {
                  "type": "string",
                  "title": "URL",
                  "description": "URL",
                  "order": 17
                },
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "The content of the cookie or registry key being set",
                  "order": 10
                }
              }
            },
            "platform": {
              "type": "object",
              "title": "platform",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name of platform",
                  "order": 1
                },
                "os": {
                  "type": "string",
                  "title": "OS",
                  "description": "Operating system",
                  "order": 2
                },
                "version": {
                  "type": "string",
                  "title": "Version",
                  "description": "Version of operating system",
                  "order": 3
                }
              }
            }
          }
        },
        "evidenceType": {
          "type": "object",
          "title": "evidenceType",
          "properties": {
            "action": {
              "type": "string",
              "title": "Action",
              "description": "Action performed",
              "order": 7
            },
            "blacklisted": {
              "type": "boolean",
              "title": "Blacklisted",
              "description": "Optional, whether the file or URL was blacklisted",
              "order": 2
            },
            "cnames": {
              "type": "array",
              "title": "Canonical Names",
              "description": "Optional, an array of CNAMEs which were associated with the hostname",
              "items": {
                "type": "string"
              },
              "order": 12
            },
            "domain": {
              "type": "string",
              "title": "Domain",
              "description": "Which domain set the cookie",
              "order": 8
            },
            "host": {
              "type": "string",
              "title": "Host",
              "description": "The hostname being resolved",
              "order": 11
            },
            "httpStatus": {
              "type": "integer",
              "title": "HTTP Status",
              "description": "Optional, the HTTP status code which was produced when our sandbox visited the URL",
              "order": 23
            },
            "ip": {
              "type": "string",
              "title": "Remote IP Address",
              "description": "The remote IP address being contacted",
              "order": 20
            },
            "ips": {
              "type": "array",
              "title": "Resolved IP Addresses",
              "description": "Optional, an array of IP addresses which were resolved to the hostname",
              "items": {
                "type": "string"
              },
              "order": 13
            },
            "key": {
              "type": "string",
              "title": "Key",
              "description": "The location of the registry key being modified or the name of the cookie being set or deleted",
              "order": 9
            },
            "md5": {
              "type": "string",
              "title": "MD5",
              "description": "Optional, the MD5 sum of the item's content",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the related item",
              "order": 18
            },
            "nameservers": {
              "type": "array",
              "title": "Nameservers",
              "description": "Optional, the nameservers responsible for the hostname's domain",
              "items": {
                "type": "string"
              },
              "order": 14
            },
            "nameserversList": {
              "type": "array",
              "title": "Nameservers List",
              "description": "Optional, the nameservers responsible for the hostname's domain",
              "items": {
                "type": "string"
              },
              "order": 15
            },
            "offset": {
              "type": "integer",
              "title": "Offset",
              "description": "Optional, the offset in bytes where the malicious content or URL was found",
              "order": 4
            },
            "path": {
              "type": "string",
              "title": "Path",
              "description": "Path to the file",
              "order": 16
            },
            "port": {
              "type": "integer",
              "title": "Port",
              "description": "The remote IP port being contacted",
              "order": 21
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "description": "Optional, the name of the static rule inside the sandbox which identified the related item",
              "order": 5
            },
            "sha256": {
              "type": "string",
              "title": "SHA256",
              "description": "The SHA256 hash of the item's content",
              "order": 1
            },
            "signatureId": {
              "type": "integer",
              "title": "Signature ID",
              "description": "The identifier of the IDs rule which observed the malicious traffic",
              "order": 19
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "description": "Optional, the size in bytes of the file content",
              "order": 6
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The protocol being used - TCP or UDP",
              "order": 22
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "URL",
              "order": 17
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "The content of the cookie or registry key being set",
              "order": 10
            }
          }
        },
        "platform": {
          "type": "object",
          "title": "platform",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of platform",
              "order": 1
            },
            "os": {
              "type": "string",
              "title": "OS",
              "description": "Operating system",
              "order": 2
            },
            "version": {
              "type": "string",
              "title": "Version",
              "description": "Version of operating system",
              "order": 3
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)