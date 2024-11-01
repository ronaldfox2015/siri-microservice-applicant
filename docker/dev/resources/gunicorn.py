bind = 'unix:/tmp/gunicorn.sock'
# Concurence for 4 users per container
worker_class = 'gevent'
workers = 1
threads = 2
errorlog = '-'
accesslog = None
reload = True
timeout = 60
keepalive = 5
