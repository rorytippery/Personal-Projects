import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
test_font = pygame.font.Font(r'C:\Users\rtipp\PycharmProjects\pythonProject\FlappyBird\UltimatePygameIntro-main\font\Pixeltype.ttf', 50)

sky_surface1 = pygame.image.load(r'C:\Users\rtipp\PycharmProjects\pythonProject\FlappyBird\UltimatePygameIntro-main\graphics/Sky.png').convert()
sky_surface2 = sky_surface1
sky_rect1 = sky_surface1.get_rect(topleft = (0,0))
sky_rect2 = sky_surface2.get_rect(topleft = (800,0))

ground_surface1 = pygame.image.load(r'C:\Users\rtipp\PycharmProjects\pythonProject\FlappyBird\UltimatePygameIntro-main\graphics/ground.png').convert()
ground_surface2 = ground_surface1
ground_rect1 = ground_surface1.get_rect(topleft = (0,300))
ground_rect2 = ground_surface2.get_rect(topleft = (800,300))

flappy_surface = pygame.image.load(r'C:\Users\rtipp\PycharmProjects\pythonProject\FlappyBird\flappybird.png').convert_alpha()
flappy_surface = pygame.transform.scale(flappy_surface, (40,30))
flappy_rect = flappy_surface.get_rect(midbottom = (200,150))

pipehigh_surface = pygame.image.load(r'C:\Users\rtipp\PycharmProjects\pythonProject\FlappyBird\pipehigh.png')
pipehigh_surface = pygame.transform.scale(pipehigh_surface, (60,350))
pipehigh_rect1 = pipehigh_surface.get_rect(topleft = (500,-240))
pipehigh_rect2 = pipehigh_surface.get_rect(topleft = (750,-280))
pipehigh_rect3 = pipehigh_surface.get_rect(topleft = (1000,-230))
pipehigh_rect4 = pipehigh_surface.get_rect(topleft = (1250,-220))

pipelow_surface = pygame.image.load(r'C:\Users\rtipp\PycharmProjects\pythonProject\FlappyBird\pipelow.png')
pipelow_surface = pygame.transform.scale(pipelow_surface, (60,350))
pipelow_rect1 = pipelow_surface.get_rect(bottomleft = (500,570))
pipelow_rect2 = pipelow_surface.get_rect(bottomleft = (750,530))
pipelow_rect3 = pipelow_surface.get_rect(bottomleft = (1000,580))
pipelow_rect4 = pipelow_surface.get_rect(bottomleft = (1250,590))

score = 0
alive = True
gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -2


    score_surface = test_font.render(str(score), False, 'Black')
    score_rect = score_surface.get_rect(center=(400, 50))

    screen.blit(sky_surface1,(sky_rect1))
    screen.blit(sky_surface2,(sky_rect2))
    screen.blit(ground_surface1,(ground_rect1))
    screen.blit(ground_surface2,(ground_rect2))

    screen.blit(flappy_surface,(flappy_rect))

    screen.blit(pipehigh_surface,(pipehigh_rect1))
    screen.blit(pipehigh_surface,(pipehigh_rect2))
    screen.blit(pipehigh_surface,(pipehigh_rect3))
    screen.blit(pipehigh_surface,(pipehigh_rect4))

    screen.blit(pipelow_surface, (pipelow_rect1))
    screen.blit(pipelow_surface, (pipelow_rect2))
    screen.blit(pipelow_surface, (pipelow_rect3))
    screen.blit(pipelow_surface, (pipelow_rect4))

    screen.blit(score_surface, (score_rect))

    if flappy_rect.colliderect(pipelow_rect1): alive = False
    if flappy_rect.colliderect(pipelow_rect2): alive = False
    if flappy_rect.colliderect(pipelow_rect3): alive = False
    if flappy_rect.colliderect(pipelow_rect4): alive = False

    if flappy_rect.colliderect(pipehigh_rect1): alive = False
    if flappy_rect.colliderect(pipehigh_rect2): alive = False
    if flappy_rect.colliderect(pipehigh_rect3): alive = False
    if flappy_rect.colliderect(pipehigh_rect4): alive = False

    if alive == True:
        gravity += .1
        flappy_rect.bottom += gravity

        if ground_rect1.right < 0: ground_rect1.left = 800
        if ground_rect2.right < 0: ground_rect2.left = 800
        if sky_rect1.right < 0: sky_rect1.left = 800
        if sky_rect2.right < 0: sky_rect2.left = 800

        if pipehigh_rect1.right < 0:
            pipehigh_rect1.top = -240
            pipelow_rect1.bottom = 570
            pipehigh_rect1.left = 950
            pipelow_rect1.left = 950
            rand = random.randint(-75,75)
            pipehigh_rect1.top += rand
            pipelow_rect1.bottom += rand
            score += 1

        if pipehigh_rect2.right < 0:
            pipehigh_rect2.top = -240
            pipelow_rect2.bottom = 570
            pipehigh_rect2.left = 950
            pipelow_rect2.left = 950
            rand = random.randint(-75, 75)
            pipehigh_rect2.top += rand
            pipelow_rect2.bottom += rand
            score += 1

        if pipehigh_rect3.right < 0:
            pipehigh_rect3.top = -240
            pipelow_rect3.bottom = 570
            pipehigh_rect3.left = 950
            pipelow_rect3.left = 950
            rand = random.randint(-75, 75)
            pipehigh_rect3.top += rand
            pipelow_rect3.bottom += rand
            score += 1

        if pipehigh_rect4.right < 0:
            pipehigh_rect4.top = -240
            pipelow_rect4.bottom = 570
            pipehigh_rect4.left = 950
            pipelow_rect4.left = 950
            rand = random.randint(-60, 60)
            pipehigh_rect4.top += rand
            pipelow_rect4.bottom += rand
            score += 1

        ground_rect1.left -= 2
        ground_rect2.left -= 2
        sky_rect1.left -= 2
        sky_rect2.left -= 2

        pipehigh_rect1.left -= 2
        pipehigh_rect2.left -= 2
        pipehigh_rect3.left -= 2
        pipehigh_rect4.left -= 2

        pipelow_rect1.left -= 2
        pipelow_rect2.left -= 2
        pipelow_rect3.left -= 2
        pipelow_rect4.left -= 2
    else:
        flappy_rect.top += 3
        if flappy_rect.colliderect(ground_rect1): flappy_rect.bottom = 300
        if flappy_rect.colliderect(ground_rect2): flappy_rect.bottom = 300


    pygame.display.update()
    clock.tick(60)