topPos = 240
bottomPos = 260

def drawLines(y) :
   line(100, y, 166, y - 30)
   line(166, y - 30, 232, y)
   line(232, y, 297, y - 30)

def drawEgg():
   background(0, 118, 165)
   stroke(255)
   strokeWeight(5)
   noFill()
   arc(200, topPos, 200, 280, 180, 345)
   drawLines(topPos)
   drawLines(bottomPos)
   arc(200, bottomPos, 200, 250, 346, 540)
   fill(255, 255, 255);
   textAlign(LEFT);
   textSize(15);
   text("def drawShirt() :", 100, 20)
   text("background(60, 40, 90)", 110, 40)
   text("image(hatchEgg, 300, 100)", 110, 60)
   text("text(messege, 300, 400)", 110, 80)
   text("Code at hatch", 270, 380)
drawEgg()
