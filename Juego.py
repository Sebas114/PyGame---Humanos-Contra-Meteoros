import pygame, random
#variables iniciales
WIDTH = 800
HEIGHT= 533

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


pygame.init()
pygame.mixer.init()
# definimos ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego PyGame - Humanos contra Meteoros")
clock = pygame.time.Clock()



#Se define la clase jugador que es la nave espacial
class Player(pygame.sprite.Sprite):
    #Se inicializa la clase
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Objetos/play2.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.shield= 100

    # se crea la función update para controlar la nave desde el teclado
	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
        # Verificamos que el borde de la nave no se salga de la pantalla
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
   
	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)

# Clase para definir enemigos - meteoros
class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(meteor_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)
	# se actualiza la posición
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)

# Clase para definir disparos laser
class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("Objetos/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()
   
# Marcador 
def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)
 
# Barra de vida
def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)  

# Menú inicial 
def show_go_screen():
	screen.blit(background, [0, 0])
	draw_text(screen, "Humanos contra meteoros", 65, WIDTH // 2, HEIGHT / 4)
	draw_text(screen, "La última nave con sobrevivientes esta amenazada por meteoritos asesinos ", 20, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "¡¡Salvala!!!", 24, WIDTH // 2, HEIGHT // 2+20)
	draw_text(screen, "Usa espacio para disparar", 18, WIDTH // 2, HEIGHT // 2+50)
	draw_text(screen, "Usa flechas para mover la nave", 18, WIDTH // 2, HEIGHT // 2+80)
	draw_text(screen, "Presiona una tecla para comenzar", 17, WIDTH // 2, HEIGHT * 3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False

# se cargan las diferentes imagenes de meteoros
meteor_images = []
meteor_list = [ "meteorGrey_med2.png", "meteorGrey_small1.png", "meteorGrey_small2.png",
				"meteorGrey_tiny1.png", "meteorGrey_tiny2.png"]
for img in meteor_list:
	meteor_images.append(pygame.image.load("Objetos/"+img).convert())

# Cargar fondo.
background = pygame.image.load("Objetos/Fondo.jpg").convert()

# se inicializan los grupos de disparo, meteoro y jugador
all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Se inicializa el jugador
player = Player()
all_sprites.add(player)

#Inicializando marcador
score = 0

for i in range(8):
	meteor = Meteor()
	all_sprites.add(meteor)
	meteor_list.add(meteor)

# Loop del juego
game_over = True
running = True
while running:
    # Se verifica si el jugador perdio
	if game_over:
		show_go_screen()
		game_over = False
		all_sprites = pygame.sprite.Group()
		meteor_list = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)

		for i in range(8):
			meteor = Meteor()
			all_sprites.add(meteor)
			meteor_list.add(meteor)

		#Marcador / Score
		score = 0
	
	clock.tick(60)
	
	for event in pygame.event.get():
		# se cierra la ventana si da en quit
		if event.type == pygame.QUIT:
			running = False
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()
		

	# se actualiza
	all_sprites.update()

	# Colisiones meteoro - laser
	hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
	for hit in hits:
		score += 1

		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)

		
	# Colisiones jugador - meteoro
	hits = pygame.sprite.spritecollide(player, meteor_list, True) 
	for hit in hits:
		player.shield -= 20
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)
		if player.shield <= 0:
			game_over = True

	#Dibujo y renderización
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)

	# Marcador
	draw_text(screen,"Puntaje: "+str(score), 25, WIDTH // 2, 10)

	# Vidas.
	draw_shield_bar(screen, 5, 5, player.shield)


	pygame.display.flip()

pygame.quit()

