def setup():
	    size(400, 400)
angles1 = 0
angles2 = 0
angles3 = 0
num_clicks = 0
def draw_arcs() :
    noFill()
    stroke(0, 255, 255)
    strokeCap(SQUARE)
    strokeWeight(20)
    start1 = 110 + angles1
    var start2 = 110 + angles2
    var start3 = 110 + angles3
    var end1 = 430 + angles1
    var end2 = 430 + angles2
    var end3 = 430 + angles3
    arc(200, 200, 200, 200, start1, end1)
    arc(200, 200, 150, 150, start2, end2)
    arc(200, 200, 100, 100, start3, end3)

def spin_arcs():
    if numClicks < 3:
        angles3 += 3
    if numClicks < 2:
        angles2 += 2
    if numClicks < 1:
         angles1 += 1
def check_win():
    if numClicks > 2 :
        if abs(angles1%360 - angles2%360) < 30 and abs(angles2%360 - angles3%360) < 30:
            background (0, 255, 0)
        else:
            background (255, 0, 0)
            
def mouse_clicked() :
    num_clicks + 1
def draw() :
    background(0, 0, 0)
    spin_arcs()
    check_win()
    draw_arcs()
