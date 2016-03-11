sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn.conf
sudo ln -s /home/box/web/etc/django.conf /etc/gunicorn.d/django.conf
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql restart
mysql -u root -e "create database Ask_db"
cd /home/box/web/ask/
#sudo python manage.py makemigrations qa
#sudo python manage.py migrate
python manage.py syncdb
