#/usr/bin/bash

#update the resolution
sudo apt update 

#upgrade 
#sudo apt upgrade 

# change your hostname
sudo hostname set-hostname mail.

#hostname

sudo hostnamectl set-hostname mail.

#installing iredmail

cd Téléchargements
cd iRedMail-1.5.2

#configuration the iredmail
sudo bash iRedMail.sh

 
