def setup():
	size(400, 400)
textAlign(CENTER, CENTER)
mono = createFont("monospace");
verdana = createFont('verdana');
georgia = createFont('georgia');
comic = createFont('comic sans ms');
arial_black = createFont('arial black’)
courier_new = createFont('Courier New')
def draw_text():
  fill(0)
  textFont(georgia, 30)
  text("Georgia", 200, 20)
  textFont(mono, 30)
  text("MonoSpace", 200, 80)
  textFont(verdana, 30)
  text("Verdana", 200, 150)
  textFont(comic, 30)
  text("Comic Sans", 200, 230)
  textFont(arialblack, 30)
  text("Arial black", 200, 300)
  textFont(CourierNew, 30)
  text("Courier New", 200, 370)
drawText()
