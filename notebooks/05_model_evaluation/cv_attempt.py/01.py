import cv2
import numpy as np
import time
import os

vid = cv2.VideoCapture(0)  # Use 0 for default camera, or replace with video file path

print('Enter letter:')
userLetter = input()

letter_dir = f'../../model/real_data/{userLetter}/'
model = ('../../model/my_files/my_CNN_model_13.1.h5')
os.makedirs(letter_dir, exist_ok=True)

count = 1
# Save the frames
while True:
    
    # Capture a single frame
    ret, frame = vid.read()
    if ret: 
        cv2.imshow('Letter', frame)
            
        roi = frame[100:400, 320:620]
        cv2.imshow('roi', roi)

        roi= cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        copy = frame.copy()
        cv2.rectangle(copy,(320,100),(620,400),(255,0,0),2)

        roi= roi.reshape(1,28,28,1)

        result = model.predict(roi)

        if cv2.waitKey(1) == 'q':
            break
# Release the capture object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
