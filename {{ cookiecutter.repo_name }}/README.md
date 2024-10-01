# {{ cookiecutter.project_name }}
==============================

{{ cookiecutter.description }}

## Project Structure

## Build
Put your Artifactory credentials in .env. It's `.gitignore`-ed so you won't commit them by accident.
```
ARTIFACTORY_USERNAME=...
ARTIFACTORY_PASSWORD=...
```

### Local build
```
poetry install --dev
pre-commit install
```

#### Train
```
poetry run train
```

#### Predict
```
poetry run predict
```

### In docker
```
bash build_local.sh
```

