import game_object
from Games.game_settings import *


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Screen set-up
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(PINK)

    def start_game(self):
        dalgona = game_object.Dalgona(self.width, self.height, self.game_screen, 20)
        game_over_timer = GameOverTimer(50)
        while True:
            left_time = game_over_timer.time_checker()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.game_screen.fill(PINK)
            message_to_screen_left(self.game_screen, 'GAME OVER: ' + str(left_time), WHITE, level_font, 0, 0)

            pygame.draw.circle(self.game_screen, YELLOWBROWN, [self.width / 2, self.height / 2], 300, 300)
            pygame.draw.circle(self.game_screen, (175, 118, 43), [self.width / 2 + 10, self.height / 2], 220, 15)
            dalgona.draw()
            if dalgona.check_win():
                self.game_screen.fill(PINK)
                message_to_screen_center(self.game_screen, "승리!", WHITE, korean_font, self.width / 2)
            if left_time <= 0:
                self.game_screen.fill(PINK)
                message_to_screen_center(self.game_screen, "패 배", WHITE, korean_font, self.width / 2)
            pygame.display.update()
            clock.tick(20)


pygame.init()
new_game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.start_game()

pygame.quit()
quit()