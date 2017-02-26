
def draw():
    background(204)

    numPoints = int(map(mouseX, 0, width, 6, 60))
    angle = 0
    angleStep = 180.0 / numPoints

    beginShape(TRIANGLE_STRIP)
    for i in range(numPoints):
        px = x + cos(radians(angle)) * outsideRadius
        py = y + sin(radians(angle)) * outsideRadius
        angle += angleStep
        vertex(px, py)
        px = x + cos(radians(angle)) * insideRadius
        py = y + sin(radians(angle)) * insideRadius
        vertex(px, py)
        angle += angleStep
    endShape()