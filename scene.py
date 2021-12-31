import sys, pygame

pygame.init()

screen_width = 640
screen_height = 740

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode ((screen_width, screen_height))


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


def leaderboards():
    return

main_menu()

while True:

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()


    pygame.display.update()