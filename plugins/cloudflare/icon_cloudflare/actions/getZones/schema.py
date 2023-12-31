# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List your zones using different filters"


class Input:
    ACCOUNTID = "accountId"
    ACCOUNTNAME = "accountName"
    DIRECTION = "direction"
    MATCH = "match"
    NAME = "name"
    ORDER = "order"
    PAGE = "page"
    PERPAGE = "perPage"
    STATUS = "status"
    

class Output:
    ZONES = "zones"
    

class GetZonesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "accountId": {
      "type": "string",
      "title": "Account ID",
      "description": "Identifier of the account",
      "order": 4
    },
    "accountName": {
      "type": "string",
      "title": "Account Name",
      "description": "Name of the account",
      "order": 3
    },
    "direction": {
      "type": "string",
      "title": "Direction",
      "description": "Direction to order results",
      "default": "desc",
      "enum": [
        "desc",
        "asc"
      ],
      "order": 9
    },
    "match": {
      "type": "string",
      "title": "Match",
      "description": "Whether to match all search requirements or at least one (any)",
      "default": "all",
      "enum": [
        "all",
        "any"
      ],
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the domain",
      "order": 2
    },
    "order": {
      "type": "string",
      "title": "Order",
      "description": "Field to order zones by",
      "default": "name",
      "enum": [
        "account ID",
        "account name",
        "name",
        "status"
      ],
      "order": 8
    },
    "page": {
      "type": "integer",
      "title": "Page",
      "description": "Page number of paginated results",
      "order": 6
    },
    "perPage": {
      "type": "integer",
      "title": "Per Page",
      "description": "Maximum number of results per page",
      "order": 7
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the zone",
      "default": "all",
      "enum": [
        "all",
        "active",
        "pending",
        "initializing",
        "moved",
        "deleted",
        "deactivated"
      ],
      "order": 5
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetZonesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "zones": {
      "type": "array",
      "title": "Zones",
      "description": "List of zones for given filters",
      "items": {
        "$ref": "#/definitions/zone"
      },
      "order": 1
    }
  },
  "definitions": {
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "customCertificateQuota": {
          "type": "integer",
          "title": "Custom Certificate Quota",
          "description": "Custom certificate quota",
          "order": 2
        },
        "multipleRailgunsAllowed": {
          "type": "boolean",
          "title": "Multiple Railguns Allowed",
          "description": "Multiple railguns allowed",
          "order": 5
        },
        "pageRuleQuota": {
          "type": "integer",
          "title": "Page Rule Quota",
          "description": "Page rule quota",
          "order": 3
        },
        "phishingDetected": {
          "type": "boolean",
          "title": "Phishing Detected",
          "description": "Phishing detected",
          "order": 4
        },
        "step": {
          "type": "integer",
          "title": "Step",
          "description": "Step",
          "order": 1
        }
      }
    },
    "owner": {
      "type": "object",
      "title": "owner",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 2
        }
      }
    },
    "plan": {
      "type": "object",
      "title": "plan",
      "properties": {
        "canSubscribe": {
          "type": "boolean",
          "title": "Can Subscribe",
          "description": "Can subscribe",
          "order": 7
        },
        "currency": {
          "type": "string",
          "title": "Currency",
          "description": "Currency",
          "order": 4
        },
        "externallyManaged": {
          "type": "boolean",
          "title": "Externally Managed",
          "description": "Externally managed",
          "order": 10
        },
        "frequency": {
          "type": "string",
          "title": "Frequency",
          "description": "Frequency",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "isSubscribed": {
          "type": "boolean",
          "title": "Is Subscribed",
          "description": "Is subscribed",
          "order": 6
        },
        "legacyDiscount": {
          "type": "boolean",
          "title": "Legacy Discount",
          "description": "Legacy discount",
          "order": 9
        },
        "legacyId": {
          "type": "string",
          "title": "Legacy ID",
          "description": "Legacy ID",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "price": {
          "type": "integer",
          "title": "Price",
          "description": "Price",
          "order": 3
        }
      }
    },
    "tenant": {
      "type": "object",
      "title": "tenant",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Identifier",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        }
      }
    },
    "tenantUnit": {
      "type": "object",
      "title": "tenantUnit",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Identifier",
          "order": 1
        }
      }
    },
    "zone": {
      "type": "object",
      "title": "zone",
      "properties": {
        "account": {
          "$ref": "#/definitions/tenant",
          "title": "Account",
          "description": "Account",
          "order": 16
        },
        "activatedOn": {
          "type": "string",
          "title": "Activated On",
          "description": "Activated on",
          "order": 13
        },
        "createdOn": {
          "type": "string",
          "title": "Created On",
          "description": "Created on",
          "order": 11
        },
        "developmentMode": {
          "type": "integer",
          "title": "Development Mode",
          "description": "Development mode",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "Zone ID",
          "description": "Identifier of the zone",
          "order": 1
        },
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Meta",
          "description": "Meta",
          "order": 14
        },
        "modifiedOn": {
          "type": "string",
          "title": "Modified On",
          "description": "Modified on",
          "order": 12
        },
        "name": {
          "type": "string",
          "title": "Zone Name",
          "description": "Name of the zone",
          "order": 2
        },
        "nameServers": {
          "type": "array",
          "title": "Name Servers",
          "description": "Name servers",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "originalDnshost": {
          "type": "string",
          "title": "Original DNS Host",
          "description": "Original DNS host",
          "order": 10
        },
        "originalNameServers": {
          "type": "array",
          "title": "Original Name Servers",
          "description": "Original name servers",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "originalRegistrar": {
          "type": "string",
          "title": "Original Registrar",
          "description": "Original registrar",
          "order": 9
        },
        "owner": {
          "$ref": "#/definitions/owner",
          "title": "Owner",
          "description": "Owner",
          "order": 15
        },
        "paused": {
          "type": "boolean",
          "title": "Paused",
          "description": "Paused",
          "order": 4
        },
        "permissions": {
          "type": "array",
          "title": "Permissions",
          "description": "Permissions",
          "items": {
            "type": "string"
          },
          "order": 19
        },
        "plan": {
          "$ref": "#/definitions/plan",
          "title": "Plan",
          "description": "Plan",
          "order": 20
        },
        "status": {
          "type": "string",
          "title": "Zone Status",
          "description": "Status of the zone",
          "order": 3
        },
        "tenant": {
          "$ref": "#/definitions/tenant",
          "title": "Tenant",
          "description": "Tenant",
          "order": 17
        },
        "tenantUnit": {
          "$ref": "#/definitions/tenantUnit",
          "title": "Tenant Unit",
          "description": "Tenant unit",
          "order": 18
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the zone",
          "order": 5
        }
      },
      "definitions": {
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "customCertificateQuota": {
              "type": "integer",
              "title": "Custom Certificate Quota",
              "description": "Custom certificate quota",
              "order": 2
            },
            "multipleRailgunsAllowed": {
              "type": "boolean",
              "title": "Multiple Railguns Allowed",
              "description": "Multiple railguns allowed",
              "order": 5
            },
            "pageRuleQuota": {
              "type": "integer",
              "title": "Page Rule Quota",
              "description": "Page rule quota",
              "order": 3
            },
            "phishingDetected": {
              "type": "boolean",
              "title": "Phishing Detected",
              "description": "Phishing detected",
              "order": 4
            },
            "step": {
              "type": "integer",
              "title": "Step",
              "description": "Step",
              "order": 1
            }
          }
        },
        "owner": {
          "type": "object",
          "title": "owner",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "Email",
              "order": 3
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 2
            }
          }
        },
        "plan": {
          "type": "object",
          "title": "plan",
          "properties": {
            "canSubscribe": {
              "type": "boolean",
              "title": "Can Subscribe",
              "description": "Can subscribe",
              "order": 7
            },
            "currency": {
              "type": "string",
              "title": "Currency",
              "description": "Currency",
              "order": 4
            },
            "externallyManaged": {
              "type": "boolean",
              "title": "Externally Managed",
              "description": "Externally managed",
              "order": 10
            },
            "frequency": {
              "type": "string",
              "title": "Frequency",
              "description": "Frequency",
              "order": 5
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "isSubscribed": {
              "type": "boolean",
              "title": "Is Subscribed",
              "description": "Is subscribed",
              "order": 6
            },
            "legacyDiscount": {
              "type": "boolean",
              "title": "Legacy Discount",
              "description": "Legacy discount",
              "order": 9
            },
            "legacyId": {
              "type": "string",
              "title": "Legacy ID",
              "description": "Legacy ID",
              "order": 8
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "price": {
              "type": "integer",
              "title": "Price",
              "description": "Price",
              "order": 3
            }
          }
        },
        "tenant": {
          "type": "object",
          "title": "tenant",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Identifier",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            }
          }
        },
        "tenantUnit": {
          "type": "object",
          "title": "tenantUnit",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Identifier",
              "order": 1
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
