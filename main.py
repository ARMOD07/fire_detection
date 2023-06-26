import cv2
from playsound import playsound
 
 





fire_cascade=cv2.CascadeClassifier('fire_detection.xml')
 

#cap = cv2.VideoCapture('fire_capture.avi')
cap=cv2.VideoCapture(0)


while (True):
    

    ret, frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    fire=fire_cascade.detectMultiScale(frame,1.2,5)
    #x=La coordonnée horizontale du coin supérieur gauche  \
    # y=La coordonnée verticale du coin supérieur gauche de la détection de feu.\
    # w: La largeur de la détection de feu.
    # h: La hauteur de la détection de feu.
    
    for(x,y,w,h)in fire:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]    
        print('fire detecterd')
        playsound('fire_detection\\K44XEWK-alarm-fire-alarm-buzzer-01.mp3')

    cv2.imshow('AMIRA_CAM',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break