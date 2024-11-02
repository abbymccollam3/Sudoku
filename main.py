# Author: Abby McCollam

# TO DO
# allow user to delete variables
# do you need both board and myboard

import pygame
import sys
import math
import random

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

# completed sudoku board
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

myboard = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
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

# function to rnadomize blank spots in grid
def erase_portion(board):
    total_cells = 81
    filled_cells = total_cells
    # at least 17 squares have to be filled
    for i in range(9):
        for j in range (9):
            if filled_cells > 17:
                choice = random.randint(0, 1)
                if choice == 1:
                    board[i][j] = 0
                    filled_cells -= 1

    pygame.display.flip()

# enable user to click on the screen
def mouse_click(board, answer):
    
    font = pygame.font.SysFont('Arial', 40)  # font of numbers

    # get position of mouse click
    mousex, mousey = pygame.mouse.get_pos() # (x,y)
    a = (mousex // 60)
    b = (mousey // 60)

    # waits for user click
    waiting_for_input = True

    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
                pygame.quit()
                sys.exit()

            # if a key is pressed
            elif event.type == pygame.KEYDOWN:
            
                # if input is a digit and the current spot is a 0
                if event.unicode.isdigit() and board[b][a] == 0:

                    # set board space equal to input
                    board[b][a] = int(event.unicode)

                    # clear and refresh screen
                    screen.fill(WHITE) 
                    draw_grid()  
                    draw_numbers(board) 
                    pygame.display.flip() 

                    keytype = pygame.key.name(event.key)
                    print(f"Keytype: {keytype}")

                    # if input key does not equal answer
                    if int(keytype) != myboard[b][a]:
                        print (f"board: {board[b][a]}")
                        answer = False

                    waiting_for_input = False
                
                elif event.key == pygame.K_BACKSPACE:
                    board[b][a] = 0
                    print("Hi and hello")

                    # Refresh the screen after deletion
                    screen.fill(WHITE)
                    draw_grid()
                    draw_numbers(board)
                    pygame.display.flip()
                
    return answer

def check_filled(board):
    
    for row in board:
        if 0 in row:
            return False

    # only returns True if the board has no 0s
    return True
      
                    
def main():
    running = True
    answer = True
    filled = True

    erase_portion(board)

    while running:
        screen.fill(WHITE) # fill screen with white background
        draw_grid() # call draw grid function
        draw_numbers(board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # run function and check input
                answer = mouse_click(board, answer)
                print (f"Answer: {answer}")

        pygame.display.flip()  # updates the display

        # keep checking if board is filled
        filled = check_filled(board)

        # once board is filled check answer and filled
        if filled:
            # return result of board
            if answer:
                print("Hooray! You answered correctly.")    
            else:
                print ("You do not have the correct answer")
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
