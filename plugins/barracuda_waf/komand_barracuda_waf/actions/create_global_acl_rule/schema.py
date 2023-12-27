# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Adds a global ACL rule with the given values"


class Input:
    GLOBAL_ACL = "global_acl"
    POLICY_ID = "policy_id"
    

class Output:
    ID = "id"
    

class CreateGlobalAclRuleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "global_acl": {
      "$ref": "#/definitions/global_acl",
      "title": "Global Acl",
      "description": "Global ACL object",
      "order": 2
    },
    "policy_id": {
      "type": "string",
      "title": "Policy Id",
      "description": "ID of security policy",
      "order": 1
    }
  },
  "required": [
    "global_acl",
    "policy_id"
  ],
  "definitions": {
    "global_acl": {
      "type": "object",
      "title": "global_acl",
      "properties": {
        "action": {
          "type": "string",
          "title": "Action",
          "description": "The action to be taken on the request matching this URL",
          "order": 5
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Description about the global ACL rule",
          "order": 9
        },
        "deny_response": {
          "type": "string",
          "title": "Deny Response",
          "description": "The response to be sent to the client if the request is denied",
          "order": 6
        },
        "extended_match": {
          "type": "string",
          "title": "Extended Match",
          "description": "An expression that consists of a combination of HTTP headers and/or query string parameters. Updating extended match parameters value is shown in the example below",
          "order": 3
        },
        "extended_match_sequence": {
          "type": "integer",
          "title": "Extended Match Sequence",
          "description": "A number to indicate the order in which the extended match rule must be evaluated in the requests",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "A name for the URL ACL rule",
          "order": 1
        },
        "redirect_url": {
          "type": "string",
          "title": "Redirect Url",
          "description": "A URL to which a user should be redirected",
          "order": 8
        },
        "response_page": {
          "type": "string",
          "title": "Response Page",
          "description": "The response page to be sent to the client",
          "order": 7
        },
        "url_match": {
          "type": "string",
          "title": "Url Match",
          "description": "The URL to be matched to the URL in the request.  The URL should start with a / and can have at most one  * anywhere in the URL. A value of '/*' means that the access control rule (ACL) applies for all URLs in that domain",
          "order": 2
        }
      },
      "required": [
        "extended_match",
        "name",
        "url_match"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateGlobalAclRuleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Id",
      "description": "ACL rule ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
