# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve ThreatConnect emails"


class Input:
    ADVERSARY_ID = "adversary_id"
    DOCUMENT_ID = "document_id"
    EMAIL_ID = "email_id"
    ID = "id"
    INCIDENT_ID = "incident_id"
    INDICATOR = "indicator"
    OWNER = "owner"
    SECURITY_LABEL = "security_label"
    SIGNATURE_ID = "signature_id"
    TAG = "tag"
    THREAT_ID = "threat_id"
    

class Output:
    EMAILS = "emails"
    

class EmailsRetrieveInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "adversary_id": {
      "type": "integer",
      "title": "Adversary ID",
      "description": "Filter Groups on associated Adversary ID",
      "order": 1
    },
    "document_id": {
      "type": "integer",
      "title": "Document ID",
      "description": "Filter Groups on associated Document ID",
      "order": 4
    },
    "email_id": {
      "type": "integer",
      "title": "Email ID",
      "description": "Filter Groups on associated Email ID",
      "order": 2
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Filter Groups on associated ID",
      "order": 3
    },
    "incident_id": {
      "type": "integer",
      "title": "Incident ID",
      "description": "Filter Groups on associated Incident ID",
      "order": 5
    },
    "indicator": {
      "type": "string",
      "title": "Indicator",
      "description": "Filter Groups on associated Indicator",
      "order": 6
    },
    "owner": {
      "type": "string",
      "title": "Owner",
      "description": "Owner/Organization",
      "order": 11
    },
    "security_label": {
      "type": "string",
      "title": "Security Label",
      "description": "Filter Groups on associated Security Label",
      "order": 7
    },
    "signature_id": {
      "type": "integer",
      "title": "Signature ID",
      "description": "Filter Groups on applied Security Label",
      "order": 8
    },
    "tag": {
      "type": "string",
      "title": "Tag",
      "description": "Filter Groups on applied Tag",
      "order": 10
    },
    "threat_id": {
      "type": "integer",
      "title": "Threat ID",
      "description": "Filter Groups on associated Threat ID",
      "order": 9
    }
  },
  "required": [
    "owner"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EmailsRetrieveOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "emails": {
      "type": "array",
      "title": "Emails",
      "description": "Emails",
      "items": {
        "$ref": "#/definitions/email_output"
      },
      "order": 1
    }
  },
  "definitions": {
    "email_output": {
      "type": "object",
      "title": "email_output",
      "properties": {
        "body": {
          "type": "string",
          "title": "Body",
          "order": 9
        },
        "date_added": {
          "type": "string",
          "title": "Date Added",
          "displayType": "date",
          "format": "date-time",
          "order": 3
        },
        "from_address": {
          "type": "string",
          "title": "From Address",
          "order": 7
        },
        "header": {
          "type": "string",
          "title": "Header",
          "order": 5
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "score": {
          "type": "string",
          "title": "Score",
          "order": 10
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "order": 6
        },
        "to": {
          "type": "string",
          "title": "To",
          "order": 8
        },
        "weblink": {
          "type": "string",
          "title": "Weblink",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
