import pygame
BLACK = (0, 0, 0)# цвет в формате rgb этот красный

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # создание спрайта - игровой объект
        self.image = pygame.Surface((50, 50)) # размеры игрока
        self.image.fill(BLACK) # цвет
        self.rect = self.image.get_rect()#  получаем его положение
       # self.image.get_width = 50 # ширина игрока
        self.rect.center = (100,100) # передаем координаты центра игрока расположения