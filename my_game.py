# SEV Beginner - Introduction to Game Development
import pgzrun
import random

WIDTH = 800 #width of the window
HEIGHT = 600 #height of the window

BACKGROUND_IMG = "mars_background"

player = Actor("spaceship_beg_up")
player.midbottom = (WIDTH/2, HEIGHT)

alien = Actor("alien_beg_sprite")
alien.pos = (random.randint(40,WIDTH-40), random.randint(100,HEIGHT-40))

score = 0
sounds.music_upbeat.play(-1)

def update():
    global score
    
    if(keyboard.up == 1 and player.top > 0):
        player.y += -5
        player.image = "spaceship_beg_up"
    elif(keyboard.down == 1 and player.bottom < HEIGHT):
        player.y += 5
        player.image = "spaceship_beg_down"
    elif(keyboard.left == 1 and player.left > 0):
        player.x += -5
        player.image = "spaceship_beg_left"
    elif(keyboard.right == 1 and player.right < WIDTH):
        player.x += 5
        player.image = "spaceship_beg_right"

    if(player.colliderect(alien) == 1):
        alien.pos = (random.randint(40,WIDTH-40), random.randint(100,HEIGHT-40))
        score += 1
        sounds.alien_device.play()

def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMG,(0,0))
    player.draw()
    alien.draw()

    show_score = str(score)
    screen.draw.text(show_score, fontsize=40, topright=(750,21), color="white")



pgzrun.go()


