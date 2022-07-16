# Trampa_Barcelo
La Trampas Barcelo  tiene como objetivo automatizar y optimizar la vigilancia de la presencia del mosquito Aedes Aegypti, para que el personal de fiscalización de plagas lo puedan hacer de manera ágil y eficaz.[Link al White Paper](https://docs.google.com/presentation/d/1T5CdcLSzgRe8cQpoi_sPB4U170551NGOrZNykcJD0xU/edit?usp=sharing)
![DemoBarcelo](https://user-images.githubusercontent.com/34106936/164496704-9e4ce7b8-644e-4b4a-9edf-5d5fb1295925.gif)

# Configuración de la Raspberry PI:
## 1)Cronogramar el Script
La raspberry tendrá que tener instalado el script "Barcelo_Script.py" y se debe configurar el sistema operativo de tal forma para que se ejecute al encender el sistema.
Para realizar esta configuración seguirmeos los siguientes pasos...

1)Ejecutaremos el siguiente comando en el bash:
```
$ sudo crontab -e
```
2)Editaremos el archivo incluyendo al final del mismo lo siguiente:
```
@reboot sleep 60; python3 /home/pi/Desktop/Barcelo_Script.py
```
Nota: para guardar y cerrar esto se debe presionar "CTRL + O".

3)Ya concluido los pasos anteriores, reiniciaremos el sistema:
```
$ sudo reboot now
```
## 2)Vincular google drive a Raspberry Pi...
Fuente: https://raspberryparanovatos.com/tutoriales/rclone-google-raspberry-pi/
Para vincular el servicio de alojamiento de archivos de Google Drive con la Raspberry PI, se usará la aplicación RClone de Linux.
De esta manera se podrá vincular una carpeta del escritorio a la nube de Google, y allí almacenar todas las fotos que vaya sacando el sistema.

1)  ```sudo apt update && sudo apt upgrade -y```
2) ```sudo apt install fuse```
3) ```sudo nano /etc/fuse.conf```
Aquí tenemos que quitar la almohadilla (#) de la línea que pone user_allow_other. De forma que se quede como la imagen que tenemos a continuación.

4)```curl https://rclone.org/install.sh | sudo bash```
5)```rclone config```

6)```mkdir gdrive```
7)```rclone mount –allow-non-empty gdrive: gdrive```

8)```mkdir -p ~/.config/systemd/user```
9)```nano ~/.config/systemd/user/rclone@.service```

Copiar y pegar lo siguiente: 
```
[Unit]
Description=rclone: Remote FUSE filesystem for cloud storage config %i
Documentation=man:rclone(1)
```

[Service]
```
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
```
[Install]
WantedBy=default.target
# Entramiento
## 1)Base de datos:
Se encuentra en Google Drive, se recomienda que ustedes hagan una copia en su perfil, el formato esta en .zip ya que asi se espera en el google colab para poder trabajar, la base de datos se ira actualizando [clik](https://drive.google.com/file/d/1_DBkt7YAei8rbQK5Nzvezl0AF4G7x9RF/view?usp=sharing)
## 2)Entrenamiento en la Nube
Se decidió usar google colab, debido a que porrpociona una maquina virtual gratuita por unas horas, subimos el archivo Barcelo_YOLOv5_Train.ipynb o pueden ingresar directamente a nuestro colab . Prestar Atención!!! tienen que desacargar el archivo de la base de datos y subirlo a su cuenta del Google Drive [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fbeB71yD09WK2JG9P3Ladu9MEzQ2rQad?usp=sharing). Luego tiene que subir el archivo customcoco128drive.yaml al google drive dentro de la carpeta yolov5/data, lo que hace este coordinar la información del etiquetado con el entrenamiento de Yolov5 .
Luego la red entrenada genera una archivo best.pt que se encuentra aqui runs/train/exp/weights/best.pt, hay que descargar el mismo 
# Deploy
## 1) Google Colab:
Para hacer un puesta en producción rápido ofrecemos un[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1othxk0GPSFzQDGskWWky45uw4ohLIGYN?usp=sharing), previamente hay que subir la red entrenada, que obtuvimos en el paso anterior que se llama best.pt .
Nota; este producto solo durará unas horas ya que esta limitado por el uso de google colab
## 2) HugginFace:
Si se desea tener un modelo en la nube de manera permanente y gratuita le ofrecemos una versión en HuggingFace, el código se encuentra libre en la misma plataforma [Link Deploy](https://hf.space/embed/cesar/demoIAZIKA/+)
# Citación
Por favor si usas la base de datos o el código 
```
@article{Trampas Barceló,
  title = {Trampas Barceló: Detección y monitoreo a tiempo real del mosquito Aedes aegypti},
  author = {Riat, César  and Schieder, Mario },
  
  year = {2021}
}
```
# Contacto 
Para mas información por favor contactarse a cesar.riat@vicentelopez.gov.ar

