sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
  

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'root'"
mysql -uroot -e "CREATE DATABASE db"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'root'"

sudo pip install mysql
#cd ~
cd box/web/ask
python manage.py syncdb
