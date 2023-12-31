# Description

[VMware Carbon Black Cloud Endpoint Standard](https://www.carbonblack.com/products/endpoint-standard/) is a next-generation antivirus and EDR in one cloud-delivered platform. The InsightConnect plugin allows you to find events and retrieve details for specific events.

This plugin utilizes the [VMware Carbon Black Cloud Endpoint Standard API](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/rest-api/).

# Key Features

* Find events
* Get details for specific events

# Requirements

* Requires an API key from VMware Carbon Black Cloud Endpoint Standard with CRUD permissions and Custom Level Access Type

# Supported Product Versions

* 2022-15-03

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|connector|string|None|True|Connector ID|None|1Y72FRRWVP|
|org_key|string|None|True|Organization key|None|1ABCDE5GH|
|url|string|https://example.com|True|API URL|None|https://example.com|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "connector": "1Y72FRRWVP",
  "org_key": "1ABCDE5GH",
  "url": "https://example.com"
}
```

## Technical Details

### Actions

#### Find Event

This action is used to retrieve all events matching the input search criteria. Response contains a list of events in JSON format. Resulting events are sorted in descending order of time.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device_external_ip|[]string|None|False|Device external IP|None|192.0.2.0|
|device_name|[]string|None|False|Device name|None|CONTOSO\bruce-win10|
|enriched_event_type|[]string|None|False|Enriched event type|None|SYSTEM_API_CALL|
|process_hash|[]string|None|False|Filter on events generated by a process with the given SHA-256 hash. Note that this hash must be lowercase|None|["A3DED3871AC66498E406798B0CA33F1B5E94B9CFB60DD4489475B9C19FBFD7F5"]|
|process_name|[]string|None|False|Process name|None|c:\windows\system32\windowspowershell\v1.0\modules\smbshare\disableunusedsmb1.ps1|
|time_range|string|None|False|Time frame to limit your search to. Integer used for amount of the following: s=second(s), m=minute(s), h=hour(s), d=day(s), w=week(s), or y=year(s). Example: -2d|None|-2d|


Example input:

```
{
  "device_external_ip": "192.0.2.0",
  "device_name": "CONTOSO\\bruce-win10",
  "enriched_event_type": "SYSTEM_API_CALL",
  "process_hash": [
    "A3DED3871AC66498E406798B0CA33F1B5E94B9CFB60DD4489475B9C19FBFD7F5"
  ],
  "process_name": "c:\\windows\\system32\\windowspowershell\\v1.0\\modules\\smbshare\\disableunusedsmb1.ps1",
  "time_range": "-2d"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|approximate_unaggregated|integer|False|The number of matching events used to construct the processes which will be equivalent to Num Found|
|completed|integer|False|The number of searchers that have reported their results|
|contacted|integer|False|The number of searchers contacted for this query|
|num_aggregated|integer|False|The number of processes that were constructed from the events which will be equal or greater than Num Available|
|num_available|integer|False|Number of found results able to be paginated|
|num_found|integer|False|Number of results found|
|results|[]event_info|False|Detailed information on the event|
|success|boolean|False|Success|

Example output:

```
{
  "approximate_unaggregated": 78750,
  "completed": 5,
  "contacted": 5,
  "num_aggregated": 503,
  "num_available": 500,
  "num_found": 78750,
  "results": [
    {
      "backend_timestamp": "2022-03-15T10:28:11.423Z",
      "device_group_id": 0,
      "device_id": 4849627,
      "device_name": "wb-auto-qa",
      "device_policy_id": 6525,
      "device_timestamp": "2022-03-15T10:26:39.253Z",
      "enriched": true,
      "enriched_event_type": "NETWORK",
      "event_description": "The operation was <accent>blocked by Cb Defense</accent>.",
      "event_id": "8581bd14a44a11ec8b1abf3be4c31ca0",
      "event_network_inbound": false,
      "event_network_local_ipv4": "10.0.7.12",
      "event_network_location": "Piscataway,NJ,United States",
      "event_network_protocol": "TCP",
      "event_network_remote_ipv4": "23.4.227.29",
      "event_network_remote_port": 443,
      "event_type": "netconn",
      "ingress_time": 1647340061569,
      "legacy": true,
      "org_id": "7DESJ9GN",
      "parent_guid": "7DESJ9GN-0049ffdb-000003c4-00000000-1d8336797e1b8e5",
      "parent_pid": 964,
      "process_guid": "7DESJ9GN-0049ffdb-0000175c-00000000-1d836263d49edea",
      "process_hash": [
        "cd10cb894be2128fca0bf0e2b0c27c16",
        "f3feb95e7bcfb0766a694d93fca29eda7e2ca977c2395b4be75242814eb6d881"
      ],
      "process_name": "c:\\windows\\system32\\svchost.exe",
      "process_pid": [
        5980
      ],
      "process_username": [
        "NT AUTHORITY\\NETWORK SERVICE"
      ],
      "sensor_action": [
        "DENY",
        "BLOCK"
      ]
    }
  ],
  "success": true
}
```


#### Get Details for Specific Event

This action is used to retrieve details for an individual event given the event ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_ids|string|None|True|Event ID used to retrieve event details. Example: 422af3fc3a7411ea8da649e797467dc0|None|422af3fc3a7411ea8da649e797467dc0|

Example input:

```
{
  "event_ids": "422af3fc3a7411ea8da649e797467dc0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|approximate_unaggregated|integer|False|The number of matching events used to construct the processes which will be equivalent to Num Found|
|completed|integer|False|The number of searchers that have reported their results|
|contacted|integer|False|The number of searchers contacted for this query|
|num_aggregated|integer|False|The number of processes that were constructed from the events which will be equal or greater than Num Available|
|num_available|integer|False|Number of found results able to be paginated|
|num_found|integer|False|Number of results found|
|results|[]event_info|False|Detailed information on the event|
|success|boolean|False|Success|

Example output:

```
{
  "approximate_unaggregated": 78750,
  "completed": 5,
  "contacted": 5,
  "num_aggregated": 503,
  "num_available": 500,
  "num_found": 78750,
  "results": [
    {
      "backend_timestamp": "2022-03-15T10:28:11.423Z",
      "device_group_id": 0,
      "device_id": 4849627,
      "device_name": "wb-auto-qa",
      "device_policy_id": 6525,
      "device_timestamp": "2022-03-15T10:26:39.253Z",
      "enriched": true,
      "enriched_event_type": "NETWORK",
      "event_description": "The operation was <accent>blocked by Cb Defense</accent>.",
      "event_id": "8581bd14a44a11ec8b1abf3be4c31ca0",
      "event_network_inbound": false,
      "event_network_local_ipv4": "10.0.7.12",
      "event_network_location": "Piscataway,NJ,United States",
      "event_network_protocol": "TCP",
      "event_network_remote_ipv4": "23.4.227.29",
      "event_network_remote_port": 443,
      "event_type": "netconn",
      "ingress_time": 1647340061569,
      "legacy": true,
      "org_id": "7DESJ9GN",
      "parent_guid": "7DESJ9GN-0049ffdb-000003c4-00000000-1d8336797e1b8e5",
      "parent_pid": 964,
      "process_guid": "7DESJ9GN-0049ffdb-0000175c-00000000-1d836263d49edea",
      "process_hash": [
        "cd10cb894be2128fca0bf0e2b0c27c16",
        "f3feb95e7bcfb0766a694d93fca29eda7e2ca977c2395b4be75242814eb6d881"
      ],
      "process_name": "c:\\windows\\system32\\svchost.exe",
      "process_pid": [
        5980
      ],
      "process_username": [
        "NT AUTHORITY\\NETWORK SERVICE"
      ],
      "sensor_action": [
        "DENY",
        "BLOCK"
      ]
    }
  ],
  "success": true
}
```

### Triggers

#### Get Notifications

This trigger is used to allows consumers to get alert and policy action notifications that a connector is subscribed to. Only API keys of type 'SIEM' can call the notifications API.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|10|True|How often to poll for new notifications requests, in seconds|None|10|

Example input:

```
{
  "frequency": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Notification Message|
|notifications|[]notifications|False|Collection of Notifications|
|success|boolean|False|Notification Success|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

When selecting adjusting frequency please review [rate limits](https://developer.carbonblack.com/reference/carbon-black-cloud/rate-limiting/).
Get Notifications trigger requires that the [API key type](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/) is a 'SIEM' type.
The Role Based Access Control (RBAC) of your API Key will require the right permissions as noted in the following link: [https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/platform-search-api-enriched-events/#authentication](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/platform-search-api-enriched-events/#authentication).

The Find Event API and Get Details for Specific Event API are now documented as Enriched Events Search and Enriched Event Details Search at the following links: [https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/platform-search-api-enriched-events/#start-an-enriched-events-search-v2](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/platform-search-api-enriched-events/#start-an-enriched-events-search-v2) and [https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/platform-search-api-enriched-events/#request-details-for-enriched-events-v2](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/platform-search-api-enriched-events/#request-details-for-enriched-events-v2).
# Version History

* 3.0.0 - Update Get Event Details Action and Find Event Action supporting new API with new inputs and outputs | Update SDK to version 4
* 2.0.1 - Rebrand and update help references
* 2.0.0 - New spec and help.md format for the Extension Library | Fix spelling of variable titled Registry Value
* 1.1.1 - Update to Python 3.7 Slim SDK (plugin size reduction) | Fix bug in output where Security Event Code was defined as an `object` instead of a `string`
* 1.1.0 - New action Get Details for Specific Event
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.0 - Initial plugin

# Links

## References

* [VMware Carbon Black Cloud Endpoint Standard](https://www.carbonblack.com/products/endpoint-standard/)
* [VMware Carbon Black Cloud Endpoint Standard API](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/rest-api/)
* [Rate Limits](https://developer.carbonblack.com/reference/carbon-black-cloud/rate-limiting/)
* [API Key Types](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/#creating-an-api-key)