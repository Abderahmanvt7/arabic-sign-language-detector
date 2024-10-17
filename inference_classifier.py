import pickle
import sys
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Load the model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# Initialize camera
for camera_index in range(10):  # Try indices 0 to 9
    cap = cv2.VideoCapture(camera_index)
    if cap.isOpened():
        print(f"Successfully opened camera with index {camera_index}")
        break
    cap.release()
else:
    print("Could not open any camera")
    sys.exit(1)

# Initialize Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Labels dictionary for Arabic characters
labels_dict = {0: 'ا', 1: 'ب', 2: 'ت', 3: 'ث', 4: 'ج', 5: 'ح', 6: 'خ', 7: 'د', 8: 'ذ', 9: 'ر', 10: 'ز', 11: 'س', 12: 'ش', 13: 'ص', 14: 'ض', 15: 'ط', 16: 'ظ', 17: 'ع', 18: 'غ', 19: 'ف', 20: 'ق', 21: 'ك', 22: 'ل', 23: 'م', 24: 'ن', 25: 'ه', 26: 'و', 27: 'ى', 28: 'ي', 29: 'لا'}

# Load Arabic font using Pillow 
font_path = "fonts/NotoSansArabic-VariableFont_wdth,wght.ttf" 
font = ImageFont.truetype(font_path, 32)

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        if len(data_aux) == 42:  # Ensure data_aux has exactly 42 features
            x1 = int(min(x_) * W)
            y1 = int(min(y_) * H)
            x2 = int(max(x_) * W)
            y2 = int(max(y_) * H)

            # Make prediction
            prediction = model.predict(np.asarray(data_aux).reshape(1, -1))
            predicted_character = labels_dict[int(prediction[0])]

            # Create an image with Arabic text using Pillow
            img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Convert frame to PIL image
            draw = ImageDraw.Draw(img_pil)
            
            # Calculate position for text at the bottom center of the screen
            left, top, right, bottom = draw.textbbox((0, 0), predicted_character, font=font)
            text_width = right - left
            text_height = bottom - top
            text_x = (W - text_width) // 2
            text_y = H - text_height - 40  # 20 pixels from the bottom

            # Draw text
            draw.text((text_x, text_y), predicted_character, font=font, fill=(255, 255, 255))  # White text

            # Convert back to OpenCV image
            frame = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

            # Draw rectangle around the hand
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)

    # Show the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()