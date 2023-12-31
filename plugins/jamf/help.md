# Description

[Jamf Pro](https://www.jamf.com/products/jamf-pro/) is a comprehensive management system for Apple macOS computers and iOS devices. This plugin uses the [Jamf Pro API](https://developer.jamf.com/apis/classic-api/index) to get and manage user and device information.

# Key Features

* Manage computers and group membership
* Get information about devices, users, and groups
* Lock mobile device in the event of a security incident

# Requirements

* Username and Password, or
* API Key

# Supported Product Versions

* Plugin successfully tested at 2022-08-26

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_login|credential_username_password|None|True|The Jamf username and password for basic authentication API interaction|None|{"username": "Example User", "password": "Example Password"}|
|timeout|integer|30|False|The interval in seconds before abandoning an attempt to access Jamf|None|30|
|url|string|None|True|The full URL for your Jamf instance|None|https://{instance}.jamfcloud.com|

Example input:

```
{
  "client_login": {
    "username": "Example User",
    "password": "Example Password"
  },
  "timeout": 30,
  "url": "https://{instance}.jamfcloud.com"
}
```

## Technical Details

### Actions

#### Add Computer to a Group

This action is used to add computer to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|integer|None|True|Group ID|None|1|
|computer_ids|[]integer|None|True|Computer IDs|None|[1, 2, 3]|

Example input:

```
{
  "ID": 1,
  "computer_ids": "[1, 2, 3]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|Status|

Example output:

```
{
  "status": 201
}
```

#### Erase Computer

This action is used to erase the user's computer by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|string|None|True|Identifier of the computer|None|134|
|passcode|string|None|True|The passcode of the computer|None|123456|

Example input:

```
{
  "ID": 134,
  "passcode": 123456
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Status|

Example output:

```
{
  "status": 201
}
```

#### Lock Computer

This action is used to test.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|string|None|True|Identifier of the computer|None|134|
|passcode|string|None|True|The passcode of the computer|None|123456|

Example input:

```
{
  "ID": 134,
  "passcode": 123456
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Status|

Example output:

```
{
  "status": 201
}
```

#### Get Device Groups

This action gets a list of all groups a device is a member of.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|integer|None|True|Device ID|None|1|

Example input:

```
{
  "ID": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device_groups|[]device_group_detail|True|List of device groups|

Example output:

```
{
  "device_groups": [
    {
      "id": 2,
      "name": "All Managed iPhones"
    },
    {
      "id": 5,
      "name": "Smart Group temp"
    }
  ]
}
```

#### Get Devices Names and IDs

This action is used to get a list of a user's device names and IDs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|User name|None|Example Name|

Example input:

```
{
  "name": "Example Name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device_detail|object|True|Device detail|

Example output:

```
{
  "device_detail": {
  "computers": [],
  "mobile_devices": [
    {
      "id": 2,
      "name": "Jon’s iPhone"
    }
  ],
  "peripherals": [],
  "total_vpp_code_count": 0,
  "vpp_assignments": []
  }
}
```

#### Get Group Details

This action is used to get group details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|integer|None|True|Group ID|None|1|

Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group_detail|group_detail|True|Group detail|

Example output:

```
{
  "group_detail": {
    "mobile_device_group": {
      "criteria": [
        {
          "and_or": "AND",
          "closing_paren": false,
          "name": "Model",
          "opening_paren": false,
          "priority": 0,
          "search_type": "like",
          "value": "iPhone"
        },
        {
          "and_or": "and",
          "closing_paren": false,
          "name": "Username",
          "opening_paren": false,
          "priority": 1,
          "search_type": "is",
          "value": "Jon"
        },
        {
          "and_or": "and",
          "closing_paren": false,
          "name": "Last Inventory Update",
          "opening_paren": false,
          "priority": 2,
          "search_type": "before (yyyy-mm-dd)",
          "value": "2019-10-10"
        }
      ],
        "id": 2,
        "is_smart": true,
        "mobile_devices": [
          {
            "id": 2,
            "mac_address": "54:4E:90:84:AC:E9",
            "name": "Jon’s iPhone",
            "serial_number": "F17Q4JFBG5MC",
            "udid": "1bdf99f35865df30ccde9a9c786abf021e41d8a9",
            "wifi_mac_address": "54:4E:90:84:AC:E9"
          }
        ],
          "name": "All Managed iPhones",
          "site": {
            "id": -1,
            "name": "None"
          }
    }
  }
}
```

#### Lock Mobile Devices

This action is used to lock mobile devices.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|devices_id|[]string|None|True|List of devices IDs|None|["1", "2"]|

Example input:

```
{
  "devices_id": ["1", "2"]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|Status|

Example output:

```
{
  "status": 201
}
```

#### Get User Location Details

This action is used to get user location details by device ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|string|None|True|Device ID|None|1|

Example input:

```
{
  "ID": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_location_detail|user_location_detail|True|User location details|

Example output:

```
{
  "user_location_detail": {
    "building": "",
    "department": "",
    "email_address": "user@example.com",
    "phone": "999-999-9999",
    "position": "Director",
    "real_name": "Jonathan Schipp",
    "room": "9999",
    "username": "Jon"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - Added new actions Lock Computer, and Erase Computer | Updated plugin SDK to 4 | Added unittests
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - Add action to get user location details by device ID
* 1.0.0 - Initial plugin

# Links

## References

* [Jamf](https://developer.jamf.com/apis/classic-api/index)

