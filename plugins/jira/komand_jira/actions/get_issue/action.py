import insightconnect_plugin_runtime
from .schema import GetIssueInput, GetIssueOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_issue
from insightconnect_plugin_runtime.exceptions import PluginException


class GetIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_issue",
            description=Component.DESCRIPTION,
            input=GetIssueInput(),
            output=GetIssueOutput(),
        )

    def run(self, params={}):
        """Get an issue by ID"""
        issue = self.connection.client.issue(id=params[Input.ID])
        get_attachments = params.get(Input.GET_ATTACHMENTS)

        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {params[Input.ID]}.",
                assistance="Please provide a valid issue ID.",
            )

        output = normalize_issue(
            issue=issue,
            get_attachments=get_attachments,
            include_raw_fields=True,
            logger=self.logger,
        )

        clean_output = insightconnect_plugin_runtime.helper.clean(output)
        return {Output.FOUND: True, Output.ISSUE: clean_output}
