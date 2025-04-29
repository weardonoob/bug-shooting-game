import pgzrun,random

WIDTH = 800
HEIGHT = 500
TITLE = "horizontal_shooting_game"

ship = Actor("captain_america")
ship.pos = WIDTH - 50, HEIGHT / 2
bug = Actor("venom")
bug.pos = 0,random.randint(40,HEIGHT - 40)

def draw():
    screen.blit("space_background",(0,0))
    ship.draw()
    bug.draw()
def update():
   bug.x += 1
   if bug.x > WIDTH:
      bug.x = -20


def on_key_down(key):
    print(key)
    if key == keys.UP and ship.y > 40:
       ship.y -= 10
    if key == keys.DOWN:
        if ship.y < HEIGHT - 40:
         ship.y += 10


pgzrun.go()