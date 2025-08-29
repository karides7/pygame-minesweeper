import pygame, random, math

pygame.init()
pygame.font.init()

pixelLetters = pygame.font.Font('assets/pixel_letters.ttf', 40)

clock = pygame.time.Clock()
clock.tick(30)

windowSize = (800, 800)