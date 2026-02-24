import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 30
graceful_timeout = 30
max_requests = 1000
max_requests_jitter = 50
accesslog = "-"
errorlog = "-"
loglevel = "info"
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
proc_name = "django_app"
preload_app = True
worker_tmp_dir = "/tmp"