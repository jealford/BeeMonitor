import numpy as np
import cv2
import time
from datetime import datetime

time.sleep(5)

cap = cv2.VideoCapture(0)
width = 640
height = 480
cap_length = .10
cap.set(3, width)  # Set horizontal resolution
cap.set(4, height)  # Set vertical resolution
#cap.set(5, 30)  # Set vertical resolution
# Define the codec and create VideoWriter object*'MJPG'
fourcc = cv2.VideoWriter_fourcc(*'XVID' )

#print(cap.get(5))

for i in range(3):
    #./recordings/2021_02_26__09:47:32.avi
    current_time = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    file_out = '/home/pi/BeeMonitor/code/recordings/' + current_time + '.avi'
    out = cv2.VideoWriter(file_out,fourcc, 30.0, (width,height))
    t_end = time.time() + 60 * cap_length
    while time.time() < t_end:
        ret, frame = cap.read()
        if ret==True:
            #frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            #cv2.imshow('frame',frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break

        else:
            break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()