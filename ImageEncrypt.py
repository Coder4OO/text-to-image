#IMAGE ENCRYPTION
import pygame
from math import floor,ceil
from os import listdir,getcwd
import os
pygame.init()

running = True

def num_to_colour(n):
    colour = []
    for i in range(3):
        if n > 255:
            colour.append(255)
            n -= 255
        else:
            colour.append(n)
            n = 0
            gap = 3-len(colour)
            for i in range(gap):
                colour.append(0)
            break
    return colour


def create_image(msg):
    colours = list(map(num_to_colour, list(map(lambda x:ord(x), msg))))
    dim = len(msg)/2
    surf = pygame.Surface((int(floor(dim)),int(ceil(dim))))
    pix = pygame.PixelArray(surf)
    colours = tuple(map(tuple, colours))
    count = 0
    print(len(colours))
    for y in range(int(ceil(dim))):
        for x in range(int(floor(dim))):
            try:
                pix[x,y] = surf.map_rgb(colours[count])
            except IndexError:
                break
            count += 1
    rsurf = pix.surface
    pix.close()
    return rsurf

while running:
    menu = input("\t\tMenu:\n\n1.Create new image\n2. Exit program")
    if menu == "1":
        txt = input("Enter message:")
        img = create_image(txt)
        pygame.image.save(img, "image"+str(len(listdir(getcwd())))+".png")
        print("Image saved as %s" % "image"+str(len(listdir(getcwd())))+".png")
    elif menu == "2":
        running = False
    else:
        print("Please enter 1 or 2")
pygame.quit()
