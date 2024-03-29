import ssl
import pygame
import sys
from pygame.locals import *

img_galaxy = pygame.image.load("image_gl/galaxy.png")

img_sship =[
    pygame.image.load("image_gl/starship.png"),
    pygame.image.load("image_gl/starship_l.png"),
    pygame.image.load("image_gl/starship_r.png"),
    pygame.image.load("image_gl/starship_burner.png"),
]
tmr=0
bg_y = 0

ss_x = 480
ss_y = 360
ss_d=0

def move_starship(scrn, key):
    global ss_x, ss_y,ss_d
    ss_d=0
    if key[K_UP] == 1:
        ss_y = ss_y-20
        if ss_y < 80:
            ss_y = 80
    if key[K_DOWN] == 1:
        ss_y = ss_y+20
        if ss_y > 640:
            ss_y = 640
    if key[K_LEFT] == 1:
        ss_d=1
        ss_x = ss_x-20
        if ss_x < 40:
            ss_x = 40
    if key[K_RIGHT] == 1:
        ss_d=2
        ss_x = ss_x+20
        if ss_x > 920:
            ss_x = 920
    scrn.blit(img_sship[3], [ss_x-8, ss_y+40+(tmr%3)*2])
    scrn.blit(img_sship[ss_d], [ss_x-37, ss_y-48])


def main():
    global bg_y,tmr
    pygame.init()
    pygame.display.set_caption("p")
    sc = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()

    while True:
        tmr=tmr+1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    sc = pygame.display.set_mode((960, 720), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    sc = pygame.display.set_mode((960,720))
        bg_y = (bg_y+16) % 720
        sc.blit(img_galaxy, [0, bg_y-720])
        sc.blit(img_galaxy, [0, bg_y])

        key = pygame.key.get_pressed()
        move_starship(sc, key)

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
