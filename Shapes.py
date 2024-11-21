import pgzrun
import random
WIDTH = 600
HEIGHT = 600

def draw():
    screen.fill("Black")
    """

    r1 = Rect ((300,300),(300,200))
    r1.center = 300,300
    screen.draw.rect(r1,"Blue")
    r2 = Rect ((300,300),(280,220))
    r2.center = 300,300
    screen.draw.rect(r2,"Green")
    r3 = Rect((300,300),(260,240))
    r3.center = 300,300
    screen.draw.rect(r3,"Red"),
    """
    w=400
    h=150
    for i in range(20):
        r= random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)


        r1=Rect((300,300),(w,h))
        r1.center = 300,300 
        screen.draw.rect(r1,(r,g,b))
        w -=20
        h +=20

    
def update():
    pass 
pgzrun.go()
