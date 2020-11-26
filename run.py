import pygame
import sys
import time
import game

# initialize Pygame
pygame.init()

# write caption
pygame.display.set_caption("Tic Tac Toe")
# set Pygame window size
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# define color
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)

# define the fonts 
my_font = pygame.font.Font("Lets-Play.ttf", 35)
sign_font = pygame.font.Font("Sore.ttf", 45)

def print_msg():
    # commands message
    message = my_font.render("r - restart | esc - exit", True, white)
    msgRect = message.get_rect()
    msgRect.center = (window_width/2, 300)
    window.blit(message, msgRect)

# set user's player to X
user = game.X
grid = game.grid
ai_turn = False
window.fill(grey)

while True:
    # close the screen when the window x is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        # close the screen when esc is clicked
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    # Draw game grid
    section_size = 200
    section_origin = (window_width / 2 - (1.5 * section_size),
                    window_height/ 2 - (1.5 * section_size))
    section = []
    for x in range(3):
        row = []
        for y in range(3):
            rect = pygame.Rect(
                section_origin[0] + y * section_size,
                section_origin[1] + x * section_size,
                section_size, section_size
            )
            pygame.draw.rect(window, black, rect, 3)

            if grid[x][y] != game.EMPTY:
                move = sign_font.render(grid[x][y], True, black)
                moveRect = move.get_rect()
                moveRect.center = rect.center
                window.blit(move, moveRect)
            row.append(rect)
        section.append(row)

    game_over = game.terminal(grid)
    player = game.player(grid)
    winner = game.winner(grid)

    # Check for AI move
    if user != player and not game_over:
        if ai_turn:
            time.sleep(0.5)
            move = game.minimax(grid)
            grid = game.result(grid, move)
            ai_turn = False
        else:
            ai_turn = True

    # Check for a user move
    rightClick, _, _ = pygame.mouse.get_pressed()
    if rightClick == 1 and user == player and not game_over:
        mouse = pygame.mouse.get_pos()
        for i in range(3):
            for j in range(3):
                if (grid[i][j] == game.EMPTY and section[i][j].collidepoint(mouse)):
                    grid = game.result(grid, (i, j))

    if game_over:
        window.fill(black)
        # print winner
        if winner == None:
            message = my_font.render("It's a draw!", True, white)
        else:
            message = my_font.render("Player " + str(winner) + " wins!", True, white)
            
        msgRect = message.get_rect()
        msgRect.center = (window_width/2, 150)
        window.blit(message, msgRect)
        print_msg()

        user = game.O
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # restart the game when r is clicked
                if event.key == pygame.K_r:
                    window.fill(grey)
                    user = game.X
                    grid = game.grid

    pygame.display.update()