# Trampa_Barcelo
La Trampas Barcelo  tiene como objetivo automatizar y optimizar la vigilancia de la presencia del mosquito Aedes Aegypti, para que el personal de fiscalización de plagas lo puedan hacer de manera ágil y eficaz.

Configuración de la Raspberry PI:
La raspberry tendrá que tener instalado el script "Barcelo_Script.py" y se debe configurar el sistema operativo de tal forma para que se ejecute al encender el sistema.
Para realizar esta configuración seguirmeos los siguientes pasos...

1)Ejecutaremos el siguiente comando en el bash:

$ sudo crontab -e

2)Editaremos el archivo incluyendo al final del mismo lo siguiente:

@reboot sudo python /home/pi/Desktop/Barcelo_Script.py

Nota: para guardar y cerrar esto se debe presionar "CTRL + O".

3)Ya concluido los pasos anteriores, reiniciaremos el sistema:

$ sudo reboot now
