import pygame
import sys
img_galaxy = pygame.image.load("image_gl/galaxy.png")
img_sship = pygame.image.load("image_gl/starship.png")


def main():
    pygame.init()
    pygame.display.set_caption("pygame")
    sc = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    ang = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    sc = pygame.display.set_mode((960, 720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    sc = pygame.display.set_mode((960, 720))
        sc.blit(img_galaxy, [0, 0])

        ang = (ang+1) % 360
        img_rz = pygame.transform.rotozoom(img_sship, ang, 1.0)
        x = 480-img_rz.get_width()/2
        y = 360-img_rz.get_height()/2
        sc.blit(img_rz, [x, y])
        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
