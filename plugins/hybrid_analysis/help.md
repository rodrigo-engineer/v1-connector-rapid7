# Description

[Hybrid Analysis](https://www.hybrid-analysis.com/) is a free malware analysis service powered by Payload Security that detects and analyzes unknown threats using a unique Hybrid Analysis technology. This plugin provides the ability to lookup file hashes to determine whether or not they are malicious.

# Key Features

* Lookup a file hash to identify known and unknown threats using Hybrid Analysis technology

# Requirements

* A HybridAnalysis API key and token

# Supported Product Versions

* Hybrid Analysis API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|url|string|https://example.com|True|Hybrid-analysis API Server URL|None|https://example.com|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://www.hybrid-analysis.com"
}
```

## Technical Details

### Actions

#### Retrieve Report

This action is used to retrieve report by providing SHA256 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|error|string|False|An error that occurred during the analysis|
|error_origin|string|False|Error origin|
|error_type|string|False|Type of error that occurred|
|related_reports|[]related_reports|False|Related reports which contained analysis information on linked data|
|state|string|True|State in which the analysis is in|

Example output:

```
{
  "related_reports": [{
    "job_id": "61dc148b0cad612f7371d2d3",
    "environment_id": 300,
    "state": "SUCCESS",
    "sha256": "275a021bbfb6489e54d411499f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
  }],
  "state": "SUCCESS"
}
```

#### Submit File

This action is used to submit file for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|custom_cmd_line|string|None|False|Optional command line that should be passed to the file analysis|None|command|
|document_password|string|None|False|Optional document password that will be used to fill-in Adobe/Office password prompts|None|somepassword|
|environment_id|string|Linux (Ubuntu 16.04, 64 bit)|False|Environment ID on which the analysis will be performed|['Linux (Ubuntu 16.04, 64 bit)', 'Android Static Analysis', 'Windows 7 64 bit', 'Windows 7 32 bit (HWP Support)', 'Windows 7 32 bit']|Linux (Ubuntu 16.04, 64 bit)|
|experimental_anti_evasion|boolean|True|False|When set to true, will set all experimental anti-evasion options of the Kernelmode Monitor|None|True|
|file|file|None|True|File to be analyzed|None|{"filename": "setup.exe", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==" }|
|hybrid_analysis|boolean|True|False|When set to false, no memory dumps or memory dump analysis will take place|None|True|
|script_logging|boolean|False|False|When set to true, will set the in-depth script logging engine of the Kernelmode Monitor|None|True|
|submit_name|string|None|False|Optional property which will be used for file type detection and analysis|None|testName|

Example input:

```
{
   "custom_cmd_line":"command",
   "document_password":"somepassword",
   "environment_id":"Linux (Ubuntu 16.04, 64 bit)",
   "experimental_anti_evasion":true,
   "file":{
      "filename":"setup.exe",
      "content":"UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
   },
   "hybrid_analysis":true,
   "script_logging":true,
   "submit_name":"testName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|environment_id|integer|False|The environment that was used for analysis|
|job_id|string|False|Job ID which will be generated by server|
|sha256|string|False|SHA256 hash for report retrieval|
|submission_id|string|False|Submission ID which will be generated by server|

Example output:

```
{
  "sha256": "6617aa88a72e6b526b88cbceda388a7b52a0e856148a12d9b8...",
  "submission_id": "61dc160cee840164931bd394",
  "environment_id": 300,
  "job_id": "61dc148b0cad612f7371d2d3"
}
```

#### Search Database

This action is used to search the database using API v2 provided at https://www.hybrid-analysis.com/docs/api/v2.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|country|string|None|False|Country must be specified in the ISO 3166-1 standard|None|AFG|
|domain|string|None|False|Domain which will be analyzed|None|example.com|
|filename|string|None|False|File name|None|setup.exe|
|filetype|string|None|False|File type|None|docx|
|host|string|None|False|Information about the host which will be analyzed|None|198.51.100.1|
|port|integer|8080|False|Port number which is associated with an IP address|None|8080|
|similar_to|string|None|False|SHA256 hash of the similar file|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|tag|string|None|False|Hashtag by which the analysis will be performed|None|ransomware|
|url|string|None|False|URL to analyze|None|https://example.com|
|verdict|string|whitelisted|False|A decision on a submitted term|['whitelisted', 'no verdict', 'no specific threat', 'suspicious', 'malicious']|whitelisted|

Example input:

```
{
  "country": "AFG",
  "domain": "example.com",
  "filename": "setup.exe",
  "filetype": "docx",
  "host": "198.51.100.1",
  "port": 8080,
  "similar_to": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "tag": "ransomware",
  "url": "https://example.com",
  "verdict": "whitelisted"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of results returned|
|result|[]result|False|List of results|
|search_terms|[]search_term|True|List of key value pairs. Where the key is the parameter specified and its value|

Example output:

```
{
  "count": 1,
  "result": [
    {
      "analysis_start_time": "2021-09-02 18:58:23",
      "av_detect": "0",
      "environment_description": "Windows 7 64 bit",
      "environment_id": 120,
      "job_id": "61311eca7a48ee7a9e3041d7",
      "sha256": "82b43762a5bc9c0ab7b5d1f96dc47b34700924b598070a7ccb30c92eb5ee1599",
      "size": 18944,
      "submit_name": "ew_usbccgpfilter.sys",
      "type_short": "64-bit service",
      "verdict": "whitelisted"
    },
  ],
  "search_terms": [
    {
      "id": "filename",
      "value": "setup.exe"
    },
    {
      "id": "verdict",
      "value": "1"
    }
  ]
}

```

#### Lookup by Hash

This action is used to get summary information for a given hash. Allowed hashes MD5/SHA1/SHA256.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Hash to lookup. Must be MD5, SHA1, or SHA256|None|44d88612fea8a8f36de82e1278abb02f|

Example input:

```
{
  "hash": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|reports|[]report|False|Reports|
|threatscore|integer|False|Threat Score (max found)|

Example output:

```
{
  "found": true,
  "reports": [
    {
      "analysis_start_time": "2021-11-09T19:12:21+00:00",
      "av_detect": 0,
      "certificates": [],
      "classification_tags": [],
      "compromised_hosts": [],
      "domains": [],
      "environment_description": "Static Analysis",
      "extracted_files": [],
      "hosts": [],
      "interesting": false,
      "machine_learning_models": [],
      "md5": "40451f20371329b992fb1b85c754d062",
      "mitre_attcks": [],
      "network_mode": "default",
      "processes": [],
      "sha1": "89504d91c5539a366e153894c1bc17277116342b",
      "sha256": "3919059a1e0d38d6116f24945b0bb2aa5e98b85ac688b3aba270d7997bb64a0d",
      "sha512": "acfaca234c48f055c0f532e16bd5879f1637ecd639938c3d301b528b08af79988fcd6f0b61e4fd51901b250e72c90a48aca60d20d1b54036373aa6996baae326",
      "size": 27298,
      "state": "SUCCESS",
      "submissions": [
        {
          "created_at": "2021-11-10T20:09:28+00:00",
          "filename": "file",
          "submission_id": "618c26f8099c0e23c541f405"
        },
        {
          "created_at": "2021-11-09T19:12:21+00:00",
          "filename": "file",
          "submission_id": "618ac815742aee567341009c"
        }
      ],
      "submit_name": "file",
      "tags": [],
      "threat_level": 0,
      "total_network_connections": 0,
      "total_processes": 0,
      "total_signatures": 0,
      "type": "PE32 executable (DLL) (GUI) Intel 80386, for MS Windows",
      "type_short": [
        "pedll",
        "executable"
      ],
      "url_analysis": false,
      "verdict": "no specific threat"
    }
  ],
  "threatscore": 0
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 3.0.0 - Update to support version 2 API | Created new actions which was moved from plugin **vxstream_sandbox** such as: Submit File, Lookup by Hash, Search Database, Retrieve Report
* 2.0.2 - Fix threatscore KeyError
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Update to new secret key credential type
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Hybrid Analysis](https://www.hybrid-analysis.com/)

