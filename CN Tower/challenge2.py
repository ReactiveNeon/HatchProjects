def drawTower():
   fill(random(0, 255), random(0, 255), random(0, 255))
   triangle(190, 400, 215, 400, 200, 50)
   ellipse(200, 180, 40, 10)
   ellipse(200, 185, 35, 10)
   ellipse(200, 175, 40, 10)
   ellipse(200, 170, 35, 10)
   ellipse(200.5, 140, 10, 7)  
   ellipse(100, 410, 200, 100)
   rect(250, 220, 60, 180)

drawTower()

def drawSign() :
   fill(255, 0, 0)
   textSize(30)
   text("T", 100, 35)
   text("N", 220, 35)
   fill(0, 0, 255)
   text("O", 130, 35)
   text("T", 250, 35)
   fill(0, 255, 0)
   text("R", 160, 35)
   text("O", 280, 35)
   fill(255, 255, 0)
   text("O", 190, 35)
def draw():
    background(255)
    drawTower()
    drawSign()
