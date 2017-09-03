import pygame, sys, random, hero, time, enemy, supply
from pygame.locals import *

BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
bg = [255,255,255]
size = width, height = 480,720
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game')
screen.fill(bg)
g_o = pygame.image.load('../img/game_over.png').convert_alpha()
g_a = pygame.image.load('../img/game_again.png').convert_alpha()


pygame.mixer.music.load('../sound/game_music.ogg')
pygame.mixer.music.set_volume(0.5)
game_over = pygame.mixer.Sound('../sound/game_over.ogg')
game_over.set_volume(0.3)
get_doublelaser = pygame.mixer.Sound('../sound/get_double_laser.ogg')
flying = pygame.mixer.Sound('../sound/big_spaceship_flying.ogg')
flying.set_volume(0.7)
use_bomb = pygame.mixer.Sound('../sound/use_bomb.ogg')
get_bomb = pygame.mixer.Sound('../sound/get_bomb.ogg')
enemy1_down = pygame.mixer.Sound('../sound/enemy1_down.ogg')
enemy2_down = pygame.mixer.Sound('../sound/enemy2_down.ogg')
enemy3_down = pygame.mixer.Sound('../sound/enemy3_down.ogg')
background = pygame.image.load('../img/background.png').convert()
screen.blit(background,[0,0])
scorer = supply.Scorer()


def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1 = enemy.Smallenemy(scorer)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2 = enemy.Midenemy(scorer)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3 = enemy.Bigenemy(scorer)
        group1.add(e3)
        group2.add(e3)
        
enemies = pygame.sprite.Group()
small_enemies = pygame.sprite.Group()

mid_enemies = pygame.sprite.Group()

big_enemies = pygame.sprite.Group()

def init():
    level = 1
    enemies.empty()
    small_enemies.empty()
    mid_enemies.empty()
    big_enemies.empty()
    add_small_enemies(small_enemies, enemies,6)
    add_mid_enemies(mid_enemies, enemies,3)
    add_big_enemies(big_enemies, enemies,1)
    
def over(plane):
    screen.blit(g_o, (90,300))
    screen.blit(g_a, (90,350))
    
            
            
            
    
def main():
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    running = True
    me = hero.MyPlane([480,720], screen)
    bullet_list = []
    time = 0
    init()
    
   
    score_font = pygame.font.Font('../font/waltographUI.ttf', 36)
    small_added = False
    mid_added = False
    big_added = False
    bomb = supply.Bomb_supply(screen, me)
    bullet_supply = supply.Bullet_supply(screen, me)
    b_i = pygame.image.load('../img/bomb.png').convert_alpha()
    is_bombing = False
    bomb_time = 50
    level = 1
    bullet_t = 0
    e_b = []
    playing = False
   
    
    def check():
        for each in big_enemies:
            if each.rect.bottom > 0:
                return True
        return False   
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not me.active:
                if event.type == MOUSEBUTTONDOWN:
                    a = g_o.get_rect()
                    a.left, a.top = 90,300
                    if a.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    b = g_o.get_rect()
                    b.left, b.top = 90,350
                    if b.collidepoint(event.pos):
                        init()
                        for x in e_b:
                            x.active = False
                        me.active = True
                        me.destroy_index = 0
                        scorer.score = 0
                        bomb.reset()
                        bullet_supply.reset()
                        me.rect.left = 189
                        me.rect.top = 550
                        me.bomb = 5
                        me.double_fire = False
                        level = 1
                        e_b = []
                        
                        

                    
        if me.active:
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down:
                me.hit()
                game_over.play()
                end_score = scorer.score
                for e in enemies_down:
                    e.active = False
                scorer.score = end_score
            
        screen.blit(background, [0, 0])
        me.move()
        me.draw()
        if time % 20 == 0 and me.active:
            if me.double_fire:
                bullet_list.append(hero.Bullet(me,0))
                bullet_list.append(hero.Bullet(me,2))
            else:
                bullet_list.append(hero.Bullet(me))

        hit_bullet = pygame.sprite.spritecollide(bullet_supply, [me], False, pygame.sprite.collide_mask)
        if hit_bullet:
            get_doublelaser.play()
            bullet_supply.active = False
            me.double_fire = True
            bullet_t = time

        if time-bullet_t >= 1000:
            me.double_fire = False
            
        bullet_list = list(filter(lambda x: x.active, bullet_list))
        for bullet in bullet_list:
            bullet.move()
            bullet.draw(screen)
            enemy_hit = pygame.sprite.spritecollide(bullet, enemies, False, pygame.sprite.collide_mask)
            if enemy_hit:
                bullet.active = False
                for x in enemy_hit:
                    x.HP = x.HP-1
        for each in enemies:
            each.move()
            each.draw(screen)
            
        if level == 1 and scorer.score >50000:
            level = 2
            add_small_enemies(small_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
        elif level == 2 and scorer.score >300000:
            level = 3
            add_small_enemies(small_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
        elif level == 3 and scorer.score >600000:
            level = 4
            add_small_enemies(small_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
        elif level == 4 and scorer.score >1000000:
            level = 5
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
            
        if me.active and is_bombing == False:
            key_pressed = pygame.key.get_pressed()
            if key_pressed:
                if key_pressed[K_SPACE] and me.bomb>0:
                    for x in enemies:
                        if x.rect.bottom >= 0:
                            x.active = False
                    for x in e_b:
                        x.active = False
                    me.bomb -= 1
                    use_bomb.play()
                    is_bombing = True
                    bomb_time = time
        if time-bomb_time >= 40:
            is_bombing = False
        if check():
            if not playing:
                flying.play(-1)
                playing = True
        else:
            if playing:
                flying.stop()
                playing = False
        if time % 100 == 0:
            for x in big_enemies:
                if x.active == True:
                    e_b.append(enemy.Enemy_bullet(screen,x))
        
        
        for b in e_b:
           b.move()
           b.draw()
        for x in e_b:
            me_hit = pygame.sprite.spritecollide(x, [me], False, pygame.sprite.collide_mask)
            if me_hit and me.active:
                me.hit()
                x.active = False
                game_over.play()
        
        bomb.move()
        bomb.draw()
        bullet_supply.move()
        bullet_supply.draw()
        if me.active == False:
            over(me)
        screen.blit(b_i, (10, 650))
        score_text = score_font.render('Score: %s' % str(scorer.score),True,BLACK)
        screen.blit(score_text,(10,5))
        bomb_text = score_font.render('x %s' % me.bomb,True, BLACK)
        screen.blit(bomb_text, (100, 660))
        clock.tick(75)
        pygame.display.flip()
        time = time + 1
        
if __name__ == '__main__':
    main()
    
        


