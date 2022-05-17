#Isaac Alejandro Gutiérrez Huerta 19110198 7E1
#Sistemas de Visión Artificial

import cv2
import numpy as np

#------------------------------DIBUJOS-----------------------#

imgN=0*np.ones((580,880,3),dtype=np.uint8)

cv2.line(imgN,(100, 100), (700, 500), (3,61,176),3)
cv2.rectangle(imgN,(400,80),(600,200),(192,79,31),6)
cv2.circle(imgN,(200,400),80,(42,26,185),9)
cv2.putText(imgN,'Isaac Gutierrez. Practica 4 Vision Artificial', (60,290), 3, 1, (255,255,255),2,cv2.LINE_AA)

pts = np.array ([[80, 80], [60, 60], [100, 40], [140, 60], [120, 80]], np.int32) # conjunto de vértices
pts = pts.reshape((-1, 1, 2))
cv2.polylines(imgN, [pts], True, (199, 15, 113),2)

#------------------------------ROI---------------------------#

#Seleccionamos la imagen
roi = cv2.selectROI('Practica 4',imgN)

#Recortamos la imagen con ayuda de las coordenadas obtenidas en roi
recorteROI = imgN[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#Mostramos el recorte
cv2.imshow("ROI", recorteROI)

cv2.waitKey(0)
cv2.destroyAllWindows()
