"""
Changes in this:
1) improved hover cross

"""


import pygame
from random import choice as chooseRandom


class Board():

    def __init__(self):

        self.board = dict()

        self.current_position = []

        self.increase = 100
        initial_x_point = 150
        initial_y_point = 50

        for i in range(1, 10):

            if i == 1:
                x_point = initial_x_point
                y_point = initial_y_point
            elif i == 4:
                x_point = initial_x_point
                y_point = initial_y_point + self.increase
            elif i == 7:
                x_point = initial_x_point
                y_point = initial_y_point + self.increase * 2
            else:
                x_point = x_point + self.increase

            self.board[(x_point, y_point)] = ''


    def mark(self, location, player_symbol):

        self.board[location] = player_symbol


    def draw(self):

        for key, value in self.board.items():

            pygame.draw.rect(
                gameDisplay,
                black,
                ((key), (self.increase, self.increase)),
                2
            )

            if value == 'x':
                drawCross(blue, (key[0] + 35, key[1] + 30), 30)
            if value == 'o':
                drawCircle(blue, (key[0] + 50, key[1] + 50), 25)

    def checkInput(self, click_position):

        click_rect = pygame.Rect(click_position, (1, 1))

        for key, value in self.board.items():

            region = pygame.Rect(key, (self.increase, self.increase))
            if region.contains(click_rect):
                if value == '':
                    self.current_position = key
                    return True

        return False


def alternatePlayer(current):

    if current == 'x':
        return 'o'

    return 'x'


def drawCircle(colour, location, radius):

    return pygame.draw.circle(gameDisplay, colour, location, radius)


def drawCross(colour, start_point, size):

    a_point = start_point
    c_point = (start_point[0] + size, start_point[1])
    b_point = (start_point[0], start_point[1] + size)
    d_point = (start_point[0] + size, start_point[1] + size)

    pygame.draw.line(gameDisplay, colour, a_point, d_point, 15)
    pygame.draw.line(gameDisplay, colour, b_point, c_point, 15)

    return pygame.draw.rect(
        gameDisplay,
        white,
        (start_point[0] - 10, start_point[1] -  10, size + 20, size + 20),
         1
    )


def game_intro():

    welcome_text = welcome_font.render('Welcome to Tic Tac Toe', False, black)

    choose_text = game_font.render('Choose', True, black)
    or_text = game_font.render('OR', True, black)

    intro = True
    circle_hover = False
    cross_hover = False

    while intro:

        gameDisplay.fill(white)

        gameDisplay.blit(welcome_text, [110, 30])
        gameDisplay.blit(choose_text, [185, 142])
        gameDisplay.blit(or_text, [266, 225])
        gameDisplay.blit(choose_text, [185, 305])

        if circle_hover:
            circle_rect = drawCircle(light_blue, (330, 150), 45)
        else:
            circle_rect = drawCircle(blue, (330, 150), 35)

        if cross_hover:
            cross_rect = drawCross(light_blue, (300, 280), 65)
        else:
            cross_rect = drawCross(blue, (310, 290), 45)

        for event in pygame.event.get():
            # print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEMOTION:

                if circle_rect.collidepoint(mouse_position):
                    circle_hover = True
                else:
                    circle_hover = False

                if cross_rect.collidepoint(mouse_position):
                    cross_hover = True
                else:
                    cross_hover = False

            if event.type == pygame.MOUSEBUTTONUP:

                if circle_rect.collidepoint(mouse_position):
                    player1 = 'o'
                    intro = False

                if cross_rect.collidepoint(mouse_position):
                    player1 = 'x'
                    intro = False

        clock.tick(30)
        pygame.display.update()

    return player1


def play(player1):

    bot = alternatePlayer(player1)

    print(player1, bot)

    current_player = chooseRandom((player1, bot))

    board = Board()

    play = True
    while play:

        gameDisplay.fill(white)

        board.draw()

        for event in pygame.event.get():
            # print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            click_position = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if board.checkInput(click_position):
                    board.mark(board.current_position, current_player)
                    # if board.checkWin():
                    #     play = False
                    # else:
                    current_player = alternatePlayer(current_player)

        clock.tick(30)
        pygame.display.update()



pygame.init()

display_width = 600
display_height = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')

black = (0, 0, 0)
blue = (0, 150, 255)
light_blue = (100, 185, 255)
white = (255,255,255)

welcome_font = pygame.font.Font(None, 50)
game_font = pygame.font.Font(None, 35)

clock = pygame.time.Clock()

player1 = game_intro()
play(player1)
game_over(player)
