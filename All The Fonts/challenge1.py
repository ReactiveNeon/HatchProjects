textAlign(CENTER, CENTER)
mono = createFont("monospace")
verdana = createFont("verdana")
georgia = createFont("georgia")
comic = createFont("comic sans ms")
arialBlack = createFont("arial black")
courierNew = createFont("courier new")

def drawText():
   fill(200, 0, 0)
   textFont(georgia, 30)
   text("Georgia", 200, 20)
   fill(0, 200, 0)
   textFont(mono, 30)
   text("MonoSpace", 200, 80)
   fill(0, 0, 200)
   textFont(verdana, 30)
   text("Verdana", 200, 150)
   fill(200, 200, 0)
   textFont(comic, 30)
   text("Comic Sans", 200, 230)
   fill(200, 0, 200)
   textFont(arialBlack, 30)
   text("Arial Black", 200, 300)
   fill(0, 200, 200)
   textFont(courierNew, 30)
   text("Courier New", 200, 370)
