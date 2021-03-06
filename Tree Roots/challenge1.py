def drawLandscape():
   background(135, 206, 250)
   fill(151, 107, 83)
   rect(0, 300, 400, 100)
   fill(30, 137, 30)
   rect(0, 280, 400, 20)

def drawTree():
   fill(101, 67, 33)
   rect(180, 100, 40, 200)
   fill(30, 137, 30)
   ellipse(100, 100, 100, 100)
   ellipse(200, 100, 100, 100)
   ellipse(300, 100, 100, 100)
   ellipse(165, 55, 100, 100)
   ellipse(235, 55, 100, 100)
   ellipse(160, 120, 100, 100)
   ellipse(240, 120, 100, 100)
   fill(101, 67, 33)
   triangle(180, 300, 220, 300, 350, 350)
   triangle(180, 300, 220, 300, 75, 350)
   triangle(210, 305, 225, 310, 200, 350)

def drawSun():
   fill(200, 200, 0)
   ellipse(380, 10, 100, 100)

def drawRain():
   fill(0, 0, 255)
   for i in range (0, 50) :
       rect(random(0, 400), random(0, 240), 3, 20)

drawLandscape()
drawTree()
drawSun()
drawRain()
