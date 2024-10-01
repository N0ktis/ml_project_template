#!/usr/bin/env python
"""
cookiecutter currently has no way to automatically add submodule to template, so
use ad-hoc script for it.
"""

import subprocess
import sys
from pathlib import Path

from rich.console import Console

log = Console().log


def check_python_version():
    # check installed python versions
    installed_versions = subprocess.check_output("pyenv versions", shell=True).decode('utf-8').split('\n')
    installed_versions_norm = [version.strip() for version in installed_versions]

    if "{{ cookiecutter.project_python_version }}" in installed_versions_norm:
        log("Python {{ cookiecutter.project_python_version }} exists")
    else:
        log("Python {{ cookiecutter.project_python_version }} cannot be founded in `~/.pyenv/versions`. \nRun 'pyenv install {{ cookiecutter.project_python_version }}' to install required version of python")
        sys.exit(1)  # stop project initialization to prevent error in poetry env


if __name__ == "__main__":
    log("Checking python version")
    check_python_version()
