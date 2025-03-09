import pygame

pygame.init()  
SCREEN = pygame.display.set_mode((1280, 720))  
CLOCK = pygame.time.Clock()  
RUNNING = True  
FRAMERATE = 60

#background_color = ((19, 57, 135))
background_color = pygame.Color(19, 57, 135)




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
		
    pygame.Surface.fill(SCREEN, background_color)
    pygame.display.update()

    CLOCK.tick(FRAMERATE)