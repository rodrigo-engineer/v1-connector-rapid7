import insightconnect_plugin_runtime
from .schema import AttachIssueInput, AttachIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AttachIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="attach_issue",
            description=Component.DESCRIPTION,
            input=AttachIssueInput(),
            output=AttachIssueOutput(),
        )

    def run(self, params={}):
        """Add attachment to issue"""
        id_ = params[Input.ID]
        issue = self.connection.client.issue(id=id_)

        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {id_}.",
                assistance="Please provide a valid issue ID.",
            )

        return {
            Output.ID: self.connection.rest_client.add_attachment(
                issue.key, params.get(Input.ATTACHMENT_FILENAME), params.get(Input.ATTACHMENT_BYTES)
            )
        }
