#This is the main file for the composite imaging assignment for CGT 115 during spring 2026
#Sophia Alexander
#Last Edited: 02/26/26

#The goal is to take a character image, delete the background and put it on a new background

#This is the averaging code found in the assignment document
import pygame

# Initialize the game
pygame.init()

#This is what names the pop-up window
pygame.display.set_caption("Rey in Prague")

#defines background image
img = pygame.image.load("prague.png")

#defines character image
img2 = pygame.image.load("Rey_green_screen.png")

width = img.get_width()

height = img.get_height()

screen = pygame.display.set_mode((width, height))

#This for loop recolors each pixel in the images. This is the original from the assignment!
'''for y in range(0, height-1):
    for x in range(0, width-1):
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
'''
#supposedly that is all comments now??

#The last slide in the presentation formats the loop like this:
for y in range(0, height-0):
    for x in range(0, width-207):
        pixelColor = img.get_at((x, y))
        pixelColor2 = img2.get_at((x, y))
        red = (pixelColor.r+pixelColor2.r) / 2
        green = (pixelColor.g+pixelColor2.g) / 2
        blue = (pixelColor.b+pixelColor2.b) / 2
        newColor = pygame.Color(int(red), int(green), int(blue))
        img.set_at((x, y), newColor)

for y in range(0, height-0):
    for x in range(width-500, width-700):
        pixelColor = img.get_at((x, y))
        pixelColor2 = img2.get_at((x, y))
        red = (pixelColor.r+pixelColor2.r) / 2
        green = (pixelColor.g+pixelColor2.g) / 2
        blue = (pixelColor.b+pixelColor2.b) / 2
        newColor = pygame.Color(int(red), int(green), int(blue))
        img.set_at((x, y), newColor)

screen.blit(img, (0, 0) )

pygame.display.flip()

pygame.image.save(img, "BW.png")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True