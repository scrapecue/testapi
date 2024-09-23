# flake8: noqa

import os

bind = "0.0.0.0:8455"
workers = os.environ.get("gunicorn_workers", 1)
threads = os.environ.get("gunicorn_threads", 1)
worker_class = "uvicorn.workers.UvicornWorker"
log_config = None
