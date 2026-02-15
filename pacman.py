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


    new_x = player_x
    new_y = player_y
    keys = pygame.key.get_pressed()

        
    #go right
    if keys[pygame.K_RIGHT]:
        new_x += 2

    #go left
    if keys[pygame.K_LEFT]:
        new_x -=  2

    #go up
    if keys[pygame.K_UP]:
        new_y -=  2

    #go down
    if keys[pygame.K_DOWN]:
        new_y += 2


    grid_x = new_x // TILE_SIZE
    grid_y = new_y // TILE_SIZE

    #Iterates through the screen to draw the board
    for r, row in enumerate(board):
        for c, character in enumerate(row):
            if character == 'W':
                x_pixel = c * TILE_SIZE
                y_pixel = r * TILE_SIZE 

                #Draws the Blue walls
                pygame.draw.rect(screen, (0, 0, 255), (x_pixel, y_pixel, TILE_SIZE, TILE_SIZE))

                
    #Draw a circle
    pygame.draw.circle(screen, (255,255,0), (player_x,player_y), 10)





    pygame.display.flip()





pygame.quit()



