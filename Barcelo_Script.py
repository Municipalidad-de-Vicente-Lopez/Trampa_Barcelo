import cv2
import time
import os

cam = cv2.VideoCapture(0)
path = "/home/pi/mnt/googledrive"
i=7
tiempo= 43200 #43200 segundos = 12 horas.

#-Resolucion de la imagen-
cam.set(3, 2560)
cam.set(4, 1600)

time.sleep(10)
image = cam.read()[1]
time.sleep(10)
cv2.imwrite(os.path.join(path,"captura"+"1.png"),image)
time.sleep(10)
image = cam.read()[1]
time.sleep(10)
cv2.imwrite(os.path.join(path,"captura"+"2.png"),image)
time.sleep(10)
image = cam.read()[1]
time.sleep(10)
cv2.imwrite(os.path.join(path,"captura"+"3.png"),image)
time.sleep(10)
image = cam.read()[1]
time.sleep(10)
cv2.imwrite(os.path.join(path,"captura"+"4.png"),image)
time.sleep(10)
image = cam.read()[1]
time.sleep(10)
cv2.imwrite(os.path.join(path,"captura"+"5.png"),image)
time.sleep(10)
image = cam.read()[1]
time.sleep(10)
cv2.imwrite(os.path.join(path,"captura"+"6.png"),image)

while True:
    image = cam.read()[1]
    cv2.imwrite(os.path.join(path,"captura"+str(i)+".png"),image)
    time.sleep(tiempo)
    i = i+1
