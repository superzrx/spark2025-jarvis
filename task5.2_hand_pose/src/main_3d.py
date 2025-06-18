# main_3d.py
import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Initialize MediaPipe Hands ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# --- Setup Matplotlib 3D plot ---
plt.ion() # Turn on interactive mode for real-time updates
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.05, right=0.85, bottom=0.05, top=0.95) # Adjust subplot to make room for colorbar

# Create an axes for the colorbar. This will be updated in the loop.
cbar_ax = fig.add_axes([0.87, 0.15, 0.03, 0.7])  # Position: [left, bottom, width, height]

# --- Main Logic ---
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while cap.isOpened():
        success, image = cap.read()
        if not success: 
            print("Ignoring empty camera frame.")
            continue

        h, w, _ = image.shape
        # Flip the image horizontally for a selfie-view display.
        image = cv2.flip(image, 1)
        # Convert the BGR image to RGB before processing.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)

        # Draw the 2D skeleton on the camera feed.
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('2D Camera Feed', image)

        # --- Core 3D Visualization Logic ---
        # Clear the previous frame's plot
        ax.cla() 
        ax.set_title('3D Hand Pose Tracking', fontsize=14, fontweight='bold')
        
        # Set axis labels and styles
        ax.set_xlabel('X', fontsize=12, labelpad=10)
        ax.set_ylabel('Y', fontsize=12, labelpad=10)
        ax.set_zlabel('Z', fontsize=12, labelpad=10)
        
        # Set a fixed axis range to prevent view jumping
        ax.set_xlim(-0.2, 0.2)
        ax.set_ylim(-0.2, 0.2)
        ax.set_zlim(-0.2, 0.2)
        
        # Set a better viewing angle
        ax.view_init(elev=30., azim=-45.)
        
        # Improve grid visibility
        ax.grid(True, linestyle='--', alpha=0.6)
        
        # Set a light gray background color
        ax.set_facecolor('#f0f0f0')

        # Default to None in case no hands are detected
        scatter = None

        if results.multi_hand_world_landmarks:
            # Process each detected hand
            for hand_world_landmarks in results.multi_hand_world_landmarks:
                # 1. Draw the 3D hand skeleton
                points = np.array([[lm.x, lm.y, lm.z] for lm in hand_world_landmarks.landmark])
                
                # Plot landmark points with a color gradient for depth
                scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], 
                            c=points[:, 2], cmap='viridis', 
                            marker='o', s=50, alpha=0.8)
                
                # Plot bone connections with thicker lines
                for connection in mp_hands.HAND_CONNECTIONS:
                    start_idx = connection[0]
                    end_idx = connection[1]
                    ax.plot([points[start_idx, 0], points[end_idx, 0]],
                            [points[start_idx, 1], points[end_idx, 1]],
                            [points[start_idx, 2], points[end_idx, 2]], 
                            'b-', linewidth=2, alpha=0.7)

                # 2. Calculate and draw the 3D pointing vector
                p_tip = points[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                p_base = points[mp_hands.HandLandmark.INDEX_FINGER_PIP]
                
                # Use ax.quiver to draw a 3D arrow
                ax.quiver(p_base[0], p_base[1], p_base[2],
                          p_tip[0] - p_base[0],
                          p_tip[1] - p_base[1],
                          p_tip[2] - p_base[2],
                          length=0.2, color='red', linewidth=3, normalize=True, 
                          arrow_length_ratio=0.15)
                
                # Add a label for the pointing vector
                ax.text(p_tip[0], p_tip[1], p_tip[2], "Pointing", 
                        color='red', fontsize=10, fontweight='bold')
        
        # Update the colorbar only if a scatter plot was created
        if scatter is not None:
            # Clear the previous colorbar
            cbar_ax.cla()
            # Create a new colorbar
            fig.colorbar(scatter, cax=cbar_ax, label='Z-Depth')

        # Redraw the canvas
        fig.canvas.draw_idle()
        plt.pause(0.001)

        # Exit on 'ESC' key press
        if cv2.waitKey(5) & 0xFF == 27:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    plt.ioff()
    plt.close()