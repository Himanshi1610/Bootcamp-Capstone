import pygame
import random

pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Bouncing Ball")

y=200
vel_y=random.randint(1,10)
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    y+=vel_y
    if y<30 or y>=370:
        vel_y=-vel_y      
    
    window.fill([255, 255, 255])
    pygame.draw.circle(window,color,(200,y),25)
    clock.tick(60)
    pygame.display.update()

quit()