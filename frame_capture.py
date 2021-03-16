import numpy as np
import cv2
from os import listdir



vids = listdir('vids')

for vid in vids:
    label = vid
    vid = "vids/"+vid
    
    cap = cv2.VideoCapture(vid)
    count = 0
    number = 0
    print("start test")
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret and count == 30:
            file_name = label + str(number)+ ".jpg"
            number += 1
            cv2.imwrite(file_name,frame)
            count = 0
            cv2.imshow('frame',frame)
        elif ret:
            count += 1
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    print("end test")
    cap.release()
    cv2.destroyAllWindows()