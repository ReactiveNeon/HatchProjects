def setup():
    size(400, 400)
    
    background(0)

outerLength = 140
innerLength = 100
outerAngle = 0
innerAngle = 0
outerSpeed = 0.07
innerSpeed = 0.05

def drawLine():
    global outerLength, innerLength
    global outerAngle, innerAngle
    global outerSpeed, innerSpeed

    stroke(outerAngle, innerAngle, outerAngle)
    strokeWeight(0.3)
    point1x = 200 + innerLength * cos(innerAngle)
    point1y = 200 + innerLength * sin(-innerAngle)
    point2x = 200 + outerLength * cos(outerAngle)
    point2y = 200 - outerLength * sin(outerAngle)
    line(point1x, point1y, point2x, point2y)
    outerAngle += outerSpeed
    innerAngle += innerSpeed

def draw():
    drawLine()