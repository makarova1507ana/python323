import pygame

BLACK = (0, 0, 0)# цвет в формате rgb этот черный

class Player(pygame.sprite.Sprite):
    def __init__(self, width=50, height=50):
        pygame.sprite.Sprite.__init__(self) # создание спрайта - игровой объект
        self.image = pygame.Surface((width, height)) # размеры игрока
        self.image.fill(BLACK) # цвет
        self.rect = self.image.get_rect()#  получаем его положение
        self.rect.center = (100,100) # передаем координаты центра игрока расположения
        self.speed_x = 3
        self.speed_y = 3

    #влияет на отрисовку игрока
    def update(self, wall):#
        self.check_walls(wall)
        self.run() #отрисовываем перемещение игрока
    
    #передвижение игрока
    def run(self):
        keystate = pygame.key.get_pressed()#узнаем какую клавишу пользователь
        # print(keystate)
        if keystate[pygame.K_DOWN]:# стрелка вниз
            self.rect.y += 3 #изменяем текущее положение
        
        if keystate[pygame.K_LEFT]:# стрелка влево
            self.rect.x -= self.speed_x #изменяем текущее положение
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 3 #изменяем текущее положение
  
        if keystate[pygame.K_UP]:
            self.rect.y -= self.speed_y #изменяем текущее положение
    
    #положение игрока
    def check_walls(self, wall):
        if self.rect.left <= wall.rect.right:
            self.speed_x = 0
        else:
            self.speed_x = 3
        if self.rect.top <= wall.rect.bottom and  (self.rect.left <= wall.rect.right and self.rect.right >= wall.rect.left):
            self.speed_y = 0
        else:
            self.speed_y = 3
   
        