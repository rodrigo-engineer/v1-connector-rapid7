# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get all samples in the system or details about specific ones. You can also search by hashes"


class Input:
    OPTIONAL_PARAMS = "optional_params"
    SAMPLE = "sample"
    SAMPLE_TYPE = "sample_type"
    

class Output:
    RESULTS = "results"
    

class GetSamplesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "optional_params": {
      "type": "object",
      "title": "Optional Parameters",
      "description": "Parameters that allow finer tuning of the Get Samples action, e.g {\\"analysis_id\\": 12345}",
      "order": 3
    },
    "sample": {
      "type": "string",
      "title": "Sample",
      "description": "Sample ID, hash or type, leave blank if 'all' is selected",
      "order": 2
    },
    "sample_type": {
      "type": "string",
      "title": "Sample Type",
      "description": "Specified type of sample",
      "enum": [
        "all",
        "sample_id",
        "created",
        "filesize",
        "md5",
        "sha1",
        "sha256",
        "type"
      ],
      "order": 1
    }
  },
  "required": [
    "sample_type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSamplesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Results from samples",
      "items": {
        "$ref": "#/definitions/sample"
      },
      "order": 1
    }
  },
  "definitions": {
    "sample": {
      "type": "object",
      "title": "sample",
      "properties": {
        "sample_classifications": {
          "type": "array",
          "title": "Sample Classifications",
          "description": "Classifications",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "sample_created": {
          "type": "string",
          "title": "Sample Created",
          "description": "Date sample was created",
          "order": 13
        },
        "sample_filename": {
          "type": "string",
          "title": "Sample Filename",
          "description": "Filename",
          "order": 23
        },
        "sample_filesize": {
          "type": "integer",
          "title": "Sample Filesize",
          "description": "Filesize",
          "order": 15
        },
        "sample_highest_vti_score": {
          "type": "integer",
          "title": "Sample Highest VTI Score",
          "description": "Highest VTI score for sample",
          "order": 10
        },
        "sample_highest_vti_severity": {
          "type": "string",
          "title": "Sample Highest VTI Severity",
          "description": "Highest VTI severity",
          "order": 11
        },
        "sample_id": {
          "type": "integer",
          "title": "Sample ID",
          "description": "Sample ID",
          "order": 2
        },
        "sample_imphash": {
          "type": "string",
          "title": "Sample Import Hash",
          "description": "Import hash",
          "order": 9
        },
        "sample_is_multipart": {
          "type": "boolean",
          "title": "Sample Is Multipart",
          "description": "Is multipart",
          "order": 21
        },
        "sample_last_md_score": {
          "type": "integer",
          "title": "Sample Last MD Score",
          "description": "MD score",
          "order": 5
        },
        "sample_last_reputation_severity": {
          "type": "string",
          "title": "Sample Last Reputation Severity",
          "description": "Last reputation severity",
          "order": 14
        },
        "sample_last_vt_score": {
          "type": "integer",
          "title": "Sample Last VT Score",
          "description": "VT score",
          "order": 6
        },
        "sample_md5hash": {
          "type": "string",
          "title": "Sample MD5 Hash",
          "description": "MD5 Hash",
          "order": 17
        },
        "sample_priority": {
          "type": "integer",
          "title": "Sample Priority",
          "description": "Priority",
          "order": 20
        },
        "sample_score": {
          "type": "integer",
          "title": "Sample Score",
          "description": "Score",
          "order": 22
        },
        "sample_severity": {
          "type": "string",
          "title": "Sample Severity",
          "description": "Severity",
          "order": 7
        },
        "sample_sha1hash": {
          "type": "string",
          "title": "Sample SHA1 Hash",
          "description": "SHA1 hash",
          "order": 3
        },
        "sample_sha256hash": {
          "type": "string",
          "title": "Sample SHA256 Hash",
          "description": "SHA256 Hash",
          "order": 18
        },
        "sample_ssdeephash": {
          "type": "string",
          "title": "Sample ssdeep Hash",
          "description": "Ssdeep hash",
          "order": 16
        },
        "sample_type": {
          "type": "string",
          "title": "Sample Type",
          "description": "Type",
          "order": 12
        },
        "sample_url": {
          "type": "string",
          "title": "Sample URL",
          "description": "URL",
          "order": 8
        },
        "sample_vti_score": {
          "type": "integer",
          "title": "Sample VTI Score",
          "description": "Automated threat score of the sample",
          "order": 1
        },
        "sample_webif_url": {
          "type": "string",
          "title": "Sample Webif URL",
          "description": "Webif URL",
          "order": 19
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
