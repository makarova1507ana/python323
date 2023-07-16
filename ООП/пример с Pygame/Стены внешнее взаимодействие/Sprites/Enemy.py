import pygame
GREEN = (0, 255, 0)# цвет в формате rgb этот зеленый

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width=50, height=50, x=500, y=100):
        pygame.sprite.Sprite.__init__(self) # создание спрайта - игровой объект
        self.image = pygame.Surface((width, height)) # размеры игрока
        self.image.fill(GREEN) # цвет
        self.rect = self.image.get_rect()#  получаем его положение
        self.rect.center = (x,y) # передаем координаты центра игрока расположения
    
    #влияет на отрисовку игрока
    def update(self):#
        self.run() #отрисовываем перемещение игрока
    
    #передвижение игрока
    def run(self):
        self.rect.x -= 1 