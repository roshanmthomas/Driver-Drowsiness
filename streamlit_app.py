import cv2
import streamlit as st

from drowsy_detection import VideoFrameHandler

# Set your desired thresholds
thresholds = {
    "WAIT_TIME": 2.0,  # Time to wait (in seconds) before triggering the alarm
    "EAR_THRESH": 0.3  # Eye Aspect Ratio threshold for drowsiness detection
}

# Create an instance of VideoFrameHandler
frame_handler = VideoFrameHandler()

# Open the video capture
cap = cv2.VideoCapture(0)  # You can replace 0 with the path to a video file if you want to process a video

# Initialize the alarm flag
play_alarm = False

# Streamlit app title and description
st.title("Driver Drowsiness Detection")
st.markdown("This app detects drowsiness of a driver in real-time.")

# Display the video frame and process it
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    processed_frame, play_alarm = frame_handler.process(frame, thresholds)

    # Display the processed frame
    st.image(processed_frame, channels="BGR", use_column_width=True)

    # Simulate the alarm behavior
    if play_alarm:
        st.warning("ALERT: Drowsiness Detected!")  # Display a warning message

    if st.button("Quit"):
        break

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
