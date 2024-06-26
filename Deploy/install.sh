#!/bin/bash

# Script de configuração para o projeto Django com Celery, Redis, Django Channels e Gunicorn

# Capturar o diretório atual

APP_NAME='apicareers'


mv APP_NAME.env $APP_NAME.env
mv APP_NAME.service $APP_NAME.service
mv APP_NAME $APP_NAME

cd ../..

echo "Digite a SERVE_name:"
read uri
SERVER_NAME="$uri"

echo "Digite a PORTA:"
read porta
SERVER_PORT=$porta

sudo mkdir /opt
sudo chmod a+rwxX /opt
sudo mv ./$APP_NAME /opt/$APP_NAME

cd /opt/$APP_NAME/
CURRENT_DIR=$(pwd)


sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000

sudo groupadd $APP_NAME
sudo useradd -s /sbin/nologin --system -g $APP_NAME $APP_NAME
sudo usermod -aG ubuntu $APP_NAME

mkdir logs
mkdir logs/gunicorn
mkdir logs/celery

sudo touch $CURRENT_DIR/logs/gunicorn/access_log
sudo touch $CURRENT_DIR/logs/gunicorn/error_log
sudo chown -R $APP_NAME:$APP_NAME $CURRENT_DIR/logs/gunicorn/
sudo chmod -R g+w $CURRENT_DIR/logs/gunicorn/

TOKEN=`cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-96} | head -n 1`

# Instale as dependências do sistema
sudo apt-get update
sudo apt-get install -y nginx python3.10-venv redis-server python3-pip

# Configuração do projeto Django
# Configure o ambiente virtual e ative-o
python3 -m venv env
source env/bin/activate


# Instale as dependências do projeto
pip install -r requirements.txt

cd src/
# Execute as config of Django
export DJANGO_DEBUG=True
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
cd ..

#GUNICORN
sed -e "s|APP_PWD|$CURRENT_DIR|g" -i $CURRENT_DIR/Deploy/gunicorn_conf.py
sed -e "s|TOKEN|$TOKEN|g" -i $CURRENT_DIR/Deploy/gunicorn_conf.py
sed -e "s|APP_NAME|$APP_NAME|g" -i $CURRENT_DIR/Deploy/gunicorn_conf.py
mv $CURRENT_DIR/Deploy/gunicorn_conf.py $CURRENT_DIR/src/

sed -e "s|APP_PWD|$CURRENT_DIR|g" -i $CURRENT_DIR/Deploy/$APP_NAME.service
sed -e "s|APP_NAME|$APP_NAME|g" -i $CURRENT_DIR/Deploy/$APP_NAME.service
sudo mv $CURRENT_DIR/Deploy/$APP_NAME.service /etc/systemd/system/

#nginx
sed -e "s|APP_PWD|$CURRENT_DIR|g" -i $CURRENT_DIR/Deploy/$APP_NAME
sed -e "s|SERVER_NAME|$SERVER_NAME|g" -i $CURRENT_DIR/Deploy/$APP_NAME
sed -e "s|PORTA_SERVER|$SERVER_PORT|g" -i $CURRENT_DIR/Deploy/$APP_NAME
sed -e "s|APP_NAME|$APP_NAME|g" -i $CURRENT_DIR/Deploy/$APP_NAME

sudo mv $CURRENT_DIR/Deploy/$APP_NAME /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled/


#env
sed -e "s|TOKEN|$TOKEN|g" -i $CURRENT_DIR/Deploy/$APP_NAME.env
mv $CURRENT_DIR/Deploy/$APP_NAME.env $CURRENT_DIR/

# init the service of Gunicorn
sudo systemctl start $APP_NAME.service
sudo systemctl enable $APP_NAME.service
sudo systemctl status $APP_NAME.service

# restart the service of Nginx
sudo systemctl restart nginx
sudo systemctl status nginx


# Run Certbot for SSL/TLS certificate
#sudo certbot --nginx -d tubedownloads.online
