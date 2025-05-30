import pgzrun,random

WIDTH = 800
HEIGHT = 500
TITLE = "horizontal_shooting_game"

level_message_countdown = 90
level = 1
level_message = False
req = 10
numb_venoms = 3
rows = 1
game_state = "start"
score = 0
cap_lives = 3
venoms = []
shields = []
cap = Actor("captain_america")
cap.death = False
cap.pos = WIDTH - 50, HEIGHT / 2
# for i in range(3):
#    ven = Actor("venom")
#    ven.pos = 0,random.randint(40,HEIGHT - 40)
#    venoms.append(ven)

def draw():
    

    screen.blit("space_background",(0,0))
    if game_state == "start":
       screen.draw.text("press space to start \n kill enemies to win \n if you get hit 3 times you lose",(150,200))
    if game_state == "over":
       screen.draw.text("you didn't make it better luck next time",(150,200))
    if game_state == "play":
      if not cap.death:
       cap.draw()
   #   ven.draw()
      for i in shields:
         i.draw()
      for i in venoms:
         i.draw()
    if level_message:
       screen.draw.text("you are now entering level "+ str(level),(150,200))
   


def update():
   global cap_lives, score, game_state, numb_venoms, req, level, level_message, level_message_countdown
   # for i in range(3):
   #    ven = Actor("venom")
   #    ven.pos = 0,random.randint(40,HEIGHT - 40)
   #    venoms.append(ven)
   for i in venoms:
      i.x += 1
      if i.colliderect(cap):
           cap_lives -= 1
           venoms.remove(i)


      for b in shields:
           if b.colliderect(i):
              shields.remove(b)
              venoms.remove(i)
              score += 1
              
   if cap_lives == 0:
    cap.death = True
   if cap.death:
     game_state = "game_over"
   # print(cap_lives)
#    if len(venoms) == 0:
#      rows += 1
#      for i in range(rows):
#       for i in range(3):
#          ven = Actor("venom")
#          ven.pos = 0,random.randint(40,HEIGHT - 40)
#          venoms.append(ven)
   if len(venoms) > 0:
      for ven in venoms:
         if ven.x > WIDTH:
            ven.x = -20
      for i in shields:
         i.x -= 2
   if score == req:
      numb_venoms += 1
      req += 15
      level += 1
      level_message = True

   if level_message:
      level_message_countdown -= 1

   if level_message_countdown == 0:
      level_message = False
      level_message_countdown = 90

def on_key_down(key):
   global shields, game_state
   print(key)
   if game_state == "play":
    if key == keys.UP and cap.y > 40:
       cap.y -= 10
    if key == keys.DOWN:
        if cap.y < HEIGHT - 40:
         cap.y += 10
    if key == keys.SPACE:
       shield = Actor("cap_shield")
       shield.pos = cap.x - 40,cap.y
       shields.append(shield)
   if key == keys.SPACE and game_state == "start":
       game_state = "play"

def create_venom():
   print("c")
   if game_state == "play":
      for i in range(numb_venoms):
         ven = Actor("venom")
         ven.pos = 0,random.randint(40,HEIGHT - 40)
         venoms.append(ven)

clock.schedule_interval(create_venom,3)

pgzrun.go()