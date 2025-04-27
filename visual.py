import pygame

from ship import Player

pygame.init()  
SCREEN = pygame.display.set_mode((1280, 720))  
CLOCK = pygame.time.Clock()  
RUNNING = True  
FRAMERATE = 60

#background_color = ((19, 57, 135))
background_color = pygame.Color(19, 57, 135)

x = 640
y = 535
radius = 15
u, v = 0, 0

player = Player()
def coords_update(cx : int, cy : int, ax : int, ay : int) :
	"""
	update coordinates
	"""
	cx += ax
	cy += ay
	return cx, cy



def handle_event(ev: pygame.event.Event) -> None:
	"""
	Handle user inputs.
	"""
	if ev.type == pygame.QUIT:  
		global RUNNING  
		RUNNING = False 
	


while RUNNING:
	

	for event in pygame.event.get():  
		handle_event(event) 
	
	userInput = pygame.key.get_pressed()

	if userInput[pygame.K_LEFT]:
		u, v = player.move(-1, 0, 7)
		x, y = coords_update(x, y, u, v)
	if userInput[pygame.K_RIGHT]:
		u, v = player.move(1, 0, 7)
		x, y = coords_update(x, y, u, v)
	if userInput[pygame.K_UP]:
		u, v = player.move(0, -1, 7)
		x, y = coords_update(x, y, u, v)
	if userInput[pygame.K_DOWN]:
		u, v = player.move(0, 1, 7)
		x, y = coords_update(x, y, u, v)



	pygame.Surface.fill(SCREEN, background_color)
	pygame.draw.circle(SCREEN, (255,255,255), (int(x), int(y)), radius)
	pygame.display.update()

	CLOCK.tick(FRAMERATE)