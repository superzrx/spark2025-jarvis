# main_2d.py
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Use 'with' statement to properly manage resources
with mp_hands.Hands(
    model_complexity=0, # Model complexity: 0 for fastest
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    # Start webcam capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Get image dimensions
        h, w, _ = image.shape
        # Flip the image horizontally for a natural selfie-view
        image = cv2.flip(image, 1)
        # Convert the BGR image to RGB for MediaPipe
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image to get hand landmarks
        results = hands.process(rgb_image)

        # Draw the hand annotations on the image
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the hand skeleton
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                # --- Calculate and draw the pointing vector ---
                # Get coordinates for the tip and base of the index finger
                p_tip_2d = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                p_base_2d = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
                
                # Convert normalized coordinates to pixel coordinates
                base_pixel = (int(p_base_2d.x * w), int(p_base_2d.y * h))
                tip_pixel = (int(p_tip_2d.x * w), int(p_tip_2d.y * h))
                
                # Calculate an extended end point for the arrow for better visualization
                arrow_end_x = base_pixel[0] + (tip_pixel[0] - base_pixel[0]) * 2
                arrow_end_y = base_pixel[1] + (tip_pixel[1] - base_pixel[1]) * 2
                
                # Draw the arrow on the image
                cv2.arrowedLine(image, base_pixel, (arrow_end_x, arrow_end_y), 
                                (0, 0, 255), 5) # Red arrow with thickness 5

        # Display the resulting frame
        cv2.imshow('2D Hand Tracking with Pointing Vector', image)

        # Exit on 'ESC' key press
        if cv2.waitKey(5) & 0xFF == 27:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()