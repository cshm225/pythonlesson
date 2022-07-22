from email import message
from tkinter.messagebox import NO
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

imgBtlBG = pygame.image.load("btlbg.png")
imgEnemy = pygame.image.load("./rpgsozai/image/enemy1.png")

emy_num = 0
emy_x = 440-imgEnemy.get_width()/2
emy_y = 560-imgEnemy.get_height()

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
    bg.blit(imgBtlBG, [0, 0])
    bg.blit(imgEnemy, [emy_x, emy_y])
    for i in range(10):
        draw_text(bg,message[i],600,100+i*50,fnt,WHITE)


def main():
    pygame.init()
    pygame.display.set_caption("sentou")
    sc = pygame.display.set_mode((800, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    init_message()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                set_message("KEYDOWN"+str(event.key))
        draw_battle(sc, font)
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
