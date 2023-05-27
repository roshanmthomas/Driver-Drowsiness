import cv2
import pygame

from drowsy_detection import VideoFrameHandler

# Set your desired thresholds
thresholds = {
    "WAIT_TIME": 2.0,  # Time to wait (in seconds) before triggering the alarm
    "EAR_THRESH": 0.3  # Eye Aspect Ratio threshold for drowsiness detection
}

# Create an instance of VideoFrameHandler
frame_handler = VideoFrameHandler()

# Initialize Pygame
pygame.init()

# Open the video capture
cap = cv2.VideoCapture(0)  # You can replace 0 with the path to a video file if you want to process a video

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    processed_frame, play_alarm = frame_handler.process(frame, thresholds)
    # Play alarm sound if play_alarm is True
    if play_alarm:
        # Code to play the alarm sound

        # Load the alarm sound file
        alarm_sound_path = r"/audio/wake_up.wav"
        pygame.mixer.music.load(alarm_sound_path)

        # Play the alarm sound
        pygame.mixer.music.play()

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            continue

    cv2.imshow("Drowsiness Detection", processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Quit Pygame
pygame.quit()
cap.release()
cv2.destroyAllWindows()
