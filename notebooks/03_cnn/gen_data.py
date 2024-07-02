import cv2
import numpy as np
import time
import os

vid = cv2.VideoCapture(0)  # Use 0 for default camera, or replace with video file path

print('Enter letter:')
userLetter = input()

letter_dir = f'../../model/real_data/{userLetter}/'
os.makedirs(letter_dir, exist_ok=True)

count = 1
# Save the frames
while True:
    
    # Capture a single frame
    ret, frame = vid.read()
    if ret: 
        cv2.imshow('Letter', frame)
            
        key = cv2.waitKey(1) & 0xFF
        # Press 's' on the keyboard to start 
        if key == ord('s'):
            cv2.destroyWindow('Letter')

            for x in range(1, 11):
                # to capture movement (add noise)
                ret, frame = vid.read()
                if not ret:
                    print("Failed to capture frame from camera. Exiting...")
                    break

                grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                targ_frame = cv2.resize(grey_frame, (28, 28))
                
                # Display the captured frame
                cv2.imshow('NEW', frame)

                # Save the frame
                file_path = f'{letter_dir}/{x}.jpg'
                cv2.imwrite(file_path, targ_frame)
                print(f'Captured frame {x}')

                time.sleep(1.0)
            
            break

        elif key == ord('q'):
            break

# Release the capture object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
