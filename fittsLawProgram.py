import pygame
import sys
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 50
LEFT_SQUARE_POS = (350 - 12.5, SCREEN_HEIGHT // 2)
RIGHT_SQUARE_POS = (SCREEN_WIDTH - (400-12.5), SCREEN_HEIGHT // 2)
START_BUTTON_RECT = pygame.Rect(300, 250, 200, 100)
END_BUTTON_RECT = pygame.Rect(350, 250, 100, 50)


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLUE = (0,0,255)

PURPLE = (255,0,255)
BLACK = (0,0,0)

DATA_FILE = "fitts_law_times.txt"  # File to store time data

class FittsLawExperiment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fitts' Law Experiment")
        self.clock = pygame.time.Clock()
        self.start_button_clicked = False

        self.distance = 25/2
        self.left_square_pos = (350 - self.distance, SCREEN_HEIGHT // 2)
        self.right_square_pos = (SCREEN_WIDTH - (400-self.distance), SCREEN_HEIGHT // 2)

        self.current_target = self.left_square_pos
        self.targets_clicked = 0
        self.start_time = None
        self.times = 0
        self.threeTimes = 1

        self.squareSize = 50

        self.time_data = []
        self.trial_number = 1

        with open(DATA_FILE, "w") as file:
            file.write(f"Trial {self.trial_number}\n")
        
    def write_to_file(self):
        with open(DATA_FILE, "a") as file:
            for time_entry in self.time_data:
                file.write(f"{time_entry}\n")
            self.trial_number = self.trial_number + 1
            
            self.time_data = []
            if self.trial_number != 16:
                file.write(f"\n Trial {self.trial_number}\n")
            
            

    def draw_start_screen(self):
        self.screen.fill(WHITE)
        
        font = pygame.font.Font(None, 36)
        if self.times == 0:
            text = font.render("Click Button to Start Trials", True, (0, 0, 0))
            pygame.draw.rect(self.screen, BLACK, START_BUTTON_RECT)
        else:
            text = font.render("Click Button to Start Next Trial", True, (0, 0, 0))
            pygame.draw.rect(self.screen, GREEN, START_BUTTON_RECT)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw_end_screen(self):
        self.times = self.times + 1
        self.threeTimes = self.threeTimes + 1
        self.targets_clicked = 0

        experiment.completion_screen()

        if self.times != 15:
            if self.threeTimes == 4:
                self.squareSize = 50
                self.threeTimes = 1

                self.distance = self.distance * 2
                self.left_square_pos = (350 - self.distance, SCREEN_HEIGHT // 2)
                self.right_square_pos = (SCREEN_WIDTH - (400-self.distance), SCREEN_HEIGHT // 2)

                
                self.current_target = self.left_square_pos
                experiment.run_experiment()
                return

            self.left_square_pos = (350 - self.distance, SCREEN_HEIGHT // 2)
            self.right_square_pos = (SCREEN_WIDTH - (400-self.distance), SCREEN_HEIGHT // 2)
            self.squareSize = 50 - (5 * self.threeTimes)
            
            self.current_target = self.left_square_pos
            experiment.run_experiment()
            return


        start_button_pressed = False
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, PURPLE, START_BUTTON_RECT)
        font = pygame.font.Font(None, 36)
        text = font.render("Congratulations, you've completed all trials!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        while not start_button_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if START_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
                        start_button_pressed = True

            self.clock.tick(60)

    def completion_screen(self):
        start_button_pressed = False
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, BLUE, END_BUTTON_RECT)
        font = pygame.font.Font(None, 36)
        text = font.render("You've completed this trial. Click button to proceed.", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        while not start_button_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if END_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
                        start_button_pressed = True

            self.clock.tick(60)
        return

    def draw_squares(self):
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.left_square_pos, (self.squareSize, self.squareSize)))
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.right_square_pos, (self.squareSize, self.squareSize)))

    def switch_target(self):
        if self.current_target == self.left_square_pos:
            self.current_target = self.right_square_pos
            print(f"Left block clicked!")
        else:
            self.current_target = self.left_square_pos
            print(f"Right block clicked!")

    def run_experiment(self):
        self.draw_start_screen()
        start_button_pressed = False

        while not start_button_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if START_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
                        start_button_pressed = True

            self.clock.tick(60)

        running = True
        while running:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if pygame.Rect(self.current_target, (self.squareSize, self.squareSize)).collidepoint(mouse_x, mouse_y):
                        if self.start_time is None:
                            self.start_time = time.time()
                        else:
                            elapsed_time = time.time() - self.start_time
                            print(f"Time taken: {elapsed_time} seconds")
                            self.time_data.append(elapsed_time)
                            self.start_time = None

                        

                        self.targets_clicked += 1
                        if self.targets_clicked == 2:
                            running = False
                            self.write_to_file()
                        
                        self.switch_target()

            self.draw_squares()
            pygame.display.flip()
            self.clock.tick(60)

        self.draw_end_screen()
        return


if __name__ == "__main__":
    experiment = FittsLawExperiment()
    experiment.run_experiment()
