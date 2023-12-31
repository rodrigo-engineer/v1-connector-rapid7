# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get policies"


class Input:
    NAME_FILTER = "name_filter"
    

class Output:
    POLICIES = "policies"
    

class GetPoliciesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name_filter": {
      "type": "string",
      "title": "Name Filter",
      "description": "Optional name to filter on",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPoliciesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "policies": {
      "type": "array",
      "title": "Policies",
      "description": "Policies",
      "items": {
        "$ref": "#/definitions/policies"
      },
      "order": 1
    }
  },
  "definitions": {
    "dstaddr": {
      "type": "object",
      "title": "dstaddr",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "q_origin_key": {
          "type": "string",
          "title": "Q Origin Key",
          "description": "Q origin key",
          "order": 1
        }
      }
    },
    "policies": {
      "type": "object",
      "title": "policies",
      "properties": {
        "action": {
          "type": "string",
          "title": "Action",
          "description": "Action",
          "order": 37
        },
        "anti-replay": {
          "type": "string",
          "title": "Anti-Replay",
          "description": "Anti-replay",
          "order": 23
        },
        "app-category": {
          "type": "array",
          "title": "App-Category",
          "description": "App-category",
          "items": {
            "type": "object"
          },
          "order": 91
        },
        "app-group": {
          "type": "array",
          "title": "App-Group",
          "description": "App-group",
          "items": {
            "type": "object"
          },
          "order": 63
        },
        "application": {
          "type": "array",
          "title": "Application",
          "description": "Application",
          "items": {
            "type": "object"
          },
          "order": 72
        },
        "auth-path": {
          "type": "string",
          "title": "Auth-Path",
          "description": "Auth-path",
          "order": 30
        },
        "auto-asic-offload": {
          "type": "string",
          "title": "Auto-ASIC-Offload",
          "description": "Auto-ASIC-offload",
          "order": 49
        },
        "block-notification": {
          "type": "string",
          "title": "Block-Notification",
          "description": "Block-notification",
          "order": 35
        },
        "captive-portal-exempt": {
          "type": "string",
          "title": "Captive-Portal-Exempt",
          "description": "Captive-portal-exempt",
          "order": 90
        },
        "capture-packet": {
          "type": "string",
          "title": "Capture-Packet",
          "description": "Capture-packet",
          "order": 51
        },
        "delay-tcp-npu-session": {
          "type": "string",
          "title": "Delay-TCP-Npu-Session",
          "description": "Delay-TCP-npu-session",
          "order": 89
        },
        "diffserv-forward": {
          "type": "string",
          "title": "Diffserv-Forward",
          "description": "Diffserv-forward",
          "order": 26
        },
        "diffserv-reverse": {
          "type": "string",
          "title": "Diffserv-Reverse",
          "description": "Diffserv-reverse",
          "order": 87
        },
        "diffservcode-forward": {
          "type": "string",
          "title": "Diffservcode-Forward",
          "description": "Diffservcode-forward",
          "order": 24
        },
        "diffservcode-rev": {
          "type": "string",
          "title": "Diffservcode-Rev",
          "description": "Diffservcode-rev",
          "order": 9
        },
        "disclaimer": {
          "type": "string",
          "title": "Disclaimer",
          "description": "Disclaimer",
          "order": 38
        },
        "dsri": {
          "type": "string",
          "title": "DSRI",
          "description": "DSRI",
          "order": 68
        },
        "dstaddr": {
          "type": "array",
          "title": "Dstaddr",
          "description": "Dstaddr",
          "items": {
            "$ref": "#/definitions/dstaddr"
          },
          "order": 95
        },
        "dstaddr-negate": {
          "type": "string",
          "title": "Dstaddr-Negate",
          "description": "Dstaddr-negate",
          "order": 39
        },
        "dstintf": {
          "type": "array",
          "title": "Dstintf",
          "description": "Dstintf",
          "items": {
            "$ref": "#/definitions/dstaddr"
          },
          "order": 33
        },
        "email-collect": {
          "type": "string",
          "title": "Email-Collect",
          "description": "Email-collect",
          "order": 83
        },
        "firewall-session-dirty": {
          "type": "string",
          "title": "Firewall-Session-Dirty",
          "description": "Firewall-session-dirty",
          "order": 27
        },
        "fixedport": {
          "type": "string",
          "title": "Fixed Port",
          "description": "Fixed port",
          "order": 67
        },
        "fsso": {
          "type": "string",
          "title": "FSSO",
          "description": "FSSO",
          "order": 76
        },
        "fsso-groups": {
          "type": "array",
          "title": "FSSO-Groups",
          "description": "FSSO-groups",
          "items": {
            "type": "object"
          },
          "order": 70
        },
        "geoip-anycast": {
          "type": "string",
          "title": "Geoip-Anycast",
          "description": "Geoip-anycast",
          "order": 82
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "Groups",
          "items": {
            "type": "object"
          },
          "order": 41
        },
        "http-policy-redirect": {
          "type": "string",
          "title": "HTTP-Policy-Redirect",
          "description": "HTTP-policy-redirect",
          "order": 19
        },
        "inbound": {
          "type": "string",
          "title": "Inbound",
          "description": "Inbound",
          "order": 54
        },
        "inspection-mode": {
          "type": "string",
          "title": "Inspection-Mode",
          "description": "Inspection-mode",
          "order": 57
        },
        "internet-service": {
          "type": "string",
          "title": "Internet-Service",
          "description": "Internet-service",
          "order": 53
        },
        "internet-service-custom": {
          "type": "array",
          "title": "Internet-Service-Custom",
          "description": "Internet-service-custom",
          "items": {
            "type": "object"
          },
          "order": 86
        },
        "internet-service-group": {
          "type": "array",
          "title": "Internet-Service-Group",
          "description": "Internet-service-group",
          "items": {
            "type": "object"
          },
          "order": 75
        },
        "internet-service-negate": {
          "type": "string",
          "title": "Internet-Service-Negate",
          "description": "Internet-service-negate",
          "order": 32
        },
        "internet-service-src": {
          "type": "string",
          "title": "Internet-Service-Src",
          "description": "Internet-service-src",
          "order": 42
        },
        "internet-service-src-group": {
          "type": "array",
          "title": "Internet-Service-Src-Group",
          "description": "Internet-service-src-group",
          "items": {
            "type": "object"
          },
          "order": 74
        },
        "internet-service-src-negate": {
          "type": "string",
          "title": "Internet-Service-Src-Negate",
          "description": "Internet-service-src-negate",
          "order": 60
        },
        "ippool": {
          "type": "string",
          "title": "IP Pool",
          "description": "IP pool",
          "order": 45
        },
        "logtraffic": {
          "type": "string",
          "title": "Log Traffic",
          "description": "Log Traffic",
          "order": 20
        },
        "logtraffic-start": {
          "type": "string",
          "title": "Logtraffic-Start",
          "description": "Logtraffic-start",
          "order": 40
        },
        "match-vip": {
          "type": "string",
          "title": "Match-VIP",
          "description": "Match-VIP",
          "order": 10
        },
        "match-vip-only": {
          "type": "string",
          "title": "Match-VIP-Only",
          "description": "Match-VIP-only",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 14
        },
        "nat": {
          "type": "string",
          "title": "NAT",
          "description": "NAT",
          "order": 73
        },
        "natinbound": {
          "type": "string",
          "title": "NAT Inbound",
          "description": "NAT inbound",
          "order": 66
        },
        "natip": {
          "type": "string",
          "title": "NAT IP",
          "description": "NAT IP",
          "order": 11
        },
        "natoutbound": {
          "type": "string",
          "title": "NAT Outbound",
          "description": "NAT outbound",
          "order": 18
        },
        "ntlm": {
          "type": "string",
          "title": "NTLM",
          "description": "NTLM",
          "order": 21
        },
        "ntlm-enabled-browsers": {
          "type": "array",
          "title": "NTLM-Enabled-Browsers",
          "description": "NTLM-enabled-browsers",
          "items": {
            "type": "object"
          },
          "order": 61
        },
        "ntlm-guest": {
          "type": "string",
          "title": "NTLM-Guest",
          "description": "NTLM-guest",
          "order": 7
        },
        "outbound": {
          "type": "string",
          "title": "Outbound",
          "description": "Outbound",
          "order": 69
        },
        "permit-any-host": {
          "type": "string",
          "title": "Permit-Any-Host",
          "description": "Permit-any-host",
          "order": 59
        },
        "permit-stun-host": {
          "type": "string",
          "title": "Permit-STUN-Host",
          "description": "Permit-STUN-host",
          "order": 17
        },
        "policyid": {
          "type": "integer",
          "title": "Policy ID",
          "description": "Policy ID",
          "order": 84
        },
        "profile-protocol-options": {
          "type": "string",
          "title": "Profile-Protocol-Options",
          "description": "Profile-protocol-options",
          "order": 81
        },
        "profile-type": {
          "type": "string",
          "title": "Profile-Type",
          "description": "Profile-type",
          "order": 55
        },
        "q_origin_key": {
          "type": "integer",
          "title": "Q Origin Key",
          "description": "Q origin key",
          "order": 80
        },
        "radius-mac-auth-bypass": {
          "type": "string",
          "title": "Radius-MAC-Auth-Bypass",
          "description": "Radius-MAC-auth-bypass",
          "order": 96
        },
        "reputation-direction": {
          "type": "string",
          "title": "Reputation-Direction",
          "description": "Reputation-direction",
          "order": 12
        },
        "reputation-minimum": {
          "type": "integer",
          "title": "Reputation-Minimum",
          "description": "Reputation-minimum",
          "order": 65
        },
        "rsso": {
          "type": "string",
          "title": "RSSO",
          "description": "RSSO",
          "order": 62
        },
        "rtp-addr": {
          "type": "array",
          "title": "Rtp-Addr",
          "description": "Rtp-addr",
          "items": {
            "type": "object"
          },
          "order": 92
        },
        "rtp-nat": {
          "type": "string",
          "title": "RTP-NAT",
          "description": "RTP-NAT",
          "order": 16
        },
        "schedule": {
          "type": "string",
          "title": "Schedule",
          "description": "Schedule",
          "order": 29
        },
        "schedule-timeout": {
          "type": "string",
          "title": "Schedule-Timeout",
          "description": "Schedule-timeout",
          "order": 13
        },
        "send-deny-packet": {
          "type": "string",
          "title": "Send-Deny-Packet",
          "description": "Send-deny-packet",
          "order": 58
        },
        "service": {
          "type": "array",
          "title": "Service",
          "description": "Service",
          "items": {
            "$ref": "#/definitions/dstaddr"
          },
          "order": 46
        },
        "service-negate": {
          "type": "string",
          "title": "Service-Negate",
          "description": "Service-negate",
          "order": 36
        },
        "session-ttl": {
          "type": "string",
          "title": "Session-TTL",
          "description": "Session-TTL",
          "order": 6
        },
        "srcaddr": {
          "type": "array",
          "title": "Srcaddr",
          "description": "Srcaddr",
          "items": {
            "$ref": "#/definitions/dstaddr"
          },
          "order": 88
        },
        "srcaddr-negate": {
          "type": "string",
          "title": "Srcaddr-Negate",
          "description": "Srcaddr-negate",
          "order": 50
        },
        "srcintf": {
          "type": "array",
          "title": "Srcintf",
          "description": "Srcintf",
          "items": {
            "$ref": "#/definitions/dstaddr"
          },
          "order": 34
        },
        "ssh-policy-redirect": {
          "type": "string",
          "title": "SSH-Policy-Redirect",
          "description": "SSH-policy-redirect",
          "order": 52
        },
        "ssl-mirror": {
          "type": "string",
          "title": "SSL-Mirror",
          "description": "SSL-mirror",
          "order": 56
        },
        "ssl-ssh-profile": {
          "type": "string",
          "title": "Ssl-Ssh-Profile",
          "description": "Ssl-ssh-profile",
          "order": 79
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 78
        },
        "tcp-mss-receiver": {
          "type": "integer",
          "title": "Tcp-Mss-Receiver",
          "description": "Tcp-mss-receiver",
          "order": 94
        },
        "tcp-mss-sender": {
          "type": "integer",
          "title": "TCP-Mss-Sender",
          "description": "TCP-mss-sender",
          "order": 64
        },
        "tcp-session-without-syn": {
          "type": "string",
          "title": "TCP-Session-Without-SYN",
          "description": "TCP-session-without-SYN",
          "order": 15
        },
        "timeout-send-rst": {
          "type": "string",
          "title": "Timeout-Send-RST",
          "description": "Timeout-send-RST",
          "order": 22
        },
        "tos": {
          "type": "string",
          "title": "TOS",
          "description": "TOS",
          "order": 48
        },
        "tos-mask": {
          "type": "string",
          "title": "TOS-Mask",
          "description": "TOS-mask",
          "order": 8
        },
        "tos-negate": {
          "type": "string",
          "title": "TOS-Negate",
          "description": "TOS-negate",
          "order": 85
        },
        "url-category": {
          "type": "array",
          "title": "URL-Category",
          "description": "URL-category",
          "items": {
            "type": "object"
          },
          "order": 71
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "Users",
          "items": {
            "type": "object"
          },
          "order": 25
        },
        "utm-status": {
          "type": "string",
          "title": "UTM-Status",
          "description": "UTM-status",
          "order": 44
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "UUID",
          "order": 4
        },
        "vlan-cos-fwd": {
          "type": "integer",
          "title": "Vlan-Cos-Fwd",
          "description": "Vlan-cos-fwd",
          "order": 31
        },
        "vlan-cos-rev": {
          "type": "integer",
          "title": "Vlan-Cos-Rev",
          "description": "Vlan-cos-rev",
          "order": 77
        },
        "wanopt": {
          "type": "string",
          "title": "WAN Option",
          "description": "WAN option",
          "order": 28
        },
        "wanopt-detection": {
          "type": "string",
          "title": "WAN opt-Detection",
          "description": "WAN opt-detection",
          "order": 2
        },
        "wanopt-passive-opt": {
          "type": "string",
          "title": "WAN opt-Passive-Opt",
          "description": "WAN opt-passive-opt",
          "order": 1
        },
        "wccp": {
          "type": "string",
          "title": "WCCP",
          "description": "WCCP",
          "order": 47
        },
        "webcache": {
          "type": "string",
          "title": "Webcache",
          "description": "Webcache",
          "order": 43
        },
        "webcache-https": {
          "type": "string",
          "title": "Web cache-https",
          "description": "Web cache-https",
          "order": 3
        },
        "wsso": {
          "type": "string",
          "title": "WSSO",
          "description": "WSSO",
          "order": 93
        }
      },
      "definitions": {
        "dstaddr": {
          "type": "object",
          "title": "dstaddr",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "q_origin_key": {
              "type": "string",
              "title": "Q Origin Key",
              "description": "Q origin key",
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
