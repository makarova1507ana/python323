import pygame
from Player import Player
from Enemy import * #from модуль import конкретный класс или фукнция

pygame.init()# точка входа и настройка игры


#просто переменные
FPS = 60 
WIDTH = 800
HEIGHT = 600
COLOR = (255, 0, 0)# цвет в формате rgb этот красный


#создать игрока
player = Player(100,100)

#создать врага
enemy = Enemy(100,100)

all_sprites = pygame.sprite.Group() # создаем группу спрайтов
sprites_enemy = pygame.sprite.Group() # создаем группу спрайтов врага

window = pygame.display.set_mode((WIDTH, HEIGHT))# задаем размеры окну
clock = pygame.time.Clock()# задаем время игры сейчас оно нужно для фпс
run = True # управление игрой

all_sprites.add(player, enemy)
sprites_enemy.add(enemy)
#сама игра
while run:
    for i in pygame.event.get():# отслеживаем события, которые просходят в окне нажатие, закрытие и т.дю
        if i.type == pygame.QUIT:# если окно закрыли 
            run = False# выходим из цикла
            
    hit = pygame.sprite.spritecollide(player,sprites_enemy,False)# было столкновение
    
    #if enemy.rect.left <= player.rect.right and (player.rect.bottom>=enemy.rect.top>= player.rect.top) and( player.rect.bottom>=enemy.rect.bottom>= player.rect.top):
    if hit:    
        player.kill()# уничтожили игрока
        #break
    window.fill(COLOR)#красим окно здесь же можно потом картинки загружать
    all_sprites.draw(window)
    player.update()#обновляем положение игрока
    enemy.update()#обновляем положение врага
    pygame.display.update()#обновляем экран каждую итерацию
    clock.tick(FPS)#плавно обновляем

pygame.quit()# корректное завершение работы