import pgzrun 
from random import randint 

TITLE = "FLAPPY BALL"
HEIGHT = 600
WIDTH = 800

GRAVITY = 2000
RED = randint(0,255)
GREEN = randint(0,255)
BLUE = randint(0,255)


class Ball():
    def __init__(self, initial_x, initial_y):
        self.y = initial_y
        self.x = initial_x
        self.vx = 200
        self.vy = 0 
        self.radius = 40

    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,(RED,GREEN,BLUE))


ball = Ball(50,100)

def draw():
    screen.clear()
    ball.draw()

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500

def update(dt):
    updated_y = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (updated_y + ball.vy) * 0.5 * dt
    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius 
        ball.vy = -ball.vy * 0.9
    ball.x += ball.vx * dt 
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx 


pgzrun.go()
