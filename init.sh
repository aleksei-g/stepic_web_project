sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn.conf
sudo ln -s /home/box/web/etc/django.conf /etc/gunicorn.d/django.conf
sudo /etc/init.d/gunicorn restart
