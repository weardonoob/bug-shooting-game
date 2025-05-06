import pgzrun,random

WIDTH = 800
HEIGHT = 500
TITLE = "horizontal_shooting_game"

venoms = []
shields = []
cap = Actor("captain_america")
cap.pos = WIDTH - 50, HEIGHT / 2
for i in range(3):
   ven = Actor("venom")
   ven.pos = 0,random.randint(40,HEIGHT - 40)
   venoms.append(ven)

def draw():
    screen.blit("space_background",(0,0))
    cap.draw()
 #   ven.draw()
    for i in shields:
       i.draw()
    for i in venoms:
       i.draw()
def update():
   for i in venoms:
      i.x += 1

   if ven.x > WIDTH:
      ven.x = -20
   for i in shields:
      i.x -= 2


def on_key_down(key):
    global shields
    print(key)
    if key == keys.UP and cap.y > 40:
       cap.y -= 10
    if key == keys.DOWN:
        if cap.y < HEIGHT - 40:
         cap.y += 10
    if key == keys.SPACE:
       shield = Actor("cap_shield")
       shield.pos = cap.x - 40,cap.y
       shields.append(shield)

pgzrun.go()