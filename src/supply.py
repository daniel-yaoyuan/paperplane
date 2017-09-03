import pygame
import random


class Scorer:
    def __init__(self):
        self.score = 0
        
class Bomb_supply(pygame.sprite.Sprite):
    def __init__(self,screen,plane):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.plane = plane
        self.image = pygame.image.load('../img/ufo2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = -1500
        self.rect.left = random.randint(1,420)
        self.screen.blit(self.image, (self.rect.left, self.rect.top))
        
        self.mask = pygame.mask.from_surface(self.image)
        self.active = True
        
    def move(self):
        self.rect.top += 1
        if self.rect.top > 720:
            self.active = False
        hit_bomb = pygame.sprite.spritecollide(self, [self.plane], False, pygame.sprite.collide_mask)
        if hit_bomb:
            self.active = False
            self.plane.bomb += 1
            
        

    def draw(self):
        self.screen.blit(self.image, (self.rect.left, self.rect.top))
        if not self.active:
            self.reset()
        
    def reset(self):
        self.rect.top = random.randint(-1500,-1000)
        self.rect.left = random.randint(1,420)
        self.active = True
        
class Bullet_supply(pygame.sprite.Sprite):
    def __init__(self,screen,plane):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.plane = plane
        self.image = pygame.image.load('../img/ufo1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = -2000
        self.rect.left = random.randint(1,420)
        self.screen.blit(self.image, (self.rect.left, self.rect.top))
        
        self.mask = pygame.mask.from_surface(self.image)
        self.active = True
        self.d_t = 1200
        
    def move(self):
        self.rect.top += 1
        if self.rect.top > 720:
            self.active = False
            
        

    def draw(self):
        self.screen.blit(self.image, (self.rect.left, self.rect.top))
        if not self.active:
            self.reset()
        
    def reset(self):
        self.rect.top = random.randint(-2500,-1000)
        self.rect.left = random.randint(1,420)
        self.active = True
