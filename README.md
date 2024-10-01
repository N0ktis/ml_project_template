# ML Template

_A logical, reasonably standardized, but flexible project structure for doing and sharing out work._


### Requirements to use this template:
-----------
 - Python 3.7+
 - [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html)
 - zenlog

``` bash
pip3 install cookiecutter rich
```

### To start a new project, run:
------------

    cookiecutter git+ssh://git@gitlab.ptsecurity.com/ml-products-research/ml-template.git


### The resulting directory structure
------------

```
├── README.md               <- The top-level README for developers using this project.
│
├── pyproject.toml          <- Project metadata for [poetry](https://python-poetry.org/).
│
├── poetry.lock             <- Locked dependencies (instead of requirements.txt).
│
├── .pre-commit-config.yml  <- Git hooks to not commit bad code.
│
├── models                  <- Trained models (don't commit if not necessary).
│
├── notebooks               <- Jupyter notebooks. Naming convention is the creator's nickname
│   │                          and a short `-` delimited description, e.g.
│   │                          `nbarsukov-initial-data-exploration`.
│   ├── chaos               <- For exploration. Can be unstructured. Not autoformatted.
│   └── reports             <- For reports. Structured, clean and commented.
│
├── src                     <- Source code for use in this project.
│   ├── dataset.py          <- Module for creation and use of dataset.
│   │
│   ├── config.py           <- Configuration as python file for easier parsing and changing.
│   │
│   └── models              <- Scripts to train models and then use trained models to make
│       │                      predictions.
│       ├── train.py        <- Train.
│       └── predict.py      <- Predict.
│
├── Dockerfile              <- If your project can be built in Docker.
│
├── .gitlab-ci.yml          <- CI.
│
├── build_local.sh          <- Local build in docker container.
│
├── build_functions.sh      <- Functions for build_local.sh and .gitlab-ci.yml.
│
├── .env                    <- Credentials.
│
├── .gitignore              <- Ignore unwanted.
│
├── reports                 <- Useful information you don't want to lose in wiki or jira.
│
└── img                     <- Images used in Markdown files.
```


### Notes
`pyproject.toml` inside template goes without lock file because we may and may not include torch in dependencies.
For now poetry resolves dependencies in around 100 seconds so lock is not that necessary.
