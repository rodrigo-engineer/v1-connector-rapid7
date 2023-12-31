# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Convert HTML to Markdown"


class Input:
    HTML = "html"
    HTML_STRING = "html_string"
    

class Output:
    MARKDOWN = "markdown"
    MARKDOWN_STRING = "markdown_string"
    

class HtmlToMarkdownInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "html": {
      "type": "string",
      "title": "HTML",
      "displayType": "bytes",
      "description": "HTML data as bytes",
      "format": "bytes",
      "order": 1
    },
    "html_string": {
      "type": "string",
      "title": "HTML String",
      "description": "HTML data as string",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class HtmlToMarkdownOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "markdown": {
      "type": "string",
      "title": "Markdown",
      "displayType": "bytes",
      "description": "Markdown data as bytes",
      "format": "bytes",
      "order": 1
    },
    "markdown_string": {
      "type": "string",
      "title": "Markdown",
      "displayType": "bytes",
      "description": "Markdown data as string",
      "format": "bytes",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
