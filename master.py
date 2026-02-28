#This is the master file for the composite imaging assignment for CGT 115 during spring 2026
#THIS FILE IS BASED ON THE ASSIGNMENT CODE NOT THE SLIDES CODE
#Sophia Alexander
#Last Edited: 02/26/26

#The goal is to take a character image, delete the background and put it on a new background

#This is the averaging code found in the assignment document
import pygame
from pygame.surface import Surface

from main import screen

# Initialize the game
pygame.init()

#This is what names the pop-up window
pygame.display.set_caption("Rey in Prague")

#defines background image
img = pygame.image.load("prague.png")

#defines character image and converts it to alpha to enable us to make it less transparent
img2 = pygame.image.load("Rey_green_screen.png").convert_alpha(screen)

width = img.get_width()

height = img.get_height()

#creates the display surface we'll be using to show us the image
screen = pygame.display.set_mode((width, height))

#sets the alpha to the max (255) to make it fully opaque
img2.set_alpha(255)

#This for loop recolors each pixel in the images. This is the original from the assignment!
for y in range(0, height-1):
    for x in range(0, width-207):
        c1 = img.get_at((x, y))
        c2 = img2.get_at((x, y))
        newcolor = ((c1.r + c2.r) // 2, (c1.g + c2.g) // 2, (c1.b + c2.b) // 2)
        img.set_at((x, y), newcolor)

screen.blit(img, (0, 0) )

pygame.display.flip()

pygame.image.save(img, "BW.png")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
