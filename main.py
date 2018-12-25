import pygame
from random import randint
import time
from spaceship import spaceship
from alien import alien
from missile import missile
pygame.init()
pygame.font.init()
win_width = 800
win_ht = 700
img_width = 100
img_ht = 70
gamedisplay = pygame.display.set_mode((win_width, win_ht))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
myfont = pygame.font.SysFont('Comic Sans MS', 50)
img = pygame.image.load("spaceship2.jpg")
img = pygame.transform.scale(img, (img_width, img_ht))
img2 = pygame.image.load("alien.jpg")
img2 = pygame.transform.scale(img2, (img_width, img_ht))
img3 = pygame.image.load("imageedit_1_2131087627.png")
img3 = pygame.transform.scale(img3, (img_width, img_ht))
img4 = pygame.image.load("imageedit_3_4754263304.png")
img4 = pygame.transform.scale(img4, (img_width, img_ht))
img5 = pygame.image.load("alienkill.jpeg")
img5 = pygame.transform.scale(img5, (img_width, img_ht))


def imag(x, y, img):
    gamedisplay.blit(img, (x, y))
prev_time = 0


def gameloop():
    counter = 0
    prev_counter = 0
    gamedisplay.fill(black)
    al = alien()
    sp = spaceship()
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    crashed = False
    t, x, w = 0, 0, 0
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and sp.x >= 100:
                    sp.moveleft()
                elif event.key == pygame.K_d and sp.x <= 600:
                    sp.moveright()
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_SPACE:
                    missile.shot.append(
                        [sp.x,
                         sp.y - win_ht / 10,
                         int(time.time()),
                            0])
                if event.key == pygame.K_s:
                    missile.shot2.append(
                        [sp.x, sp.y - win_ht / 10, int(time.time()), 0])

        gamedisplay.fill(black)
        global prev_time
        if int(time.time()) - prev_time >= 10:
            al = alien()
            alien.aliens.append([al.x, al.y, int(time.time()), 0])
            prev_time = int(time.time())

        for i in range(0, len(missile.shot2)):
            try:
                if missile.shot2[i][3] == 0:
                    imag(missile.shot2[i][0], missile.shot2[i][1], img4)
                b = int(time.time()) - missile.shot2[i][2]
                if missile.shot2[i][3] == 1:
                    missile.shot2.remove(missile.shot2[i])
                    continue
                if missile.shot2[i][1] >= 0:
                    if b >= 1:
                        missile.shot2[i][2] = int(time.time())
                        missile.shot2[i][1] -= win_ht / 5
                else:
                    missile.shot2.remove(missile.shot2[i])
            except:
                pass
        for i in range(0, len(missile.shot)):
            try:
                if missile.shot[i][3] == 0:
                    imag(missile.shot[i][0], missile.shot[i][1], img3)
                a = int(time.time()) - missile.shot[i][2]
                if missile.shot[i][3] == 1:
                    del missile.shot[i]
                    continue
                if missile.shot[i][1] >= 0:
                    if a >= 1:
                        missile.shot[i][2] = int(time.time())
                        missile.shot[i][1] -= win_ht / 10
                else:
                	    missile.shot.remove(missile.shot[i])
            except:
                pass

        for i in range(0, len(alien.aliens)):
            try:
                if int(time.time()) - alien.aliens[i][2] <= 8 and alien.aliens[i][3] == 0:
                    imag(alien.aliens[i][0], alien.aliens[i][1], img2)
                if int(time.time()) - alien.aliens[i][2] >= 8 and alien.aliens[i][3] == 0:
                    del alien.aliens[i]
                    continue
                if alien.aliens[i][3] == 1:
                    if int(time.time()) - alien.aliens[i][2] <= 5:
                        imag(alien.aliens[i][0], alien.aliens[i][1], img5)
                    else:
                        alien.aliens.remove(alien.aliens[i])
            except:
                pass
        for i in range(0, len(alien.aliens)):
            try:
                for j in range(0, len(missile.shot)):
                    try:
                        if missile.shot[j][0] == alien.aliens[i][0] and missile.shot[j][1] <= alien.aliens[i][1]:
                            prev_counter = counter
                            counter += 2
                            missile.shot[j][3] = 1
                            del alien.aliens[i]
                            del missile.shot[j]
                    except:
                        pass
                for j in range(0, len(missile.shot2)):
                    try:
                        if missile.shot2[j][0] == alien.aliens[i][0] and missile.shot2[j][1] <= alien.aliens[i][1]:
                            prev_counter = counter
                            counter += 1
                            alien.aliens[i][3] = 1
                            missile.shot2[j][3] = 1
                            alien.aliens[i][2] = int(time.time())
                    except:
                        pass
            except:
                pass
        imag(sp.x, sp.y, img)
        scoretext = myfont.render("Score = " + str(counter), False, white)
        gamedisplay.blit(scoretext, (300, 0))
        prev_counter = counter
        pygame.display.update()
        clock.tick(100)
gameloop()
