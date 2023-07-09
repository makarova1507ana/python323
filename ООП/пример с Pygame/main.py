import pygame
from Player import Player
pygame.init()# точка входа и настройка игры


#просто переменные
FPS = 60 
WIDTH = 800
HEIGHT = 600
COLOR = (255, 0, 0)# цвет в формате rgb этот красный


#создать игрока
player = Player()
all_sprites = pygame.sprite.Group() # создаем группу спрайтов
window = pygame.display.set_mode((WIDTH, HEIGHT))# задаем размеры окну
clock = pygame.time.Clock()# задаем время игры сейчас оно нужно для фпс
run = True # управление игрой

all_sprites.add(player)

#сама игра
while run:
    for i in pygame.event.get():# отслеживаем события, которые просходят в окне нажатие, закрытие и т.дю
        if i.type == pygame.QUIT:# если окно закрыли 
            run = False# выходим из цикла
    
    
    window.fill(COLOR)#красим окно здесь же можно потом картинки загружать
    all_sprites.draw(window)
    pygame.display.update()#обновляем экран каждую итерацию
    clock.tick(FPS)#плавно обновляем

pygame.quit()# корректное завершение работы