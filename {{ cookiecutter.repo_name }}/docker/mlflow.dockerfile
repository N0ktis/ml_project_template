ARG PYTHON_VERSION=3.8.0-slim
FROM python:$PYTHON_VERSION
WORKDIR /mlflow/

ARG MLFLOW_VERSION=2.5.0
RUN pip install mlflow==$MLFLOW_VERSION

CMD mlflow server \
  --backend-store-uri sqlite:///mlflow.sqlite \
  --artifacts-destination file:///artifacts \
  --serve-artifacts \
  --host 0.0.0.0
