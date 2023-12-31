# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get all dynamic and static analyses in the system or details about specific ones"


class Input:
    ID = "id"
    ID_TYPE = "id_type"
    OPTIONAL_PARAMS = "optional_params"
    

class Output:
    RESULTS = "results"
    

class GetAnalysisInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "ID based on ID type selected, leave blank if 'all' is selected",
      "order": 2
    },
    "id_type": {
      "type": "string",
      "title": "ID Type",
      "description": "Get analysis based on ID of a specified type",
      "enum": [
        "analysis_id",
        "analyzer",
        "configuration",
        "static_config",
        "created",
        "job",
        "jobrule",
        "job_started",
        "prescript",
        "result_code",
        "sample",
        "size",
        "snapshot",
        "submission",
        "user",
        "vm",
        "vmhost",
        "vti_score",
        "all"
      ],
      "order": 1
    },
    "optional_params": {
      "type": "object",
      "title": "Optional Parameters",
      "description": "Parameters that allow finer tuning of the Get Analysis action, e.g {\\"analysis_id\\": 12345}",
      "order": 3
    }
  },
  "required": [
    "id_type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAnalysisOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Results returned from analysis",
      "items": {
        "$ref": "#/definitions/analysis_result"
      },
      "order": 1
    }
  },
  "definitions": {
    "analysis_result": {
      "type": "object",
      "title": "analysis_result",
      "properties": {
        "analysis_analyzer_id": {
          "type": "integer",
          "title": "Analysis Analyzer ID",
          "description": "Analysis analyzer ID",
          "order": 1
        },
        "analysis_analyzer_name": {
          "type": "string",
          "title": "Analysis Analyzer Name",
          "description": "Analysis analyzer name e.g vmray",
          "order": 4
        },
        "analysis_analyzer_version": {
          "type": "string",
          "title": "Analysis Analyzer Version",
          "description": "Analysis analyzer version",
          "order": 22
        },
        "analysis_configuration_id": {
          "type": "integer",
          "title": "Analysis Configuration ID",
          "description": "Analysis configuration ID",
          "order": 27
        },
        "analysis_configuration_name": {
          "type": "string",
          "title": "Analysis Configuration Name",
          "description": "Analysis configuration name",
          "order": 42
        },
        "analysis_created": {
          "type": "string",
          "title": "Analysis Created",
          "description": "Analysis Created",
          "order": 46
        },
        "analysis_document_password": {
          "type": "string",
          "title": "Analysis Document Password",
          "description": "Analysis document password",
          "order": 14
        },
        "analysis_id": {
          "type": "integer",
          "title": "Analysis ID",
          "description": "Analysis ID",
          "order": 11
        },
        "analysis_ioc_aggregation_state": {
          "type": "string",
          "title": "Analysis IOC Aggregation State",
          "description": "Analysis IOC aggregation state",
          "order": 18
        },
        "analysis_job_id": {
          "type": "integer",
          "title": "Analysis Job ID",
          "description": "Analysis job ID",
          "order": 36
        },
        "analysis_job_started": {
          "type": "string",
          "title": "Analysis Job Started",
          "description": "Analysis job started date e.g 2017-11-29T12:06:39",
          "order": 6
        },
        "analysis_job_type": {
          "type": "string",
          "title": "Analysis Job Type",
          "description": "Analysis job type",
          "order": 37
        },
        "analysis_jobrule_id": {
          "type": "integer",
          "title": "Analysis Job Rule ID",
          "description": "Analysis job rule ID",
          "order": 35
        },
        "analysis_prescript_force_admin": {
          "type": "boolean",
          "title": "Analysis Prescript Force Admin",
          "description": "Analysis prescript force admin",
          "order": 26
        },
        "analysis_prescript_id": {
          "type": "integer",
          "title": "Analysis Prescript ID",
          "description": "Analysis prescript ID",
          "order": 23
        },
        "analysis_priority": {
          "type": "integer",
          "title": "Analysis Priority",
          "description": "Analysis priority e.g 5",
          "order": 3
        },
        "analysis_report_version": {
          "type": "integer",
          "title": "Analysis Report Version",
          "description": "Analysis report version",
          "order": 7
        },
        "analysis_result_code": {
          "type": "integer",
          "title": "Analysis Result Code",
          "description": "Analysis result code",
          "order": 25
        },
        "analysis_result_str": {
          "type": "string",
          "title": "Analysis Result String",
          "description": "Analysis result string",
          "order": 40
        },
        "analysis_sample_id": {
          "type": "integer",
          "title": "Analysis Sample ID",
          "description": "Analysis sample ID",
          "order": 43
        },
        "analysis_sample_md5": {
          "type": "string",
          "title": "Analysis Sample MD5",
          "description": "Analysis sample MD5",
          "order": 15
        },
        "analysis_sample_sha1": {
          "type": "string",
          "title": "Analysis Sample SHA1",
          "description": "Analysis sample SHA1 e.g 124f46228d1e220d88ae5e9a24d6e713039a64f9",
          "order": 5
        },
        "analysis_sample_sha256": {
          "type": "string",
          "title": "Analysis Sample SHA-256",
          "description": "Analysis sample SHA-256",
          "order": 10
        },
        "analysis_sample_ssdeep": {
          "type": "string",
          "title": "Analysis Sample ssdeep",
          "description": "Analysis sample ssdeep",
          "order": 20
        },
        "analysis_serialized_results": {
          "$ref": "#/definitions/analysis_serialized_result",
          "title": "Analysis Serialized Results",
          "description": "Analysis serialized results",
          "order": 16
        },
        "analysis_severity": {
          "type": "string",
          "title": "Analysis Severity",
          "description": "Analysis severity e.g suspicious",
          "order": 9
        },
        "analysis_size": {
          "type": "integer",
          "title": "Analysis Size",
          "description": "Analysis size",
          "order": 24
        },
        "analysis_snapshot_id": {
          "type": "integer",
          "title": "Analysis Snapshot ID",
          "description": "Analysis snapshot ID",
          "order": 39
        },
        "analysis_snapshot_name": {
          "type": "string",
          "title": "Analysis Snapshot Name",
          "description": "Analysis snapshot name",
          "order": 30
        },
        "analysis_static_config_id": {
          "type": "integer",
          "title": "Analysis Static Config ID",
          "description": "Analysis static config ID",
          "order": 21
        },
        "analysis_submission_id": {
          "type": "integer",
          "title": "Analysis submission ID",
          "description": "Analysis submission ID",
          "order": 19
        },
        "analysis_system_time": {
          "type": "string",
          "title": "Analysis System Time",
          "description": "Analysis system time",
          "order": 34
        },
        "analysis_tags": {
          "type": "array",
          "title": "Analysis tags",
          "description": "Analysis tags",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "analysis_user_email": {
          "type": "string",
          "title": "Analysis User Email",
          "description": "Analysis user email e.g demo@vmray.com",
          "order": 2
        },
        "analysis_user_id": {
          "type": "integer",
          "title": "Analysis User ID",
          "description": "Analysis user ID",
          "order": 32
        },
        "analysis_vm_id": {
          "type": "integer",
          "title": "Analysis VM ID",
          "description": "Analysis VM ID",
          "order": 17
        },
        "analysis_vm_name": {
          "type": "string",
          "title": "Analysis VM Name",
          "description": "Analysis VM name",
          "order": 29
        },
        "analysis_vmhost_id": {
          "type": "integer",
          "title": "Analysis VMhost ID",
          "description": "Analysis vmhost ID",
          "order": 13
        },
        "analysis_vmhost_name": {
          "type": "string",
          "title": "Analysis VMhost Name",
          "description": "Analysis vmhost name",
          "order": 12
        },
        "analysis_vti_aggregation_state": {
          "type": "string",
          "title": "Analysis VTI Aggregation State",
          "description": "Analysis VTI aggregation state",
          "order": 38
        },
        "analysis_vti_built_in_rules_version": {
          "type": "string",
          "title": "Analysis VTI Built in Rules Version",
          "description": "Analysis VTI built in rules version",
          "order": 33
        },
        "analysis_vti_custom_rules_hash": {
          "type": "string",
          "title": "Analysis VTI Custom Rules Hash",
          "description": "Analysis VTI custom rules hash",
          "order": 31
        },
        "analysis_vti_score": {
          "type": "integer",
          "title": "Analysis VIT Score",
          "description": "Analysis VTI score",
          "order": 41
        },
        "analysis_webif_url": {
          "type": "string",
          "title": "Analysis Webif URL",
          "description": "Analysis webif URL",
          "order": 44
        },
        "analysis_yara_latest_ruleset_date": {
          "type": "string",
          "title": "Analysis Yara Latest Ruleset Data",
          "description": "Analysis Yara latest ruleset data",
          "order": 28
        },
        "analysis_yara_match_count": {
          "type": "integer",
          "title": "Analysis Yara Match Count",
          "description": "Analysis Yara match count",
          "order": 45
        }
      },
      "definitions": {
        "analysis_serialized_result": {
          "type": "object",
          "title": "analysis_serialized_result",
          "properties": {
            "code": {
              "type": "integer",
              "title": "Code",
              "description": "Code",
              "order": 1
            },
            "extra_args": {
              "type": "object",
              "title": "Extra Arguments",
              "description": "Extra args",
              "order": 2
            },
            "fmt_args": {
              "type": "array",
              "title": "Formatted Arguments",
              "description": "Formatted arguments",
              "items": {
                "type": "object"
              },
              "order": 3
            }
          }
        }
      }
    },
    "analysis_serialized_result": {
      "type": "object",
      "title": "analysis_serialized_result",
      "properties": {
        "code": {
          "type": "integer",
          "title": "Code",
          "description": "Code",
          "order": 1
        },
        "extra_args": {
          "type": "object",
          "title": "Extra Arguments",
          "description": "Extra args",
          "order": 2
        },
        "fmt_args": {
          "type": "array",
          "title": "Formatted Arguments",
          "description": "Formatted arguments",
          "items": {
            "type": "object"
          },
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
