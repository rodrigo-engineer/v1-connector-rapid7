import komand
from .schema import SubmitSampleInput, SubmitSampleOutput, Input, Output, Component

# Custom imports below
import base64
from komand.exceptions import PluginException


class SubmitSample(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_sample",
            description=Component.DESCRIPTION,
            input=SubmitSampleInput(),
            output=SubmitSampleOutput(),
        )

    def run(self, params={}):
        sample = params.get(Input.SAMPLE)

        # File handling
        try:
            file_bytes = base64.b64decode(sample["content"])
        except KeyError as e:
            raise PluginException(cause="The sample file is empty.", assistance="Please check your input.", data=e)
        except Exception as e:
            raise PluginException(cause=PluginException.Preset.BASE64_DECODE, data=e)

        is_private = params.get(Input.PRIVATE)
        if not isinstance(is_private, bool):
            is_private = True

        filename = params.get(Input.SAMPLE_FILENAME)
        if not filename:
            filename = sample.get("filename")

        data = {
            "callback_url": params.get(Input.CALLBACK_URL),
            "email_notification": params.get(Input.EMAIL_NOTIFICATION),
            "network_exit": params.get(Input.NETWORK_EXIT),
            "playbook": params.get(Input.PLAYBOOK),
            "private": is_private,
            "sample_filename": filename,
            "sample_password": params.get(Input.SAMPLE_PASSWORD),
            "tags": params.get(Input.TAGS),
            "vm": params.get(Input.VM),
        }
        files = {"sample": file_bytes}
        return {Output.RESULTS: komand.helper.clean(self.connection.api.submit_sample(data=data, files=files))}
