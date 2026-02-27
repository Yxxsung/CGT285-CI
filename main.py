#This is the main file for the composite imaging assignment for CGT 115 during spring 2026
#Sophia Alexander
#Last Edited: 02/26/26

#The goal is to take a character image, delete the background and put it on a new background

#This is the averaging code found in the assignment document
import pygame

# Initialize the game
pygame.init()

pygame.display.set_caption("Hello World")

img = pygame.image.load("prague.png")

img2 = pygame.image.load("winter.png")

width = img.get_width()

height = img.get_height()

screen = pygame.display.set_mode((width, height))

for y in range(0, height):
    for x in range(0, width):
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