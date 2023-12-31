import komand
import requests
from .schema import DeleteArtifactInput, DeleteArtifactOutput


class DeleteArtifact(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_artifact",
            description="Deletes an artifact.",
            input=DeleteArtifactInput(),
            output=DeleteArtifactOutput(),
        )

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        artifact_id = params.get("artifact_id")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/artifacts/{artifact_id}".format(
            org_id=org_id, inc_id=inc_id, artifact_id=artifact_id
        )

        self.logger.info("Deleting artifact %s on incident %s..." % (artifact_id, inc_id))
        try:
            response = self.connection.SESSION.delete(url)
            status = response.json()
            status = komand.helper.clean(status)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"status": status}

    def test(self):
        """TODO: Test action"""
        return {}
