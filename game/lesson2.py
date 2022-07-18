import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    sc= pygame.display.set_mode((300,200))
    pygame.display.set_caption("game")

    while(1):
        sc.fill((0,0,0))
        # (0,0)から(80,80)まで線幅5pxで緑色(R=0, G=95, B=0)の直線を描く
        pygame.draw.line(sc,(0,95,0),(0,0),(80,80),5)

        # 左上座標(10,10)、幅80px、高さ50pxの長方形を線幅5pxの緑色(R=0, G=80, B=0)で描く
        pygame.draw.rect(sc,(0,80,0),Rect(10,10,80,50),5) # 四角形を描画(塗りつぶしなし)
        #pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50))    # 四角形を描画(塗りつぶし)

        # 左上の座標が(50,50)、幅が150、高さが50の矩形に内接する楕円を線幅5pxの緑色(R=0, G=100, B=0)で描く
        pygame.draw.ellipse(sc,(0,100,0),(50,50,200,100),5)
        #pygame.draw.ellipse(screen,(0,100,0),(50,50,200,100)) # 円を描画(塗りつぶし)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()


if __name__=="__main__":
    main()

