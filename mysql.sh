# root create database
create database caesarFinal;
# root grand ruixin privilege
grant all privileges on caesarFinal.* to 'ruixin'@'%';
flush privileges;

# django connect mysql caesarFinal
python manage.py migrate

# pip install mysqlclient
sudo apt-get install python3-dev libmysqlclient-dev
pip install mysqlclient
