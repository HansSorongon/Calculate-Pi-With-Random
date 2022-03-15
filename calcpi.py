import pygame, sys

from random import random

class CalcPi:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Calculate Pi")

        try:
            self.blip = pygame.mixer.Sound("sounds/blip.wav")
            self.blip.set_volume(0.1)
        except:
            print("No sound found.")

        self.circles = []
        self.pi = 0.
        self.points_in = 0
        self.total_points = 3000
        self.buffer = 0

        self.muted = False

    def draw_rect(self):
        rect = pygame.Surface((400,400))
        rect.set_alpha(50)
        rect.fill('green')
        self.screen.blit(rect, (0,0))

    def display_text(self):
        font = pygame.font.SysFont('Calibri', 32)
        text = font.render(f" π = {format(self.pi, '.4f')}", True, 'white')
        pygame.draw.rect(self.screen, 'black', (0,0,150,30))
        self.screen.blit(text, (0,0))

    def draw_circle(self, x, y):
        pygame.draw.circle(self.screen, 'red', (x,y), 1)

    def run_game(self):

        # UI Loop
        while True:
            self.screen.fill('white')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_w:
                        if not self.muted:
                            try:
                                self.blip.set_volume(0)
                            except:
                                print("No sound found.")
                            self.muted = True
                        else:
                            try:
                                self.blip.set_volume(0.1)
                            except:
                                print("No sound found.")
                            self.muted = False

            # MAIN ALGORITHM
            if self.buffer < self.total_points:

                x = random()
                y = random()

                distance = (x**2 + y**2) ** 0.5

                self.circles.append([int((x*400)),int(y*400)])

                if distance < 1:
                    self.points_in += 1
                    try:
                        pygame.mixer.Sound.play(self.blip)
                    except:
                        print("No sound found.")
                self.buffer += 1

                self.pi = 4*self.points_in/self.total_points

            pygame.draw.circle(self.screen, 'black', (400,400), 400, 5)

            for circle in self.circles:
                 pygame.draw.circle(self.screen, 'red', (circle[0],circle[1]), 3)

            self.draw_rect()

            self.display_text()
            self.clock.tick(0)
            pygame.display.update()

if __name__ == "__main__":
    inst = CalcPi()
    inst.run_game()
