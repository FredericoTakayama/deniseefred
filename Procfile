release: python weddingsite/manage.py migrate
web: gunicorn weddingsite.wsgi --pythonpath '/app/weddingsite' --log-file -
