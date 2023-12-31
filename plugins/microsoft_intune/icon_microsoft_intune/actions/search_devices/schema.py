# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search devices by device name, user ID, email address or device ID"


class Input:
    DEVICE = "device"


class Output:
    DEVICES = "devices"


class SearchDevicesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device": {
      "type": "string",
      "title": "Device",
      "description": "Search devices by either of - device name, user ID, email address, device ID",
      "order": 1
    }
  },
  "required": [
    "device"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchDevicesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "devices": {
      "type": "array",
      "title": "Devices",
      "description": "Devices details",
      "items": {
        "$ref": "#/definitions/device"
      },
      "order": 1
    }
  },
  "definitions": {
    "device": {
      "type": "object",
      "title": "device",
      "properties": {
        "@odata.type": {
          "type": "string",
          "title": "Odata Type",
          "description": "Odata type",
          "order": 1
        },
        "activationLockBypassCode": {
          "type": "string",
          "title": "Activation Lock Bypass Code",
          "description": "Activation lock bypass code",
          "order": 2
        },
        "androidSecurityPatchLevel": {
          "type": "string",
          "title": "Android Security Patch Level",
          "description": "Android security patch level",
          "order": 3
        },
        "azureADDeviceId": {
          "type": "string",
          "title": "Azure AD Device ID",
          "description": "Azure AD device ID",
          "order": 4
        },
        "azureADRegistered": {
          "type": "boolean",
          "title": "Azure AD Registered",
          "description": "Azure AD registered",
          "order": 5
        },
        "complianceGracePeriodExpirationDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Compliance Grace Period Expiration Date Time",
          "description": "Compliance grace period expiration date time",
          "order": 6
        },
        "complianceState": {
          "type": "string",
          "title": "Compliance State",
          "description": "Compliance state",
          "order": 7
        },
        "configurationManagerClientEnabledFeatures": {
          "$ref": "#/definitions/configurationManagerClientEnabledFeatures",
          "title": "Configuration Manager Client Enabled Features",
          "description": "Configuration manager client enabled features",
          "order": 8
        },
        "deviceActionResults": {
          "type": "array",
          "title": "Device Action Results",
          "description": "Device action results",
          "items": {
            "$ref": "#/definitions/deviceActionResults"
          },
          "order": 9
        },
        "deviceCategoryDisplayName": {
          "type": "string",
          "title": "Device Category Display Name",
          "description": "Device category display name",
          "order": 10
        },
        "deviceEnrollmentType": {
          "type": "string",
          "title": "Device Enrollment Type",
          "description": "Device enrollment type",
          "order": 11
        },
        "deviceHealthAttestationState": {
          "$ref": "#/definitions/deviceHealthAttestationState",
          "title": "Device Health Attestation State",
          "description": "Device health attestation state",
          "order": 12
        },
        "deviceName": {
          "type": "string",
          "title": "Device Name",
          "description": "Device name",
          "order": 13
        },
        "deviceRegistrationState": {
          "type": "string",
          "title": "Device Registration State",
          "description": "Device registration state",
          "order": 14
        },
        "easActivated": {
          "type": "boolean",
          "title": "EAS Activated",
          "description": "EAS activated",
          "order": 15
        },
        "easActivationDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "EAS Activation Date Time",
          "description": "EAS activation date time",
          "order": 16
        },
        "easDeviceId": {
          "type": "string",
          "title": "EAS Device ID",
          "description": "EAS device ID",
          "order": 17
        },
        "emailAddress": {
          "type": "string",
          "title": "Email Address",
          "description": "Email address",
          "order": 18
        },
        "enrolledDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Enrolled Date Time",
          "description": "Enrolled date time",
          "order": 19
        },
        "exchangeAccessState": {
          "type": "string",
          "title": "Exchange Access State",
          "description": "Exchange access state",
          "order": 20
        },
        "exchangeAccessStateReason": {
          "type": "string",
          "title": "Exchange Access State Reason",
          "description": "Exchange access state reason",
          "order": 21
        },
        "exchangeLastSuccessfulSyncDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Exchange Last Successful Sync Date Time",
          "description": "Exchange last successful sync date time",
          "order": 22
        },
        "freeStorageSpaceInBytes": {
          "type": "integer",
          "title": "Free Storage Space In Bytes",
          "description": "Free storage space in bytes",
          "order": 23
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 24
        },
        "imei": {
          "type": "string",
          "title": "IMEI",
          "description": "IMEI",
          "order": 25
        },
        "isEncrypted": {
          "type": "boolean",
          "title": "Is Encrypted",
          "description": "Is encrypted",
          "order": 26
        },
        "isSupervised": {
          "type": "boolean",
          "title": "Is Supervised",
          "description": "Is supervised",
          "order": 27
        },
        "jailBroken": {
          "type": "string",
          "title": "Jail Broken",
          "description": "Jail broken",
          "order": 28
        },
        "lastSyncDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Last Sync Date Time",
          "description": "Last sync date time",
          "order": 29
        },
        "managedDeviceName": {
          "type": "string",
          "title": "Managed Device Name",
          "description": "Managed device name",
          "order": 30
        },
        "managedDeviceOwnerType": {
          "type": "string",
          "title": "Managed Device Owner Type",
          "description": "Managed device owner type",
          "order": 31
        },
        "managementAgent": {
          "type": "string",
          "title": "Management Agent",
          "description": "Management agent",
          "order": 32
        },
        "manufacturer": {
          "type": "string",
          "title": "Manufacturer",
          "description": "Manufacturer",
          "order": 33
        },
        "meid": {
          "type": "string",
          "title": "MEID",
          "description": "MEID",
          "order": 34
        },
        "model": {
          "type": "string",
          "title": "Model",
          "description": "Model",
          "order": 35
        },
        "operatingSystem": {
          "type": "string",
          "title": "Operating System",
          "description": "Operating system",
          "order": 36
        },
        "osVersion": {
          "type": "string",
          "title": "OS Version",
          "description": "OS version",
          "order": 37
        },
        "partnerReportedThreatState": {
          "type": "string",
          "title": "Partner Reported Threat State",
          "description": "Partner reported threat state",
          "order": 38
        },
        "phoneNumber": {
          "type": "string",
          "title": "Phone Number",
          "description": "Phone number",
          "order": 39
        },
        "remoteAssistanceSessionErrorDetails": {
          "type": "string",
          "title": "Remote Assistance Session Error Details",
          "description": "Remote assistance session error details",
          "order": 40
        },
        "remoteAssistanceSessionUrl": {
          "type": "string",
          "title": "Remote Assistance Session URL",
          "description": "Remote assistance session URL",
          "order": 41
        },
        "serialNumber": {
          "type": "string",
          "title": "Serial Number",
          "description": "Serial number",
          "order": 42
        },
        "subscriberCarrier": {
          "type": "string",
          "title": "Subscriber Carrier",
          "description": "Subscriber carrier",
          "order": 43
        },
        "totalStorageSpaceInBytes": {
          "type": "integer",
          "title": "Total Storage Space In Bytes",
          "description": "Total storage space in bytes",
          "order": 44
        },
        "userDisplayName": {
          "type": "string",
          "title": "User Display Name",
          "description": "User display name",
          "order": 45
        },
        "userId": {
          "type": "string",
          "title": "User ID",
          "description": "User ID",
          "order": 46
        },
        "userPrincipalName": {
          "type": "string",
          "title": "User Principal Name",
          "description": "User principal name",
          "order": 47
        },
        "wiFiMacAddress": {
          "type": "string",
          "title": "Wifi MAC Address",
          "description": "Wifi MAC address",
          "order": 48
        }
      }
    },
    "configurationManagerClientEnabledFeatures": {
      "type": "object",
      "title": "configurationManagerClientEnabledFeatures",
      "properties": {
        "@odata.type": {
          "type": "string",
          "title": "Odata Type",
          "description": "Odata type",
          "order": 1
        },
        "compliancePolicy": {
          "type": "boolean",
          "title": "Compliance Policy",
          "description": "Compliance policy",
          "order": 2
        },
        "deviceConfiguration": {
          "type": "boolean",
          "title": "Device Configuration",
          "description": "Device configuration",
          "order": 3
        },
        "inventory": {
          "type": "boolean",
          "title": "Inventory",
          "description": "Inventory",
          "order": 4
        },
        "modernApps": {
          "type": "boolean",
          "title": "Modern Apps",
          "description": "Modern apps",
          "order": 5
        },
        "resourceAccess": {
          "type": "boolean",
          "title": "Resource Access",
          "description": "Resource access",
          "order": 6
        },
        "windowsUpdateForBusiness": {
          "type": "boolean",
          "title": "Windows Update For Business",
          "description": "Windows update for business",
          "order": 7
        }
      }
    },
    "deviceActionResults": {
      "type": "object",
      "title": "deviceActionResults",
      "properties": {
        "@odata.type": {
          "type": "string",
          "title": "Odata Type",
          "description": "Odata type",
          "order": 1
        },
        "actionName": {
          "type": "string",
          "title": "Action Name",
          "description": "Action name",
          "order": 2
        },
        "actionState": {
          "type": "string",
          "title": "Action State",
          "description": "Action state",
          "order": 3
        },
        "lastUpdatedDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Last Updated Date Time",
          "description": "Last updated date time",
          "order": 4
        },
        "startDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Start Date Time",
          "description": "Start date time",
          "order": 5
        }
      }
    },
    "deviceHealthAttestationState": {
      "type": "object",
      "title": "deviceHealthAttestationState",
      "properties": {
        "@odata.type": {
          "type": "string",
          "title": "Odata Type",
          "description": "Odata type",
          "order": 1
        },
        "attestationIdentityKey": {
          "type": "string",
          "title": "Attestation Identity Key",
          "description": "Attestation identity key",
          "order": 2
        },
        "bitLockerStatus": {
          "type": "string",
          "title": "BitLocker Status",
          "description": "BitLocker status",
          "order": 3
        },
        "bootAppSecurityVersion": {
          "type": "string",
          "title": "Boot App Security Version",
          "description": "Boot app security version",
          "order": 4
        },
        "bootDebugging": {
          "type": "string",
          "title": "Boot Debugging",
          "description": "Boot debugging",
          "order": 5
        },
        "bootManagerSecurityVersion": {
          "type": "string",
          "title": "Boot Manager Security Version",
          "description": "Boot manager security version",
          "order": 6
        },
        "bootManagerVersion": {
          "type": "string",
          "title": "Boot Manager Version",
          "description": "Boot manager version",
          "order": 7
        },
        "bootRevisionListInfo": {
          "type": "string",
          "title": "Boot Revision List Info",
          "description": "Boot revision list info",
          "order": 8
        },
        "codeIntegrity": {
          "type": "string",
          "title": "Code Integrity",
          "description": "Code integrity",
          "order": 9
        },
        "codeIntegrityCheckVersion": {
          "type": "string",
          "title": "Code Integrity Check Version",
          "description": "Code integrity check version",
          "order": 10
        },
        "codeIntegrityPolicy": {
          "type": "string",
          "title": "Code Integrity Policy",
          "description": "Code integrity policy",
          "order": 11
        },
        "contentNamespaceUrl": {
          "type": "string",
          "title": "Content Namespace URL",
          "description": "Content namespace URL",
          "order": 12
        },
        "contentVersion": {
          "type": "string",
          "title": "Content Version",
          "description": "Content version",
          "order": 13
        },
        "dataExcutionPolicy": {
          "type": "string",
          "title": "Data Excution Policy",
          "description": "Data excution policy",
          "order": 14
        },
        "deviceHealthAttestationStatus": {
          "type": "string",
          "title": "Device Health Attestation Status",
          "description": "Device health attestation status",
          "order": 15
        },
        "earlyLaunchAntiMalwareDriverProtection": {
          "type": "string",
          "title": "Early Launch Anti Malware Driver Protection",
          "description": "Early launch anti malware driver protection",
          "order": 16
        },
        "healthAttestationSupportedStatus": {
          "type": "string",
          "title": "Health Attestation Supported Status",
          "description": "Health attestation supported status",
          "order": 17
        },
        "healthStatusMismatchInfo": {
          "type": "string",
          "title": "Health Status Mismatch Info",
          "description": "Health status mismatch info",
          "order": 18
        },
        "issuedDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Issued Date Time",
          "description": "Issued date time",
          "order": 19
        },
        "lastUpdateDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Last Update Date Time",
          "description": "Last update date time",
          "order": 20
        },
        "operatingSystemKernelDebugging": {
          "type": "string",
          "title": "Operating System Kernel Debugging",
          "description": "Operating system kernel debugging",
          "order": 21
        },
        "operatingSystemRevListInfo": {
          "type": "string",
          "title": "Operating System Rev List Info",
          "description": "Operating system rev list info",
          "order": 22
        },
        "pcr0": {
          "type": "string",
          "title": "PCR0",
          "description": "PCR0",
          "order": 23
        },
        "pcrHashAlgorithm": {
          "type": "string",
          "title": "PCR Hash Algorithm",
          "description": "PCR hash algorithm",
          "order": 24
        },
        "resetCount": {
          "type": "integer",
          "title": "Reset Count",
          "description": "Reset count",
          "order": 25
        },
        "restartCount": {
          "type": "integer",
          "title": "Restart Count",
          "description": "Restart count",
          "order": 26
        },
        "safeMode": {
          "type": "string",
          "title": "Safe Mode",
          "description": "Safe mode",
          "order": 27
        },
        "secureBoot": {
          "type": "string",
          "title": "Secure Boot",
          "description": "Secure boot",
          "order": 28
        },
        "secureBootConfigurationPolicyFingerPrint": {
          "type": "string",
          "title": "Secure Boot Configuration Policy Finger Print",
          "description": "Secure boot configuration policy finger print",
          "order": 29
        },
        "testSigning": {
          "type": "string",
          "title": "Test Signing",
          "description": "Test signing",
          "order": 30
        },
        "tpmVersion": {
          "type": "string",
          "title": "TPM Version",
          "description": "TPM version",
          "order": 31
        },
        "virtualSecureMode": {
          "type": "string",
          "title": "Virtual Secure Mode",
          "description": "Virtual secure mode",
          "order": 32
        },
        "windowsPE": {
          "type": "string",
          "title": "Windows PE",
          "description": "Windows PE",
          "order": 33
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
