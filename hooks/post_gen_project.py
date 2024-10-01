#!/usr/bin/env python
"""
cookiecutter currently has no way to automatically add submodule to template, so
use ad-hoc script for it.
"""

import subprocess
from pathlib import Path

from rich.console import Console

log = Console().log


def init_poetry():
    subprocess.call(["poetry", "install"])


def create_ipython_kernel():
    subprocess.call(
        [
            "poetry",
            "run",
            "ipython",
            "kernel",
            "install",
            "--user",
            "--name={{ cookiecutter.repo_name }}",
        ]
    )


if __name__ == "__main__":
    log("Project initialization done.")

    log("Initializing poetry environment")
    init_poetry()

    log("Creating ipython kernel so you can use your poetry env from jupyter")

    create_ipython_kernel()

    log("Ipython kernel created. Use it for your pleasure!")
