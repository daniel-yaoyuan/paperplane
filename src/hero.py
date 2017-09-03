import pygame
from pygame.locals import *


class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image1 = pygame.image.load('../img/hero1.png').convert_alpha()
        self.image2 = pygame.image.load('../img/hero2.png').convert_alpha()
        self.active = True
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.left = (bg_size[0] - 102) / 2
        self.rect.top = 550
        self.speed = 4
        self.HP = 5
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load('../img/hero_blowup_n1.png').convert_alpha(),
                                    pygame.image.load('../img/hero_blowup_n2.png').convert_alpha(),
                                    pygame.image.load('../img/hero_blowup_n3.png').convert_alpha(),
                                    pygame.image.load('../img/hero_blowup_n4.png').convert_alpha()])
        self.destroy_index = 0
        self.timer = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.bomb = 5
        self.double_fire = False
        self.f = 20
        

    def move(self):
        self.timer += 1
        if self.active:
            key_pressed = pygame.key.get_pressed()
            if  key_pressed[K_w] or key_pressed[K_UP]:
                self.rect.top = self.rect.top - self.speed
            if  key_pressed[K_s] or key_pressed[K_DOWN]:
                self.rect.top = self.rect.top + self.speed
            if  key_pressed[K_a] or key_pressed[K_LEFT]:
                self.rect.left = self.rect.left - self.speed
            if  key_pressed[K_d] or key_pressed[K_RIGHT]:
                self.rect.left = self.rect.left + self.speed
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top > 574:
                self.rect.top = 574
            if self.rect.left > 378:
                self.rect.left = 378
            if self.rect.top < 0:
                self.rect.top = 0
            if self.image == self.image1:
                self.image = self.image2
            else:
                self.image = self.image1
        else:
            if self.destroy_index < 4:
                self.image = self.destroy_images[self.destroy_index]
                if self.timer % 25 == 0:
                    self.destroy_index += 1
            
                

    def draw(self):
        self.screen.blit(self.image,[self.rect.left,self.rect.top])

    def hit(self):
        self.active = False

    def reset(self):
        self.active = True
        self.image = self.image1
        self.destroy_index = 0
        self.bomb = 5
        
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self,plane, pos = 1):
        pygame.sprite.Sprite.__init__(self) # pos: 0 - left, 1 - middle, 2 - right
        self.plane = plane
        self.active = True
        self.pos = pos
        self.img1 = pygame.image.load('../img/bullet1.png').convert_alpha()
        self.img2 = pygame.image.load('../img/bullet2.png').convert_alpha()
        self.img = self.img1
        #self.sound = pygame.mixer.music.load('bullet.mp3')
        self.rect = self.img.get_rect()
        if pos == 1:
            self.rect.left = plane.rect.left + 50
            self.rect.top = plane.rect.top + 50
        elif pos == 0:
            self.img = self.img2
            self.rect.left = plane.rect.left + 25
            self.rect.top = plane.rect.top + 50
        elif pos == 2:
            self.rect.left = plane.rect.left + 75
            self.rect.top = plane.rect.top + 50
            self.img = self.img2
            

    def move(self):
        self.rect.top -= 10
        if self.rect.top<0:
            self.active = False
            
        
    def draw(self,screen):
        screen.blit(self.img, [self.rect.left, self.rect.top])
        self.mask = pygame.mask.from_surface(self.img)
    
        
        
        

    
            
        
        
        


        
        
        
        
