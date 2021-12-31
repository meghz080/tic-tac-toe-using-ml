import pygame, sys
import scene

pygame.init ()

screen_width = 640
screen_height = 740
square_size = 200

line_thickness = 10

board_rows = 3
board_cols = 3

bg_color = (28, 170, 156)
line_color = (23, 145, 135)
color_light = (170,170,170)
color_dark = (100,100,100)
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode ((screen_width, screen_height))
font = pygame.font.Font('freesansbold.ttf', 32)
title = font.render('TIC - TAC - TOE', True, white)
title_rect = title.get_rect ()
title_rect.center = (320, 25)


tic_tac_toe_board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

ttt = {
	0 : [[0, 0], [0, 1], [0, 2], [110, 55], [110, 685]],
	1 : [[1, 0], [1, 1], [1, 2], [320, 55], [320, 685]],
	2 : [[2, 0], [2, 1], [2, 2], [530, 55], [530, 685]],
	3 : [[0, 0], [1, 0], [2, 0], [5, 160], [635, 160]],
	4 : [[0, 1], [1, 1], [2, 1], [5, 370], [635, 370]],
	5 : [[0, 2], [1, 2], [2, 2], [5, 580], [635, 580]],
	6 : [[0, 0], [1, 1], [2, 2], [5, 55], [635, 685]],
	7 : [[0, 2], [1, 1], [2, 0], [635, 55], [5, 685]]
}

symbol = ['X', 'O', '*']
player = 0

player_log = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

global game_over
game_over = False


def render_text(font_type, font_size, font_color, font_text, text_rect_center):

    font = pygame.font.Font(font_type, font_size)
    text = font.render(font_text, True, font_color)
    text_rect = text.get_rect ()
    text_rect.center = text_rect_center
    screen.blit (text, text_rect)


def main_menu():

    screen.fill (white)

    solo = "solo"
    vs = "vs"
    leaderboards = "leaderboards"
    exit = "exit"

    font = "freesansbold.ttf"

    pygame.draw.rect (screen, black, pygame.Rect(150, 95, 340, 100), 2)
    render_text(font, 40, black, solo, (320, 145))

    pygame.draw.rect (screen, black, pygame.Rect(150, 245, 340, 100), 2)
    render_text(font, 40, black, vs, (320, 295))

    pygame.draw.rect (screen, black, pygame.Rect(150, 395, 340, 100), 2)
    render_text(font, 40, black, leaderboards, (320, 445))

    pygame.draw.rect (screen, black, pygame.Rect(150, 545, 340, 100), 2)
    render_text(font, 40, black, exit, (320, 595))


def set_prototype_screen ():

    pygame.display.set_caption ("TIC-TAC-TOE")
    screen.fill (bg_color)

    render_text("freesansbold.ttf", 32, white, "TIC-TAC-TOE", (320, 25))

    pygame.draw.lines (screen, line_color, True, [(5, 55), (635, 55), (635, 685), (5, 685)], line_thickness)
    pygame.draw.line (screen, line_color, (215, 55), (215, 685), line_thickness)
    pygame.draw.line (screen, line_color, (425, 55), (425, 685), line_thickness)
    pygame.draw.line (screen, line_color, (5, 265), (635, 265), line_thickness)
    pygame.draw.line (screen, line_color, (5, 475), (635, 475), line_thickness)


def game_logic (row, col, player):

    tic_tac_toe_board[row][col] = symbol[player]

    for x in range (0, 8):
        if [row, col] in ttt[x]:
            player_log [player][x] += 1

    for x in range(0, 8):

        if player_log [0][x] == 3:

            draw_lines (x)
            game_over = True
            print (str(player) + " wins!")
            return True

        if player_log [1][x] == 3:

            draw_lines (x)
            game_over = True
            print (str(player) + " wins!")
            return True


def available_square (row, col):
    return tic_tac_toe_board[row][col] == '*'


def mark_square (row, col, player):
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render(symbol[player], True, white)
    text_rect = text.get_rect ()
    text_rect.center = (int( row*square_size + (square_size+ (row+1)*20)//2), int(col*square_size+ (square_size+ (col+1)*20)//2 + 50))
    screen.blit(text, text_rect)


def draw_lines (x):
    #(i_start, j_start) = (int(ttt[x][0][0]*square_size + (square_size+ (ttt[x][0][0]+1)*20)//2), int(ttt[x][0][1]*square_size+ (square_size+ (ttt[x][0][1]+1)*20)//2 + 50))
    #(i_end, j_end) = (int(ttt[x][2][0]*square_size + (square_size+ (ttt[x][2][0]+1)*20)//2), int(ttt[x][2][1]*square_size+ (square_size+ (ttt[x][2][1]+1)*20)//2 + 50))
    pygame.draw.line (screen, black, (ttt[x][3][0], ttt[x][3][1]), (ttt[x][4][0], ttt[x][4][1]), line_thickness)


def restart ():
    screen.fill (bg_color)
    set_prototype_screen()
    for i in range(3):
        for j in range(3):
            tic_tac_toe_board[i][j] = '*'


def main_menu():
    solo = "solo"
    vs = "vs"
    leaderboards = "leaderboards"
    exit = "exit"
    screen.fill (bg_color)

    return


def leaderboards():
    return


def exit():
    sys.exit ()


set_prototype_screen()

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mposx = event.pos[0]
            mposy = event.pos[1]

            clicked_row = int (mposx // square_size)
            clicked_col = int ((mposy-55) //square_size)

            if available_square (clicked_row, clicked_col):

                mark_square (clicked_row, clicked_col, player)

                if (game_logic(clicked_row, clicked_col, player)):
                    game_over = True

                if player == 0:
                    player = 1
                elif player == 1:
                    player = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                restart()
                player = 0
                game_over = False
                player_log = [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]
            elif event.key == pygame.K_m:
                main_menu()
                player = 0
                game_over = False
                player_log = [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]


    pygame.display.update()

