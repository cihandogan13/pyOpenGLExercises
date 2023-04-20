import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = 0
ortho_bottom = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Turtle Graphics')


currentPosition = (0, 0)
currentDirection = np.array([0,1,0])
#drawLength = 50

axiom = 'X'
rules = {
    "F":"FF",
    "X":"F+[-F-XF-X][+FF][+FF][--XF[+X]][++F-X]"
}
drawLength = 5
angle = 25
stack = [] 
ruleRunNumber = 5

points = []
x = 0
y = 0

def runRule(runCount):
    global instructions
    instructions = axiom 
    for loops in range(runCount):
        oldInstructions = instructions
        instructions = ""
        for index in range(0,len(oldInstructions)):
            if oldInstructions[index] in rules:
                instructions += rules[oldInstructions[index]]
            else: 
                instructions += oldInstructions[index]
    print("Rule")
    print(instructions)
                
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

def lineTo(x,y):
    global currentPosition
    glBegin(GL_LINE_STRIP)
    glVertex2f(currentPosition[0],currentPosition[1])
    glVertex2f(x,y)
    currentPosition = (x,y)
    glEnd()

# def moveTo(x,y):
#     global currentPosition
#     currentPosition = (x,y)
    
def moveTo(pos):
    global currentPosition
    currentPosition = (pos[0], pos[1])
 
def drawPoints():
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()   

def drawTurtle():
    global x, y
    #points.append((np.random.randint(-200,200),np.random.randint(-200,200)))
    points.append((x,y))
    r = np.random.rand()
    # if r < 0.1:
    #     x, y = 0.00 * x + 0.00 * y, 0.00 * x + 0.16 * y + 0.0
    # elif r < 0.86:
    #     x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    # elif r < 0.93:
    #     x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    # else:
    #     x, y = 0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
    
    if r < 0.33:
        x, y = 0.5 * x + 0.00 * y + 0.0, 0.00 * x + 0.5 * y + 0.5
    elif r < 0.66:
        x, y = 0.5 * x + 0.00 * y + 0.5, 0.00 * x + 0.5 * y + 0.00
    else:
        x, y = 0.5 * x + 0.00 * y + 0.0, 0.00 * x + 0.5 * y + 0.00
    
def resetTurtle():
    global currentPosition
    global direction
    currentPosition = (0,0)
    direction = np.array([0,1,0])
    
    
def forward(drawLength):
    newX = currentPosition[0] + direction[0] * drawLength
    newY = currentPosition[1] + direction[1] * drawLength
    lineTo(newX,newY)
    
def rotate(angle):
    global direction
    direction = zRotation(direction, math.radians(angle))    
    
    
init_ortho()
done = False
#glLineWidth(1)
glPointSize(1)
glColor3f(0, 1, 0)

# runRule(ruleRunNumber)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(-200,100,0)
    glScaled(550,550,1)
    
    
    resetTurtle()
    drawTurtle()
    drawPoints()
    
    pygame.display.flip()
    pygame.time.wait(1)
    
pygame.quit()

