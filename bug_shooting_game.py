import pgzrun,random

WIDTH = 500
HEIGHT = 800
TITLE = "bug_shooting_game"

ship = Actor("galaga")
ship.pos = WIDTH / 2, HEIGHT -50
bug = Actor("bug")
bug.pos = random.randint(40, WIDTH - 40),0

def draw():
    screen.blit("space_background",(0,0))
    ship.draw()
    bug.draw()
def update():
   bug.y += 1
   if bug.y > HEIGHT:
      bug.y = -20


def on_key_down(key):
    print(key)
    if key == keys.LEFT and ship.x > 40:
       ship.x -= 10
    if key == keys.RIGHT:
        if ship.x < WIDTH - 40:
         ship.x += 10


pgzrun.go()