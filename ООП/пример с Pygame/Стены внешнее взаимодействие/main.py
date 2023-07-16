import pygame
#from Sprites.Player import Player
#from Sprites.Enemy import * #from модуль import конкретный класс или фукнция
from Sprites import Player as p, Enemy as e, Wall as w
pygame.init()# точка входа и настройка игры


#просто переменные
FPS = 60 
WIDTH = 800
HEIGHT = 600
COLOR = (255, 0, 0)# цвет в формате rgb этот красный


#создать игрока
player = p.Player(100,100)

#создать врага
enemy = e.Enemy(100,100)
enemy2 = e.Enemy(100,100,500,500)


#создать стену
wall = w.Wall(40,1200)

all_sprites = pygame.sprite.Group() # создаем группу спрайтов
sprites_enemy = pygame.sprite.Group() # создаем группу спрайтов врага
walls = pygame.sprite.Group() # создаем группу спрайтов wall

window = pygame.display.set_mode((WIDTH, HEIGHT))# задаем размеры окну
clock = pygame.time.Clock()# задаем время игры сейчас оно нужно для фпс
run = True # управление игрой

all_sprites.add(player, enemy,enemy2,wall)
sprites_enemy.add(enemy)
walls.add(wall)
#сама игра
while run:
    for i in pygame.event.get():# отслеживаем события, которые просходят в окне нажатие, закрытие и т.дю
        if i.type == pygame.QUIT:# если окно закрыли 
            run = False# выходим из цикла
            
    hit = pygame.sprite.spritecollide(player,sprites_enemy,False)# было столкновение
    hit_wall = pygame.sprite.spritecollide(player,walls,False)# было столкновение

    #if enemy.rect.left <= player.rect.right and (player.rect.bottom>=enemy.rect.top>= player.rect.top) and( player.rect.bottom>=enemy.rect.bottom>= player.rect.top):
    #if hit_wall:    
    if player.rect.left <= wall.rect.right:
        player.left_border = True
    else:
        player.left_border = False
       
    if hit:    
        player.kill()# уничтожили игрока
    window.fill(COLOR)#красим окно здесь же можно потом картинки загружать
    all_sprites.draw(window)
    player.update()#обновляем положение игрока
    enemy.update()#обновляем положение врага
    pygame.display.update()#обновляем экран каждую итерацию
    clock.tick(FPS)#плавно обновляем

pygame.quit()# корректное завершение работы