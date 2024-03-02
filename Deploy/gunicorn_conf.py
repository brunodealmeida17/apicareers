from multiprocessing import cpu_count


# Socket Path
bind = 'unix:/tmp/gunicorn_APP_NAME.sock'


# Worker Options
workers = 1

# Logging Options
loglevel = 'debug'
accesslog = 'APP_PWD/logs/gunicorn/access_log'
errorlog =  'APP_PWD/logs/gunicorn/error_log'


raw_env = [
    "DJANGO_DEBUG=False",
    "DJANGO_SECRET_KEY=TOKEN"
]
