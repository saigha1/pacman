import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))
board = ['WWWWWWWW', 
         'W......W', 
         'W......W', 
         'W......W',
         'W......W', 
         'W......W',
         'W......W',
         'W......W',
         'W......W',
         'W......W',
         'W......W',
         'W......W',
         'W......W',
         'WWWWWWWW']
board = [list(row) for row in board]
pellets_remaining = sum(row.count('.') for row in board)

score = 0
font = pygame.font.SysFont(None, 36)

TILE_SIZE = 24
vel_x = 0 
vel_y = 0

player_x = 1 * TILE_SIZE + TILE_SIZE // 2
player_y = 1 * TILE_SIZE + TILE_SIZE // 2

game_state = "playing"
running = True
while running:
    if game_state == "playing":
        screen.fill((0, 0, 0))
        speed = 2
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:    vel_x = -speed
                elif event.key == pygame.K_RIGHT: vel_x = speed
                elif event.key == pygame.K_UP:    vel_y = -speed
                elif event.key == pygame.K_DOWN:  vel_y = speed

            # Stop moving when key is released
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT): vel_x = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):    vel_y = 0

        new_x = player_x + vel_x 
        new_y = player_y + vel_y
        size = 10

        corners = {
            (new_x - size, new_y - size),   #top-left
            (new_x + size - 1, new_y - size),  #top-right
            (new_x - size, new_y + size - 1),       #bottom-left
            (new_x + size - 1, new_y + size - 1)        #bottom-right
        }


        #Iterates through the screen to draw the board
        for r, row in enumerate(board):
            for c, character in enumerate(row):
                x_pixel = c * TILE_SIZE
                y_pixel = r * TILE_SIZE 
                
                if character == 'W':
                    #Draws the Blue walls
                    pygame.draw.rect(screen, (0, 0, 255), (x_pixel, y_pixel, TILE_SIZE, TILE_SIZE))
                elif character == '.':
                    #Drawing Pellets
                    pygame.draw.circle(screen, (255, 255, 255), (x_pixel + 12, y_pixel + 12), 2 )

                    
        #Draw a circle
        pygame.draw.circle(screen, (255,255,0), (player_x,player_y), 10)
        
        keys = pygame.key.get_pressed()

        current_grid_x = player_x // TILE_SIZE
        current_grid_y = player_y // TILE_SIZE    
        

        grid_x = new_x // TILE_SIZE
        grid_y = new_y // TILE_SIZE


        #This checks the corners of the pacman if it can move
        can_move = True
        for cx, cy in corners:
            grid_x = cx // TILE_SIZE
            grid_y = cy //TILE_SIZE

            if board[grid_y][grid_x] == 'W':
                can_move = False
                break

        if can_move:
            player_x = new_x
            player_y = new_y



        if board[current_grid_y][current_grid_x] == '.':
            board[current_grid_y][current_grid_x] = ' '
            score += 10
            pellets_remaining -= 1
            

            if pellets_remaining == 0:
                game_state = "level_complete"                

        text_surface = font.render("Score: " + str(score), True, (255,255,255))
        screen.blit(text_surface, (10, 10))

        clock.tick(60)

    elif game_state == "level_complete":
        text_surface = font.render("Level Complete!", True, (255,255,255))
        screen.blit(text_surface, (200, 180))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:  # Press Enter to restart
            board = [list(row) for row in ['WWWWW', 'W...W', 'W...W', 'W...W', 'WWWWW']]
            pellets_remaining = sum(row.count('.') for row in board)
            player_x, player_y = 100, 100
            score = 0
            game_state = "playing"


    
    pygame.display.flip()


pygame.quit()