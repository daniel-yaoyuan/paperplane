import pygame, random
from pygame.locals import *



class Smallenemy(pygame.sprite.Sprite):
    def __init__(self,scorer):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../img/enemy1.png').convert_alpha()
        self.image1 = self.image
        self.scorer = scorer
        self.destroy_image = []
        self.destroy_image.extend([pygame.image.load('../img/enemy1_down1.png').convert_alpha(),
                                   pygame.image.load('../img/enemy1_down2.png').convert_alpha(),
                                   pygame.image.load('../img/enemy1_down3.png').convert_alpha(),
                                   pygame.image.load('../img/enemy1_down4.png').convert_alpha()])
        self.active =True
        self.timer = 0
        self.HP = 1
        self.destroy_index = 0
        self.rect = self.image.get_rect()
        self.width, self.height = 480,720
        self.speed = 2
        self.rect.left,self.rect.bottom = random.randint(0,self.width - self.rect.width), random.randint(-1 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)
        
    def move(self):
        self.timer += 1
        
        if not self.active:
            if self.timer % 25 == 0:
                if self.destroy_index>3:
                    self.scorer.score += 1000
                    self.reset()
                else:
                    self.image = self.destroy_image[self.destroy_index]
                    self.destroy_index += 1
        else:
            if self.rect.top <self.height:
                self.rect.top += self.speed
            else:
                self.reset()
        if self.HP<=0:
            self.active = False
            

    def reset(self):
        self.rect.left,self.rect.bottom = random.randint(0,self.width - self.rect.width), random.randint(-1 * self.height, 0)
        self.image = self.image1
        self.active = True
        self.destroy_index = 0
        self.HP = 1

    def draw(self,screen):
        screen.blit(self.image,[self.rect.left, self.rect.top])

class Midenemy(pygame.sprite.Sprite):
    def __init__(self,scorer):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../img/enemy2.png').convert_alpha()
        self.image1 = self.image
        self.scorer = scorer
        self.destroy_image = []
        self.destroy_image.extend([pygame.image.load('../img/enemy2_down1.png').convert_alpha(),
                                   pygame.image.load('../img/enemy2_down2.png').convert_alpha(),
                                   pygame.image.load('../img/enemy2_down3.png').convert_alpha(),
                                   pygame.image.load('../img/enemy2_down4.png').convert_alpha()])
        self.active =True
        self.timer = 0
        self.HP = 8
        self.destroy_index = 0
        self.rect = self.image.get_rect()
        self.width, self.height = 480,720
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()

    def move(self):
        self.timer += 1
        if not self.active:
            if self.timer % 25 == 0:
                if self.destroy_index>3:
                    self.scorer.score += 6000
                    self.reset()
                else:
                    self.image = self.destroy_image[self.destroy_index]
                    self.destroy_index += 1
        else:
            if self.rect.top <self.height:
                self.rect.top += self.speed
            else:
                self.reset()
        if self.HP<=0:
            self.active = False
            
    def reset(self):
            self.rect.left,self.rect.top = random.randint(0,self.width - self.rect.width), random.randint(-5 * self.height, 0)
            self.image = self.image1
            self.active = True
            self.destroy_index = 0
            self.HP = 5
    def draw(self,screen):
            screen.blit(self.image,[self.rect.left, self.rect.top])
            
            
class Bigenemy(pygame.sprite.Sprite):
    def __init__(self,scorer):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('../img/enemy3_n1.png').convert_alpha()
        self.image2 = self.image1
        self.scorer = scorer
        self.destroy_image = []
        self.destroy_image.extend([pygame.image.load('../img/enemy3_down1.png').convert_alpha(),
                                   pygame.image.load('../img/enemy3_down2.png').convert_alpha(),
                                   pygame.image.load('../img/enemy3_down3.png').convert_alpha(),
                                   pygame.image.load('../img/enemy3_down4.png').convert_alpha(),
                                   pygame.image.load('../img/enemy3_down5.png').convert_alpha(),
                                   pygame.image.load('../img/enemy3_down6.png').convert_alpha()])
        
        self.timer = 0
        self.active =True
        self.image = random.choice([self.image1,self.image2])
        self.timer = 0
        self.destroy_index = 0
        self.HP = 15
        self.rect = self.image.get_rect()
        self.width, self.height = 480,720
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()

    def move(self):
        self.timer += 1
        if not self.active:
            if self.timer % 30 == 0:
                if self.destroy_index>5:
                    self.scorer.score += 15000
                    self.reset()
                else:
                    self.image = self.destroy_image[self.destroy_index]
                    self.destroy_index += 1
        else:
            if self.rect.top <self.height:
                if self.timer % 2:
                    self.rect.top += self.speed
            else:
                self.reset()
        if self.HP<=0:
            self.active = False
            
           
    def reset(self):
            self.rect.left,self.rect.top = random.randint(0,self.width - self.rect.width), random.randint(-2* self.height, 0)
            self.image = self.image2
            self.active = True
            self.destroy_index = 0
            self.HP = 15
    def draw(self,screen):
            screen.blit(self.image,[self.rect.left, self.rect.top])
class Enemy_bullet(pygame.sprite.Sprite):
    def __init__(self,screen,plane):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.active = True
        self.plane = plane
        self.image = pygame.image.load('../img/bullet2.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.y = random.choice([-1,1])
        self.rect = self.image.get_rect()
        self.rect.left = self.plane.rect.left + 80
        self.rect.top = self.plane.rect.top + 130

    def move(self):        
        self.rect.top += 3
        self.rect.left += self.y
        if self.rect.top >= 720:
            self.active = False

    def draw(self):
        if self.active:
            self.screen.blit(self.image,(self.rect.left, self.rect.top))
        
        
        
        
