def setup():
	size(400, 400)
brickW = 24
brickH = 11
def drawSetup() :
    background(199, 253, 255)
    fill(252, 133, 133)

drawSetup()

def drawBricks() :
    for i in range (0, 15) :
     for j in range (0, 10) :
     rect(10 + i * 25, 26 + 11 * j, brickW, brickH)

drawBricks()
