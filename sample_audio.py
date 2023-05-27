import pygame

# Initialize Pygame
pygame.init()

# Load the alarm sound file
alarm_sound_path = r"/audio/wake_up.wav"
pygame.mixer.music.load(alarm_sound_path)

# Play the alarm sound
pygame.mixer.music.play()

# Wait for the sound to finish playing
while pygame.mixer.music.get_busy():
    continue

# Quit Pygame
pygame.quit()
