FROM rapid7/insightconnect-python-3-38-plugin:5

LABEL organization=komand

# Add any custom package dependencies here
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

USER nobody

ENTRYPOINT ["/usr/local/bin/komand_recorded_future"]
