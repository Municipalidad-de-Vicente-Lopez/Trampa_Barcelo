import time
from picamera import Picamera
from time import sleep

i=1
tiempoCaptura = 21600
camara = Picamera()

while true:
  camara.start_preview()
  camara.capture("/home/pi/Pictures/captura"+str(i)+".jpg")
  camara.stop_preview()
  i=i+1
  time.sleep(tiempocaptura)
                 
