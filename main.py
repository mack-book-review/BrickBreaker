import pygame,sys

import player
from player import Player
from ball import Ball
from brick import Brick
from constants import *

brick = Player()
ball = Ball()

def handleInput(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("move left")
                brick.moveLeft()
            elif event.key == pygame.K_RIGHT:
                print("move right")
                brick.moveRight()



def main():
    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Brick Breaker")

    clock = pygame.time.Clock()

    #create bricks
    target_bricks = []
    target_rects = []
    num_rows = 2
    num_cols = 8
    x_margin_space = 50
    brick_width = (SCREEN_WIDTH-x_margin_space-10)/num_cols
    x_offset = x_margin_space/num_cols

    y_margin_space = 50
    brick_height = (SCREEN_WIDTH/4 - y_margin_space -10) / num_rows
    y_offset = y_margin_space/num_cols

    x_pos = 0
    y_pos = 0

    for row in range(num_rows):
        for col in range(num_cols):
            x_pos = 10 + (x_offset + brick_width)*col
            y_pos = 10+ (y_offset + brick_height)*row
            b = Brick(x_pos,y_pos,brick_width,brick_height,FOREST_GREEN)
            target_bricks.append(b)
            target_rects.append(b.rect)

    gameLost = False
    gameWon = False
    killCount = 0

    while not gameLost and not gameWon:
        screen.fill((255,255,255))

        handleInput(pygame.event.get())

        brick.draw(screen)
        brick.update()

        index_collide = ball.rect.collidelist(target_rects)
        if index_collide and not target_bricks[index_collide].isDead:
            if ball.rect.top <= b.rect.bottom:
                ball.moveDown()
                target_bricks[index_collide].kill()
                killCount += 1

        for b in target_bricks:
            if not b.isDead:
                b.draw(screen)

        #Second Approach
        # for b in target_bricks:
        #     if b.rect.colliderect(ball.rect) and not b.isDead:
        #         if ball.rect.top <= b.rect.bottom:
        #             ball.moveDown()
        #             b.kill()
        #             killCount += 1
        #
        #     b.draw(screen)

        ball.draw(screen)
        ball.update()

        if ball.rect.bottom >= SCREEN_HEIGHT:
            gameLost = True

        if ball.rect.colliderect(brick.rect):
            if ball.rect.bottom >= brick.rect.top:
                ball.moveUp()


        print("Kill Count: " + str(killCount))
        print("Total Bricks:" + str(num_rows*num_cols))
        print("Lenght of target bricks: " + str(len(target_bricks)))
        if killCount >= num_cols*num_rows:
            gameWon = True

        pygame.display.flip()
        clock.tick(60)

    if gameWon:
        print("You won!")

    if gameLost:
        print("You lost!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
