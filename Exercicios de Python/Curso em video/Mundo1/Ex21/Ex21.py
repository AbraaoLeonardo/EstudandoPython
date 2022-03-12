import pygame
print(pygame.version)
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Lesson_1.mp3')
pygame.mixer.music.play()
pygame.event.wait()