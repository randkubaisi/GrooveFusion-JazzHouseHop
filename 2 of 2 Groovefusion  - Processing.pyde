scene = 0 
bus_x = -100  # Starting position of the bus
transition_time = 300  

def setup():
    size(800, 400)
    textAlign(CENTER, CENTER)
    textSize(20)

def draw():
    global scene, bus_x
    
    background(135, 206, 235)  # Light blue sky
    
    if frameCount < transition_time:
        scene = 0  # Scene 1: Bus driving past
    elif frameCount < transition_time * 2:
        scene = 1  # Scene 2: Human listening to music
    else:
        scene = 2  # Scene 3: Dancing animation background
    
    if scene == 0:
        draw_scene_1()
    elif scene == 1:
        draw_scene_2()
    elif scene == 2:
        draw_scene_3()

def draw_scene_1():
    global bus_x
    # Draw the road
    fill(50)  # Dark gray for road
    rect(0, 300, width, 100)
    
    # Dashed lane markings
    stroke(255)  # White lane markings
    strokeWeight(4)
    for i in range(0, width, 40):
        line(i, 350, i + 20, 350)
    
    # Draw the bus
    noStroke()
    fill(255, 215, 0)  # Yellow for bus
    rect(bus_x, 250, 100, 50)  # Main body
    rect(bus_x + 10, 230, 80, 30)  # Top part
    
    # Bus windows
    fill(0, 191, 255)  # Blue for windows
    rect(bus_x + 20, 240, 20, 20)
    rect(bus_x + 60, 240, 20, 20)
    
    # Bus wheels
    fill(0)  # Black for wheels
    ellipse(bus_x + 20, 300, 20, 20)
    ellipse(bus_x + 80, 300, 20, 20)
    
    # Update bus position
    bus_x += 2
    if bus_x > width:
        bus_x = -100  
    
    # Display text
    fill(255)
    text("Once upon a time, I was listening to GrooveFusion:JazzHouseHop", width / 2, 50)

def draw_scene_2():
    # Background for the music scene
    background(100, 100, 200)
    
    # Draw headphones 
    fill(0)
    ellipse(width / 2 - 40, height / 2, 60, 60)
    ellipse(width / 2 + 40, height / 2, 60, 60)
    
    # Draw headband
    stroke(0)
    strokeWeight(8)
    noFill()
    arc(width / 2, height / 2 - 30, 140, 80, PI, TWO_PI)
    
    # Display text
    fill(255)
    text("I love Working With data and code", width / 2, 50)
    text("Best Class ever!!", width / 2, 70)


def draw_scene_3():
    # Background for the dance scene
    background(0)
    
    # Moving circles for a "dancing" effect
    for i in range(10):
        fill(random(50, 255), random(50, 255), random(50, 255), 150)
        noStroke()
        ellipse(random(width), random(height), random(30, 70), random(30, 70))
    
    # Display text
    fill(255)
    text("Dance Party!", width / 2, 50)
