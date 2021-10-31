import pygame
from constants import *

class Brick():

    def __init__(self,xPos,yPos,width,height, color):
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(xPos,yPos,width,height)

        self.isDead = False


    def kill(self):
        self.isDead = True

    def draw(self,screen):
        if not self.isDead:
            pygame.draw.rect(screen,self.color,(self.rect.x,self.rect.y,self.width,self.height))

    def update(self):
        pass