import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()                                           #初期化
    screen=pygame.display.set_mode((800,600))                 #画面サイズ設定
    pygame.display.set_caption("sample")                   #タイトル表示(上のとこ)
    font=pygame.font.Font(None,50)

    while(1):
        screen.fill((0,0,255))                                #画面を黒塗り(r,g,b)
        text=font.render("TEST",False,(0,0,0))
        text2=font.render("TEST",True,(255,255,255))    #Font.render(text, antialias, color, background=None): return Surface

        screen.blit(text,[20,80])#表示
        screen.blit(text2,[20,120])
        pygame.display.update()                             #画面を更新引数なしで画面全部更新
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

if __name__=="__main__":
    main()