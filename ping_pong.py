import pygame
pygame.init()

scene_width = 600
scene_length = 500
scene_title = "Ping Pong 101"
GAME_RUN = True
GAME_FINISH = False

bg_img = "bgbgbgbg.jpg"
bomb_img = "bomb.png"
player1_img = "lol.png"
bg_music = "jungles.ogg"

scene = pygame.display.set_mode((scene_width, scene_length))
FPS = pygame.time.Clock()
scene_bg = pygame.transform.scale(pygame.image.load(bg_img), (scene_width, scene_length))

pygame.mixer.init()
pygame.mixer.music.load(bg_music)
pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
   def __init__(self, gambar, x, y, width, length, kecepatan):
       super().__init__()
       self.width = width
       self.length = length
       self.image = pygame.transform.scale(
           pygame.image.load(gambar), (self.width, self.length))   
       self.speed = kecepatan
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
   def reset(self):
       scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if button[pygame.K_s] and self.rect.y < scene_length - self.length:
            self.rect.y += self.speed
    def update_right(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if button[pygame.K_DOWN] and self.rect.y < scene_length - self.length:
            self.rect.y += self.speed

player_left = Player(player1_img, 10, 10, 50, 100, 20)
player_right = Player(player1_img, scene_width-60, 10, 50, 100, 20)

while GAME_RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUN = False
    if GAME_FINISH == False:
        scene.blit(scene_bg, (0,0))
        player_left.reset()
        player_right.reset()
        player_left.update_left()
        player_right.update_right()
    
    FPS.tick(60)
    pygame.display.update()