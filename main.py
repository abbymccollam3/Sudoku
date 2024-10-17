import pygame
import sys
import math

# Initialize pygame
pygame.init()

WIDTH = 540
HEIGHT = 540
GRID_SIZE = WIDTH // 9 # 60

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # creates screen for display
pygame.display.set_caption("Sudoku") # sets title of display

# defines colors using RGB
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# first need to draw grid
def draw_grid():
    for i in range(10):  # Draw horizontal and vertical grid lines
        if i % 3 == 0:
            thickness = 4  # Thicker lines for 3x3 subgrids
        else:
            thickness = 1
        #pygame.draw.line(surface, color, start_pos, end_pos, thickness)
        pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), thickness)  # Horizontal lines
        pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), thickness)  # Vertical lines

# function for drawing numbers in grid
def draw_numbers(board):
    font = pygame.font.SysFont('Arial', 40)  # font of numbers
    for i in range(9):
        for j in range(9): # iterating over 9x9 grid
            if board[i][j] != 0: # when value of number is not 0
                #  Note: antialiasing makes text smoother so set to True
                text = font.render(str(board[i][j]), True, BLACK) # params: text, antialias, color
                screen.blit(text, (j * GRID_SIZE + 20, i * GRID_SIZE + 10)) # params: text, (x, y)

# enable user to click on the screen
def mouse_click():
    waiting_for_input = True
    user_input = ''
    font = pygame.font.SysFont('Arial', 40)  # font of numbers

    # get position of mouse click
    mousex, mousey = pygame.mouse.get_pos() # (x,y)
    a = mousex // 60
    b = mousey // 60

    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit() and board[a][b] == 0:
                    user_input += event.unicode
                    text = font.render(str(user_input), True, BLACK) # params: text, antialias, color
                    screen.blit(text, (a * GRID_SIZE + 20, b * GRID_SIZE + 10)) # params: text, (x, y)
                    pygame.display.flip()  # updates the display

                if event.key == pygame.K_RETURN and user_input:
                        board[a][b] = int(user_input)  # Update the board
                        waiting_for_input = False
                    
def main():
    running = True
    while running:
        screen.fill(WHITE) # fill screen with white background
        draw_grid() # call draw grid function
        draw_numbers(board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # run function
                mouse_click()

        pygame.display.flip()  # updates the display

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
