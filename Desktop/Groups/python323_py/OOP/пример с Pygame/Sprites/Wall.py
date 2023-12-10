import pygame
COLOR = (100, 100, 100)# цвет в формате rgb 
class Wall(pygame.sprite.Sprite):
    def __init__(self, width=50, height=50,x=25,y=25):
        pygame.sprite.Sprite.__init__(self) # создание спрайта - игровой объект
        self.image = pygame.Surface((width, height)) # размеры игрока
        self.image.fill(COLOR) # цвет
        self.rect = self.image.get_rect()#  получаем его положение
        self.rect.center = (x,y) # передаем координаты центра игрока расположения
    