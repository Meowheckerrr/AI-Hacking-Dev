import pygame
import time 

def speaking(mindTextPath):
    pygame.mixer.init()
    pygame.mixer.music.load(mindTextPath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  #getbusy used to check if music is already playing or not
        time.sleep(0.5) # time for waiting specking End 
