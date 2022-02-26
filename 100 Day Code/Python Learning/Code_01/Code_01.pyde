value = 0

def setup():
    size(800, 650)
    smooth()

def draw():
    global value
    
    img = loadImage("a.png")
    img.resize(800, 650)
    background(img)
    img1 = loadImage("cream.png")
    img1.resize(60, 60)
    image(img1, mouseX - 30, mouseY - 30)

    fill(value)
    for i in range(100):
        ellipse(i, i , 50, 50)
    
def mousePressed():
    global value
    if value == 0:
        value = 255
    else:
        value = 0
