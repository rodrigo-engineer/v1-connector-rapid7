# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extracts all dates from a string or file"


class Input:
    DATE_FORMAT = "date_format"
    FILE = "file"
    STR = "str"


class Output:
    DATES = "dates"


class DateExtractorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "date_format": {
      "type": "string",
      "title": "Date Format",
      "description": "Dates matching this format are extracted - If All Formats is selected, found dates will be processed in the listed order documented",
      "enum": [
        "dd/mm/yyyy",
        "mm/dd/yyyy",
        "dd\\mm\\yyyy",
        "dd.mm.yyyy",
        "dd-mm-yyyy",
        "dd.mm.yy",
        "dd-mm-yy",
        "dd/mm/yy",
        "dd\\mm\\yy",
        "mm\\dd\\yyyy",
        "mm.dd.yyyy",
        "mm-dd-yyyy",
        "mm/dd/yy",
        "mm\\dd\\yy",
        "mm.dd.yy",
        "mm-dd-yy",
        "dd/mmm/yyyy",
        "dd\\mmm\\yyyy",
        "dd.mmm.yyyy",
        "dd-mmm-yyyy",
        "dd/mmm/yy",
        "dd\\mmm\\yy",
        "dd.mmm.yy",
        "dd-mmm-yy",
        "yyyy.mm.dd",
        "yyyy-mm-dd",
        "yyyy/mm/dd",
        "yyyy\\mm\\dd",
        "yyyy.mmm.dd",
        "yyyy-mmm-dd",
        "yyyy/mmm/dd",
        "yyyy\\mmm\\dd",
        "yy.mm.dd",
        "yy-mm-dd",
        "yy/mm/dd",
        "yy\\mm\\dd",
        "yyyy-mm-ddThh:mm",
        "yyyy-mm-ddThh:mm:ss",
        "All Formats",
        ""
      ],
      "order": 1
    },
    "file": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "File",
      "description": "Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS",
      "order": 3
    },
    "str": {
      "type": "string",
      "title": "String",
      "description": "Input string",
      "order": 2
    }
  },
  "required": [
    "date_format"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DateExtractorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "dates": {
      "type": "array",
      "title": "Dates",
      "description": "List of extracted dates",
      "items": {
        "type": "string",
        "format": "date-time",
        "displayType": "date"
      },
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)