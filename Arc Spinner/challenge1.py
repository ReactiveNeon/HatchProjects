angles1 = 0
angles2 = 0
angles3 = 0
angles4 = 0
numClicks = 0

def drawArcs():
   noFill()
   stroke(0, 255, 255)
   strokeCap(SQUARE)
   strokeWeight(20)
   start1 = 110 + angles1
   start2 = 110 + angles2
   start3 = 110 + angles3
   start4 = 110 + angles4
   end1 = 430 + angles1
   end2 = 430 + angles2
   end3 = 430 + angles3
   end4 = 430 + angles4
   arc(200, 200, 250, 250, start1, end1)
   arc(200, 200, 200, 200, start2, end2)
   arc(200, 200, 150, 150, start3, end3)
   arc(200, 200, 100, 100, start4, end4)

def spinArcs () :
   global angles4
   global angles3
   global angles2
   global angles1
   if numClicks < 4 :
       angles4 += 4
   
   if numClicks < 3 :
       angles3 += 3
   
   if numClicks < 2 :
       angles2 += 2
   
   if numClicks < 1 :
        angles1 += 1
   

def checkWin() :
   if numClicks > 3 :
       if abs(angles1 % 360 - angles2 % 360) < 30 and abs(angles2 % 360 - angles3 % 360) < 30 and abs(angles3 % 360 - angles4 % 360) < 30 :
           background (0, 255, 0)
       else :
           background (255, 0, 0)
      
  

def mouseClicked(e) :
   global numClicks
   numClicks +=1

def draw():
   background(0, 0, 0)
   spinArcs()
   checkWin()
   drawArcs()
