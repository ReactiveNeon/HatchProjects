def mouseClicked():
  fill(random(0, 255), random(0, 255), random(0, 255))
  ellipse(random(0, 400), random(0, 400), random(0, 100), random(0, 100))
  rect(random(0, 400), random(0, 400), random(0, 100), random(0, 100))
  strokeWeight(5)
  line(random(0, 400), random(0, 400), random(200, 400), random(300, 400))
  textSize(18)
  fill(random(0, 100), random(0, 100), random(0, 100))
  text('Click the page to see everything change!', 30, 380)
