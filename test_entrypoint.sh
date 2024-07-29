#!/bin/bash
python -m unittest discover -s tests -t selenium_oxide/
exit $?