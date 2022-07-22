from email import message
import random
from tkinter.messagebox import NO
import pygame
from pygame.locals import *
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

imgBtlBG = pygame.image.load("btlbg.png")
imgEnemy = pygame.image.load("./rpgsozai/image/enemy4.png")
imgEffect = pygame.image.load("effect_a.png")

emy_num = 0
emy_x = 440-imgEnemy.get_width()/2
emy_y = 560-imgEnemy.get_height()
emy_step = 0
emy_blink = 0
dmg_eff = 0
COMMAND = ["[A]ttack", "[P]otion", "[B]laze gem", "[R]un"]


message = [""]*10


def init_message():
    for i in range(10):
        message[i] = ""


def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i+1]
    message[9] = msg


def draw_text(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x+1, y+2])

    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])


def init_battle():
    global imgEnemy, emy_num, emy_x, emy_y
    emy_num = emy_num+1
    if emy_num == 5:
        emy_num = 1

    imgEnemy = pygame.image.load("./rpgsozai/image/enemy"+str(emy_num)+".png")

    emy_x = 440-imgEnemy.get_width()/2
    emy_y = 560-imgEnemy.get_height()


def draw_battle(bg, fnt):
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff-1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)

    bg.blit(imgBtlBG, [bx, by])

    if emy_blink % 2 == 0:

        bg.blit(imgEnemy, [emy_x, emy_y+emy_step])
    if emy_blink > 0:
        emy_blink = emy_blink-1
    for i in range(10):
        draw_text(bg, message[i], 600, 100+i*50, fnt, WHITE)


def battle_command(bg, fnt):
    for i in range(4):
        draw_text(bg, COMMAND[i], 20, 360+60*i, fnt, WHITE)


def main():
    global emy_step, emy_blink, dmg_eff
    idx = 10
    tmr = 0
    pygame.init()
    pygame.display.set_caption("sentou")
    sc = pygame.display.set_mode((800, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    init_message()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_battle(sc, font)
        tmr = tmr + 1
        key = pygame.key.get_pressed()

        if idx == 10:
            if tmr == 1:
                set_message("encount")
            if tmr == 6:
                idx = 11
                tmr = 0
        elif idx == 11:
            if tmr == 1:
                set_message("your turn")
            battle_command(sc, font)
            if key[K_a] == 1 or key[K_SPACE] == 1:
                idx = 12
                tmr = 0

        elif idx == 12:
            if tmr == 1:
                set_message("you attack")
            if 2 <= tmr and tmr <= 4:
                sc.blit(imgEffect, [700-tmr*120, -100+tmr*120])
            if tmr == 5:
                emy_blink = 5
                set_message("************damege")
            if tmr == 16:
                idx = 13
                tmr = 0
        elif idx == 13:
            if tmr == 1:
                set_message("enemy turn")
            if tmr == 5:
                set_message("enemy aataack")
                emy_step = 30
            if tmr == 9:
                set_message("******:damge")
                dmg_eff = 5
                emy_step = 0
            if tmr == 20:
                idx = 11
                tmr = 0
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
