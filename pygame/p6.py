import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)


def main():
    pygame.init()
    pygame.display.set_caption("初めてのPygame")
    sc = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    try:

        pygame.mixer.music.load("pygame_bgm.ogg")
        se = pygame.mixer.Sound("pygame_se.ogg")
    except:
        print("ogg not found ")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_p] == 1:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play(-1)

        if key[pygame.K_s] == 1:
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.stop()

        if key[pygame.K_SPACE] == 1:
            se.play()

        pos = pygame.mixer.music.get_pos()
        txt1 = font.render("BGM pos"+str(pos), True, WHITE)
        txt2 = font.render("play bgm:[S]top bgm: [SPACE] se", True, CYAN)
        sc.fill(BLACK)
        sc.blit(txt1, [100, 100])
        sc.blit(txt2, [100, 200])
        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
