FROM rapid7/insightconnect-python-3-38-plugin:4

LABEL organization=rapid7
LABEL sdk=python
LABEL type=plugin


# Add any custom package dependencies here
RUN apt-get update && apt-get install curl -y
# NOTE: Add pip packages to requirements.txt

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_samanage"]