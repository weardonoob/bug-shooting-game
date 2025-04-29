import pgzrun,random

WIDTH = 500
HEIGHT = 800
TITLE = "bug_shooting_game"

ship = Actor("galaga")
ship.pos = WIDTH / 2, HEIGHT -50

bullets = []
bugs = []
xp = 100
direction = -1
move = True

for i in range(4):
   bug = Actor("bug")
   bug.pos = xp,0
   bugs.append(bug)
   xp += 80


def draw():
    screen.blit("space_background",(0,0))
    ship.draw()
    for i in range(4):
       bugs[i].draw()
    for i in bullets:
       i.draw()
def update():
   global direction
   if (bugs[0].x < 0 and bugs[-1].x > WIDTH - 30) and len(bugs) > 0:
     direction = direction * (-1)
     for bug in bugs:
      bug.x += direction * 2
      bug.y += 1
      if bug.y > HEIGHT:
       bug.y = -20
   #if move:
   for i in bugs:
        i.y += 1
        i.x += direction * 2
   for i in bullets:
      i.y -= 2


def on_key_down(key):
    global bullets
    print(key)
    if key == keys.LEFT and ship.x > 40:
       ship.x -= 10
    if key == keys.RIGHT:
        if ship.x < WIDTH - 40:
         ship.x += 10
    if key == keys.SPACE:
       bullet = Actor("bullet")
       bullet.pos = ship.x,ship.y - 40
       bullets.append(bullet)

pgzrun.go()