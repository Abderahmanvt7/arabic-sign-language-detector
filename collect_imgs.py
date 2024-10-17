import os
import cv2
import sys

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 30
dataset_size = 50

# Try different camera indices
for camera_index in range(10):  # Try indices 0 to 9
    cap = cv2.VideoCapture(camera_index)
    if cap.isOpened():
        print(f"Successfully opened camera with index {camera_index}")
        break
    cap.release()
else:
    print("Could not open any camera")
    sys.exit(1)

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)
    
    print(f'Collecting data for class {j}')
    
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Failed to capture frame. Exiting.")
            sys.exit(1)
        
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break
    
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Failed to capture frame. Skipping.")
            continue
        
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        
        counter += 1
        print(f"Captured image {counter}/{dataset_size} for class {j}", end='\r')
    print()  # New line after counter

cap.release()
cv2.destroyAllWindows()