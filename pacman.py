import pygame


pygame.init()
screen = pygame.display.set_mode((600, 400))
board = ['WWWWW', 
         'W   W', 
         'W   W', 
         'W   W', 
         'WWWWW']
TILE_SIZE = 24

player_x = 100
player_y = 100

running = True
while running:
    screen.fill((0, 0, 0))
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for r, row in enumerate(board):
        for c, character in enumerate(row):
            if character == 'W':
                x_pixel = c * TILE_SIZE
                y_pixel = r * TILE_SIZE 

                #Draws the Blue walls
                pygame.draw.rect(screen, (0, 0, 255), (x_pixel, y_pixel, TILE_SIZE, TILE_SIZE))

                



    pygame.display.flip()





pygame.quit()



