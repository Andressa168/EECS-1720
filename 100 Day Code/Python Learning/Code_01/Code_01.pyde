add_library('sound')
value = 0
music = None
overButton = False

def setup():
    size(800, 650)
    smooth()
    
    global music
    
    music = SoundFile(this, "Remember_the_Time.mp3")

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
        ellipse(width/3, height/3 , 50, 50)
    
    if keyPressed == True:
        # heavy
        music.stop()
    else:
        pass
        
    if overButton:
        fill(255, 128, 0)
        rect(145, 85, 75, 75)
        ellipse(150, 85 , 50, 50)
        ellipse(210, 85 , 50, 50)
        
    else:
        noFill()
    
def mousePressed():
    global value
    if value == 0:
        value = 255
    else:
        value = 0
    
    if overButton:
        link("https://www.youtube.com/watch?v=LeiFF0gvqcc&ab_channel=michaeljacksonVEVO")

def mouseClicked():
    music.play(1, 1)

def mouseMoved():
    checkButtons()

def mouseDragged():
    checkButtons()

def checkButtons():
    global overButton
    
    overButton = 105 < mouseX < 180 and 60 < mouseY < 135;
