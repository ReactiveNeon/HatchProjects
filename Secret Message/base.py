def setup ():
    size(400, 400)
    
    background(0)
    noStroke()
    
def draw ():
    fill(0)
    textSize(20)
    text("SECRET MESSAGE", 100, 200)
    
    if mousePressed:
        fill(255, 255, 255, 10)
        ellipse(mouseX, mouseY, 20, 20)
    