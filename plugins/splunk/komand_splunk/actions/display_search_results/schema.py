# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Displays the search results from a job"


class Input:
    JOB_ID = "job_id"
    TIMEOUT = "timeout"
    

class Output:
    SEARCH_RESULTS = "search_results"
    

class DisplaySearchResultsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job_id": {
      "type": "string",
      "title": "Job Id",
      "description": "Job ID to look up results for",
      "order": 1
    },
    "timeout": {
      "type": "number",
      "title": "Timeout",
      "description": "Duration of time, in seconds, to wait for retrieving results",
      "order": 2
    }
  },
  "required": [
    "job_id",
    "timeout"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DisplaySearchResultsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "search_results": {
      "type": "array",
      "title": "Search Results",
      "description": "Search results from a job",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
