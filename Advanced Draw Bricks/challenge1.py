brickW = 28
brickH = 15
index = 0
brickArray = {
   "xPos": [],
   "yPos": [],
   "On": [],
}

def setupBricks():
   global brickW, brickH, index
   for i in range (0, 13) :
       for j in range (0, 10) :
           if round(random (0, 3)) == 1 :
               brickArray["On"[index]] = False
           else :
               brickArray["On"[index]] = True
               brickArray["xPos"[index]] = 10 + i * 29
               brickArray["yPos"[index]] = 31 + 15 * j
           index +=1
setupBricks()

def drawBricks():
   global brickW, brickH, index
   background(120, 251, 255)
   fill(250, 87, 87)
   for k in range (0, index) :
       if brickArray["On[k]"] == true :
           rect(brickArray["xPos"[k]], brickArray["yPos"[k]], brickW, brickH)
drawBricks()