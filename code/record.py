import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object*'MJPG'
fourcc = cv2.VideoWriter_fourcc(*'XVID' )
out = cv2.VideoWriter('./recordings/output.avi',fourcc, 30.0, (640,480))

t_end = time.time() + 60 * .15

while time.time() < t_end:
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()