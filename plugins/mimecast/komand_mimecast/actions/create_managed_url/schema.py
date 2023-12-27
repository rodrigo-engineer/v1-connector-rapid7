# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a managed URL"


class Input:
    ACTION = "action"
    COMMENT = "comment"
    DISABLE_LOG_CLICK = "disable_log_click"
    DISABLE_REWRITE = "disable_rewrite"
    DISABLE_USER_AWARENESS = "disable_user_awareness"
    MATCH_TYPE = "match_type"
    URL = "url"


class Output:
    RESPONSE = "response"


class CreateManagedUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Set to 'block' to blacklist the URL, 'permit' to whitelist it",
      "default": "block",
      "enum": [
        "block",
        "permit"
      ],
      "order": 6
    },
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "A comment about the why the URL is managed; for tracking purposes",
      "order": 2
    },
    "disable_log_click": {
      "type": "boolean",
      "title": "Disable Log Click",
      "description": "Disable logging of user clicks on the URL",
      "order": 5
    },
    "disable_rewrite": {
      "type": "boolean",
      "title": "Disable Rewrite",
      "description": "Disable rewriting of this URL in emails. Applies only if action = 'permit'",
      "order": 3
    },
    "disable_user_awareness": {
      "type": "boolean",
      "title": "Disable User Awareness",
      "description": "Disable User Awareness challenges for this URL. Applies only if action = 'permit'",
      "order": 4
    },
    "match_type": {
      "type": "string",
      "title": "Match Type",
      "description": "Set to 'explicit' to block or permit only instances of the full URL. Set to 'domain' to block or permit any URL with the same domain",
      "default": "explicit",
      "enum": [
        "explicit",
        "domain"
      ],
      "order": 7
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "The URL to block or permit. Do not include a fragment",
      "order": 1
    }
  },
  "required": [
    "action",
    "disable_log_click",
    "disable_rewrite",
    "disable_user_awareness",
    "match_type",
    "url"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateManagedUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "type": "array",
      "title": "Managed URL",
      "description": "Managed URL that was created",
      "items": {
        "$ref": "#/definitions/managed_url"
      },
      "order": 1
    }
  },
  "definitions": {
    "managed_url": {
      "type": "object",
      "title": "managed_url",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast secure ID of the managed URL",
          "order": 1
        },
        "scheme": {
          "type": "string",
          "title": "Scheme",
          "description": "The protocol to apply for the managed URL. Either HTTP or HTTPS",
          "order": 2
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The managed domain",
          "order": 3
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "The specified in the managed URL. Default value is -1 if no port was provided",
          "order": 4
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "The resource path of the managed URL",
          "order": 5
        },
        "queryString": {
          "type": "string",
          "title": "Query string",
          "description": "The query string of the managed URL",
          "order": 6
        },
        "matchType": {
          "type": "string",
          "title": "Match Type",
          "description": "The type of URL to match against",
          "order": 7
        },
        "action": {
          "type": "string",
          "title": "Action",
          "description": "Action to take for when URL is clicked. Either block or permit",
          "order": 8
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "The comment that was posted in the request",
          "order": 9
        },
        "disableUserAwareness": {
          "type": "boolean",
          "title": "User Awareness",
          "description": "If User Awareness challenges for this URL are disabled",
          "order": 10
        },
        "disableLogClick": {
          "type": "boolean",
          "title": "Click Logging",
          "description": "If logging of user clicks on the URL is disabled",
          "order": 11
        },
        "disableRewrite": {
          "type": "boolean",
          "title": "URL Rewriting",
          "description": "If rewriting of this URL in emails is disabled",
          "order": 12
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)