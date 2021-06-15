import pygame

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 8
FRAMERATE = 60
# define classes


class Ball:
    RADIUS = 25

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), Ball.RADIUS)

    def update(self):
        global bgColor, fgColor
        newX = self.x + self.vx
        newY = self.y + self.vy

        if newX < BORDER + Ball.RADIUS:
            self.vx = -self.vx
        elif newY < BORDER + Ball.RADIUS or newY > HEIGHT-BORDER-Ball.RADIUS:
            self.vy = -self.vy

        elif newX + Ball.RADIUS > WIDTH-Paddle.WIDTH and abs(newY-paddle.y) < Paddle.HEIGHT//2:
            self.vx = -self.vx
        else:

            self.show(bgColor)
            self.x = newX
            self.y = newY
            self.show(fgColor1)


class Paddle:
    WIDTH = 20
    HEIGHT = 90

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color,
                         pygame.Rect(
                             WIDTH - self.WIDTH, self.y - self.HEIGHT//2, self.WIDTH, self.HEIGHT))

    def update(self):
        newY = pygame.mouse.get_pos()[1]
        if newY - self.HEIGHT//2 > BORDER and newY + self.HEIGHT//2 < HEIGHT-BORDER:
            self.show(bgColor)
            self.y = newY
            self.show(fgColor)


# initialize game
pygame.init()

# window screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# making rectangle
fgColor1 = pygame.Color("white")
bgColor = pygame.Color("black")
fgColor = pygame.Color("red")
pygame.draw.rect(screen, fgColor,
                 pygame.Rect((0, 0), (WIDTH, BORDER)))

pygame.draw.rect(screen, fgColor,
                 pygame.Rect(0, 0, BORDER, HEIGHT))

pygame.draw.rect(screen, fgColor,
                 pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))

# create objects
ball = Ball(WIDTH-Ball.RADIUS-1, HEIGHT//2, -VELOCITY, -VELOCITY)
ball.show(fgColor1)

paddle = Paddle(HEIGHT//2)
paddle.show(fgColor)

clock = pygame.time.Clock()
# making a loop(infinite) till an event is reached
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)

    pygame.display.flip()
    ball.update()
    paddle.update()

pygame.quit()
