cp /var/www/nilms/nilms/config.json /tmp/nilms.json
rm -rf /var/www/nilms/nilms
mkdir -p /var/www/nilms/
mv nilms /var/www/nilms/.
cd /var/www/nilms/nilms

cp /tmp/nilms.json .

cp nilms.nginx /etc/nginx/sites-available/nilms.nginx
ln -s /etc/nginx/sites-available/nilms.nginx /etc/nginx/sites-enabled/.

cp nilms.service /etc/systemd/system/.

rm -rf ./venv
virtualenv -p /usr/bin/python2.7 ./venv
source ./venv/bin/activate
python setup.py develop; wait;
nilms-init

chown -R www-data:www-data /var/www/nilms

systemctl daemon-reload
systemctl restart nginx
systemctl restart nilms.service
