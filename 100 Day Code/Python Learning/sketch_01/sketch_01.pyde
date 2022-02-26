value = 0

def setup():

    size(800, 600)


def draw():
    global value
    background(125)
    fill(value)
    ellipse(width/2, height/2 , 50, 50)
    
def mousePressed():
    global value
    if value == 0:
        value = 255
    else:
        value = 0
