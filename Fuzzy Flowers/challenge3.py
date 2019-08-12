def drawFlowers():
   stroke(random(150, 255), random(150, 255), random(150, 255), 30)
   strokeWeight(random(15))
   translate(random(0, 400), random(0, 400))
   for i in range (0, 60) :
       rotate(7)
       line(0, 0, random(10, 25), random(10, 25))

def draw():
   frameRate(100)
   drawFlowers()
   resetMatrix()
   fill(0, 0, 0, 10)
   rect(0, 0, 400, 400)
