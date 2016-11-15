sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/gunicorn-wsgi.conf
sudo /etc/init.d/gunicorn restart﻿﻿
#gunicorn -с /etc/gunicorn.d/gunicorn-wsgi.py hello:app
