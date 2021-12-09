# Trampa_Barcelo
La Trampas Barcelo  tiene como objetivo automatizar y optimizar la vigilancia de la presencia del mosquito Aedes Aegypti, para que el personal de fiscalización de plagas lo puedan hacer de manera ágil y eficaz.

# Configuración de la Raspberry PI:
# 1)Cronogramar el Script
La raspberry tendrá que tener instalado el script "Barcelo_Script.py" y se debe configurar el sistema operativo de tal forma para que se ejecute al encender el sistema.
Para realizar esta configuración seguirmeos los siguientes pasos...

1)Ejecutaremos el siguiente comando en el bash:

$ sudo crontab -e

2)Editaremos el archivo incluyendo al final del mismo lo siguiente:

@reboot sleep 10; python3 /home/pi/Desktop/WebCamScript.py

Nota: para guardar y cerrar esto se debe presionar "CTRL + O".

3)Ya concluido los pasos anteriores, reiniciaremos el sistema:

$ sudo reboot now

# 2)Vincular google drive a Raspberry Pi...
Fuente: https://raspberryparanovatos.com/tutoriales/rclone-google-raspberry-pi/
Para vincular el servicio de alojamiento de archivos de Google Drive con la Raspberry PI, se usará la aplicación RClone de Linux.
De esta manera se podrá vincular una carpeta del escritorio a la nube de Google, y allí almacenar todas las fotos que vaya sacando el sistema.

1) sudo apt update && sudo apt upgrade -y
2) sudo apt install fuse
3) sudo nano /etc/fuse.conf
Aquí tenemos que quitar la almohadilla (#) de la línea que pone user_allow_other. De forma que se quede como la imagen que tenemos a continuación.

4)curl https://rclone.org/install.sh | sudo bash
5)rclone config

6)mkdir gdrive
7)rclone mount –allow-non-empty gdrive: gdrive

8)mkdir -p ~/.config/systemd/user
9)nano ~/.config/systemd/user/rclone@.service
Copiar y pegar lo siguiente: 

[Unit]
Description=rclone: Remote FUSE filesystem for cloud storage config %i
Documentation=man:rclone(1)

[Service]
Type=notify
ExecStartPre=/bin/mkdir -p %h/mnt/%i
ExecStart= \
  /usr/bin/rclone mount \
    --config="%h/.config/rclone/rclone.conf" \
    --allow-other \
    --drive-acknowledge-abuse=true \
    --fast-list \
    --vfs-cache-mode writes \
    --vfs-cache-max-size 100M  \
    %i: %h/mnt/%i
ExecStop=/bin/fusermount -u -z %h/mnt/%i
ExecStop=/bin/rmdir %h/mnt/%i
Restart=on-failure
[Install]
WantedBy=default.target
