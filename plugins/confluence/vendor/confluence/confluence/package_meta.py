# Do not import anything except from standard lib and setuptools,
# as this is getting imported by the setup script
from pkg_resources import parse_version
import subprocess  # noqa: B404
import os
import re
import datetime
import logging

# Add any variable which needs to be in the init to __all__
__all__ = ("__version__", "__author__", "__contact__", "__homepage__", "__license__")

# Base version, from which to determine the dynamic version
BASE_VERSION = "0.2"
# Other metadata
__author__ = "Sorin Sbarnea"
__copyright__ = "Copyright 2010-2016, Sorin Sbarnea"
__email__ = "sorin(dot)sbarnea(at)gmail.com"
__status__ = "Beta"
__contact__ = __author__
__homepage__ = "https://github.com/pycontribs/confluence"
__license__ = "BSD"
__date__ = "2016-08-05"


# setup call metadata parameters
setup_metadata = {
    "author": __author__,
    "author_email": __contact__,
    "maintainer_email": __contact__,
    "url": __homepage__,
    "license": __license__,
    "description": __doc__,
}


def get_version(base_version=BASE_VERSION):
    base_version = parse_version(base_version)

    version = base_version.base_version
    if base_version.is_prerelease or is_prerelease_branch():
        git_changeset = get_git_changeset()
        if git_changeset:
            return "{}.dev{}".format(version, git_changeset)

    return str(base_version)


def is_prerelease_branch():
    branch = get_git_branch()
    # If we can't get a branch (None), we need to assume it is a release,
    # as the installed version won't have git
    if branch in ("master", "stable", None) or branch.startswith("release/"):
        return False
    return True


def run_but_ignore_errors(*args, **kwargs):
    # if git is not installed, or there is not git repo,
    # we use the version as is. We don't want any errors
    with open(os.devnull, "w") as devnull:
        try:
            return subprocess.check_output(*args, shell=True, stderr=devnull, **kwargs)  # noqa: B602
        except (subprocess.SubprocessError, FileNotFoundError, OSError):
            return None
        except Exception:
            logger = logging.getLogger(__name__)
            logger.exception("Unexpected exception")
            return None


def get_git_branch():
    # Jenkins may not do a full checkout so we use the branch reported
    # via env variables.
    repo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    branch = os.environ.get("GIT_BRANCH", os.environ.get("BRANCH_NAME"))
    if branch:
        # Git Plugin specifies a format for branch name,
        # but our experience prooved that in many case we may not get the 'origin/' part.
        # https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin
        if branch.startswith("origin/"):
            branch = branch[len("origin/") :]
        return branch
    else:
        output = run_but_ignore_errors("git branch", cwd=repo_dir)
        if output:
            branch = re.findall(r"^\*\s+(.*)$", output.decode("utf-8"), re.MULTILINE)
            if branch:
                return branch[0]


def get_git_changeset():
    repo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    timestamp = run_but_ignore_errors("git log --pretty=format:%ct --quiet -1 HEAD", cwd=repo_dir)
    try:
        timestamp = datetime.datetime.utcfromtimestamp(int(timestamp))
    except (ValueError, TypeError):
        return None
    return timestamp.strftime("%Y%m%d%H%M%S")


__version__ = get_version()
setup_metadata["version"] = __version__
