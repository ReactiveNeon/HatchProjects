def setup():
    size(400, 400)
    
def drawMiddle():
    fill(242, 221, 106)
    stroke(204, 112, 0)
    ellipse(274, 310, 80, 80)
    bezier(262, 326, 276, 305, 272, 281,234, 302)
    bezier(303, 320, 288, 300, 291, 283,306, 285)
drawMiddle()

def drawWings():
    fill(251, 255, 148)
    triangle(223, 282, 99, 219, 50, 62)
    triangle(302, 280, 254, 153, 283, 25)
    quad(52, 64, 37, 38, 248, 305, 245, 311)
    quad(284, 24, 278, 21, 299, 280, 304, 285)
    line(68, 121, 65, 79)
    line(87, 180, 77, 96)
    line(153, 245, 101, 128)
    line(280, 224, 286, 107)
    line(264, 180, 279, 46)
drawWings()