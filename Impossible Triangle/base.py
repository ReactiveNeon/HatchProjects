def drawSide1():
    noStroke()
    background(168, 168, 168)
    fill(0, 0, 48)
    rect(44, 296, 292, 40)
    rotate(-30)
    rect(99, 231, 45, 215)
    rotate(30)
    triangle(268, 181, 242, 63, 197, 148)
    triangle(13, 296, 44, 335, 194, 148)
    triangle(360, 337, 204, 327, 340, 295)
drawSide1()

def drawSide2():
    fill(0, 0, 255)
    rect(37, 255, 223, 40)
    rotate(30.5)
    rect(163, -63, 44, 279)
    rotate(-30.5)
    triangle(225, 29, 173, 29, 150, 153)
    triangle(284, 296, 242, 296, 259, 256)
    triangle(74, 292, 81, 191, 13, 295)
drawSide2()

def drawSide3():
    fill(0, 0, 99)
    rotate(30)
    rect(208, -66, 40, 216)
    rotate(29.7)
    rect(158, -181, 292, 38)
    rotate(-59.7)
    triangle(208, 55, 244, 63, 225, 29)
    triangle(348, 315, 381, 297, 360, 336)
    triangle(91, 255, 142, 254, 225, 29)
drawSide3()

def drawOutline():
    strokeWeight(3)
    stroke(0, 0, 0)
    line(200, 150, 283, 295)
    line(260, 254, 92, 254)
    line(140, 254, 227, 104)
    line(360, 336, 227, 104)
    line(283, 295, 13, 295)
    line(359, 336, 44, 336)
    line(92, 254, 225, 28)
    line(384, 295, 225, 28)
    line(383, 295, 360, 337)
    line(44, 336, 13, 295)
    line(13, 295, 173, 28)
    line(173, 28, 225, 28)
drawOutline()