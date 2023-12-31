# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="cuckoo-rapid7-plugin",
      version="1.0.3",
      description="Cuckoo Sandbox is an open source automated malware analysis system. Using the Cuckoo Sandbox plugin for Rapid7 InsightConnect, users can analyze files and URLs, manage tasks, and more",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_cuckoo']
      )
