# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="typo_squatter-rapid7-plugin",
      version="1.0.2",
      description="Detect cybersquatting of domains to aid in phishing investigation and analysis",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_typo_squatter']
      )