
DATABASE_PASSWORD=rootDBPass#12

#remove existing Installation
#---------------------------------------------
echo 'removing previous mysql server installation and MariaDb'
sudo systemctl stop mysql.service  && sudo apt-get remove -y mysql-community-server && sudo rm -rf /var/lib/mysql && sudo rm -rf  /var/log/mysql.log && sudo rm -rf /etc/my.cnf 
sudo apt-get del mariadb* -y
sudo apt-get del mysql80-community-release.noarch -y

#------------------------------------------------------
#Set yum repository and Install Mysql community Server 

#------------------------------------------------------------------

echo 'Installing mysql server '
sudo apt-get install mysql-server

#--------------------------------------------
#Start Mysql server and grep temporary  password
echo 'starting mysql server for first time'

sudo systemctl start mysql.service 2> /dev/null
systemctl enable mysqld.service 2>/dev/null

temp_root_pass="sudo grep 'temporary.*root@localhost' /var/log/mysqld.log | tail -n 1 | sed 's/.*root@localhost: //'"

#set new password for root user 

echo 'setting up new mysql server root password'

mysql -u "root" --password="$temp_root_pass"  --connect-expired-password -e "alter user root@localhost identified by '${DATABASE_PASSWORD}'; flush privileges;"

#do the basic Hardening

mysql -u root  --password="$DATABASE_PASSWORD" -e "DELETE FROM mysql.user WHERE User=''; DROP DATABASE IF EXISTS test; DELETE FROM  mysql.db where Db='test' or Db='test\\_%'; FLUSH PRIVILEGES;"
sudo systemctl status mysqld.service

#perform a sanity chek
echo "sanity check: check if  password login works for root."
mysql -u root --password="$DATABASE_PASSWORD" -e quit

#enable firewall

echo "enabling firewall service"
sudo firewall-cmd --permanent --add-service=mysql 2>/dev/null
sudo firewall-cmd --reload 2>/dev/null

#final output 

echo "mysql server installation completed, root password: $DATABASE_PASSWORD";

