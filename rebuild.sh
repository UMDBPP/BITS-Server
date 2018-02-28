#!/bin/bash
source venvs/venv-bits/bin/activate
pip install -e .
supervisorctl restart bits-server
