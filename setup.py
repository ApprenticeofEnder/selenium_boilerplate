# [metadata]
# name = selenium-oxide-enderthenetrunner
# version = 0.0.1
# author = Robert Babaev
# author_email = mail@robertbabaev.tech
# description = A Selenium boilerplate for automating web exploits. Use responsibly and ethically.
# long_description = file: README.md
# long_description_content_type = text/markdown
# url = https://github.com/ApprenticeofEnder/Selenium-Oxide
# project_urls =
#     Bug Tracker = https://github.com/ApprenticeofEnder/Selenium-Oxide/issues
# classifiers =
#     Programming Language :: Python :: 3
#     License :: OSI Approved :: MIT License
#     Operating System :: OS Independent

# [options]
# package_dir =
#     = src
# packages = find:
# python_requires = >=3.7

# [options.packages.find]
# where = src

import os
from distutils.core import setup

from setuptools import find_packages

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""
setup(
    # Project name:
    name="selenium-oxide",
    # Packages to include in the distribution:
    packages=["selenium_oxide"],
    # Project version number:
    version="2.0.0",
    # List a license for the project, eg. MIT License
    license="MIT License",
    # Short description of your library:
    description="A framework for automating web exploits with Selenium and Python. Use responsibly and ethically.",
    # Long description of your library:
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Your name:
    author="Robert Babaev",
    # Your email address:
    author_email="github@robertbabaev.tech",
    # Link to your github repository or website:
    url="https://github.com/ApprenticeofEnder/Selenium-Oxide",
    # Download Link from where the project can be downloaded from:
    download_url="https://github.com/ApprenticeofEnder/Selenium-Oxide",
    # List of keywords:
    keywords=["Selenium", "Web", "Offensive Security"],
    # List project dependencies:
    install_requires=["selenium ~= 4.1.3", "Faker >= 13.15.1", "requests >= 2.28.1"],
    # https://pypi.org/classifiers/
    classifiers=[],
)
