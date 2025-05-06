import pgzrun,random

WIDTH = 500
HEIGHT = 800
TITLE = "bug_shooting_game"

ship = Actor("galaga")
ship.pos = WIDTH / 2, HEIGHT -50

game_state = "start"
ship.death = False
ship.countdown = 90
score = 0
bullets = []
bugs = []
xp = 100
direction = 1
move = True

for i in range(4):
   bug = Actor("bug")
   bug.pos = xp,0
   bugs.append(bug)
   xp += 80


def draw():
    screen.blit("space_background",(0,0))
    if game_state == "start":
       screen.draw.text("press space to start \n kill enemies to win \n if you get hit you will be revived",(150,200))
    if game_state == "over":
       screen.draw.text("yay you have killed all the enemies",(150,200))
    if game_state == "play":
      
      if not ship.death:
         ship.draw()
      for i in range(len(bugs)):
         bugs[i].draw()
      for i in bullets:
         i.draw()

def update():
   global direction, score, game_state
   print(ship.countdown)
   if (bugs[0].x < 30 or bugs[-1].x > WIDTH - 30) and len(bugs) > 0:
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
        if i.colliderect(ship):
           ship.death = True
        for b in bullets:
           if b.colliderect(i):
              bullets.remove(b)
              bugs.remove(i)
              score += 1
   
   for i in bullets:
      i.y -= 2
   if ship.death:
     ship.countdown -= 1
   if ship.countdown == 0:
       ship.death = False
       ship.countdown = 90
   if len(bugs) == 0:
      game_state = "over"

def on_key_down(key):
    global bullets, game_state
    print(key)
    if not ship.death and game_state == "play":
         
      if key == keys.LEFT and ship.x > 40:
         ship.x -= 10
      if key == keys.RIGHT:
         if ship.x < WIDTH - 40:
            ship.x += 10
      if key == keys.SPACE:
         bullet = Actor("bullet")
         bullet.pos = ship.x,ship.y - 40
         bullets.append(bullet)
    if key == keys.SPACE and game_state == "start":
       game_state = "play"

pgzrun.go()