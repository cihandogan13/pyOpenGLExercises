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
    
    
def resetTurtle():
    global currentPosition
    global direction
    currentPosition = (0,0)
    direction = np.array([0,1,0])
    
def drawTurtle():
    global direction
    for index in range(0, len(instructions)):
        if instructions[index] == 'F':
            forward(drawLength)
        elif instructions[index] == '+':
            rotate(angle)
        elif instructions[index] == '-':
            rotate(-angle)
        elif instructions[index] == '[':
            stack.append((currentPosition,currentDirection))
        elif instructions[index] == ']':
            currentVector = stack.pop()
            moveTo(currentVector[0])
            direction = currentVector[1]
    
def forward(drawLength):
    newX = currentPosition[0] + direction[0] * drawLength
    newY = currentPosition[1] + direction[1] * drawLength
    lineTo(newX,newY)
    
def rotate(angle):
    global direction
    direction = zRotation(direction, math.radians(angle))    
    
    
init_ortho()
done = False
glLineWidth(1)
runRule(ruleRunNumber)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # glBegin(GL_POINTS)
    # glVertex2f(0, 0)
    # glEnd()
    
    resetTurtle()
    drawTurtle()
    
    pygame.display.flip()
pygame.quit()

