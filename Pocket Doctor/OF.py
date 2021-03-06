# mode-demo.py

from tkinter import *
import random 
from tkinter import font
import PIL
from PIL import Image, ImageOps
from PIL import ImageTk
from PIL import *
import math
import numpy as np
import pickle 
import copy
import os

#################################################
# HELPER FUNCTIONS 
#################################################
# turns a list of meds into a list of strings
def display(resL):
    for med in resL:
        print(med.name)
        print("Drugs that will lead to Adverse Drug Interactions(ADI):\n")
        for name in med.contraMeds:
            print(name)
            # print(med.sideEffects + "\n")
        # print(med.cautions + "\n")
        print("\n")
        
def processLine(commandLine, infoList):
    processedLine = commandLine
    tokens = []
  
    commaLocator = processedLine.find(',')
    while commaLocator != -1:
        if processedLine[commaLocator-1] == ' ':
            processedLine = processedLine[:commaLocator-1] + processedLine[commaLocator:]   # if user uses a space before the comma

        newToken = processedLine[:commaLocator]     # things must be separated by commas
        tokens.append(newToken)
        processedLine = processedLine[commaLocator+1:]
        print(processedLine)

        while processedLine[0] == ' ':
            processedLine = processedLine[1:]       # in the case that the user uses spaces after commas
        
        commaLocator = processedLine.find(',')      # for the while loop condition
   
    if len(processedLine) > 0:
        while processedLine[0] == ' ':
            processedLine = processedLine[1:]       # in the case that the user uses spaces after commas
        newToken = processedLine     # for the case that the line is not empty after parsing
        tokens.append(newToken)
    
    return tokens

def mkTreatmentList(tokens, dictionary):
    treatmentList = []
    for token in tokens:
        condition = dictionary[token]
        treatment = condition.treatments
        treatmentList.append(treatment)
    return treatmentList

#################################################
# DATA STRUCTURE
#################################################

class Medication():

    def __init__(self, name, contraMeds, sideEffects):
        self.name = name
        # a list of med names that cause adverse drug reactions 
        self.contraMeds = contraMeds
        # a list of side effects 
        self.sideEffects = sideEffects

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, Medication)and(self.name == other.name))

class Condition():

    def __init__(self, name, treatments):
        self.name = name
        # a list of medications classes 
        self.treatments = treatments

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, Condition)and(self.name == other.name))

    def printer(self):
        print(2)

#################################################
# PRELOAD
#################################################
# This just ignores dictionary for now 

def loadConditions():
    # medications that pertain to the conditions
    abilify = Medication('abilify', ['fentora', 'morphine'], ['difficulty with speaking', 'uncontrolled movements'])
    cymbalta = Medication('cymbalta', ['zoloft', 'sustol', 'lithium', 'tamofen', 'prozac', 'fentora', 'ranexa'], ['cold sweats', 'weakness', 'blindness'])
    fentora = Medication('fentora', ['prozac', 'sustol', 'zoloft', 'morphine', 'abilify', 'cymbalta', 'haldol'], ['convulsions', 'light-headedness', 'nervousness'])
    sustol = Medication('sustol', ['lithium', 'zoloft', 'cymbalta', 'fentora', 'prozac', 'haldol'], ['blurred vision', 'fever', 'pounding in the ears'])
    zoloft = Medication('zoloft', ['lithium', 'cymbalta', 'fentora', 'sustol', 'tamofen', 'haldol'], ['diarrhea', 'sweating', 'inability to sit still'])
    ibuprofen = Medication('ibuprofen', ['lithium'], ['heartburn', 'shortness of breath'])
    tamofen = Medication('tamofen', ['ibuprofen', 'prozac', 'zoloft', 'ranexa', 'haldol'], ['anxiety', 'confusion', 'dizziness'])
    prozac = Medication('prozac', ['abilify', 'ibuprofen', 'lithium', 'tamofen', 'sustol'], ['suicidal thoughts and behaviors', 'seizures', 'abnormal bleeding'])
    lithium = Medication('lithium', ['ibuprofen', 'zoloft', 'sustol', 'prozac', 'cymbalta', 'haldol'], ['fainting', 'irregular heartbeat', 'troubled breathing'])
    morphine = Medication('morphine', ['abilify', 'fentora', 'haldol'], ['stomache pain', 'headache'])
    ranexa = Medication('ranexa', ['tamofen', 'cymbalta', 'haldol'], ['dizziness', 'constipation', 'nausea', 'sensation of spinning'])
    haldol = Medication('haldol', ['sustol', 'ranexa', 'zoloft', 'morphine', 'fentora', 'lithium', 'tamofen'], ['insomnia', 'agitation', 'difficulty speaking', 'troubled swallowing'])

    # initializing actual conditions
    depression = Condition('depression', [lithium, zoloft, prozac, cymbalta, haldol])
    pain = Condition('pain', [ibuprofen, morphine, ranexa, fentora])
    schizophrenia = Condition('schizophrenia', [lithium, haldol])
    cancer = Condition('cancer', [tamofen])
    OCD = Condition('OCD', [prozac, zoloft])
    anxietyDisorder = Condition('anxietyDisorder', [zoloft, cymbalta])

    L = [depression, pain, schizophrenia, cancer, OCD, anxietyDisorder]
    return L

def loadDictionary(data):
    # dictionary data.d contains all of the conditions 
    # contains all of the information on the conditions 
    data.d = dict()
    conditionsL = loadConditions()
    for condition in conditionsL:
        data.d[condition.name] = condition
def loadButtons(data):
    data.startButtonImg = Image.open("Desktop/start.gif")
    data.backButtonImg = Image.open("Desktop/back.gif")
    data.runButtonImg = Image.open("Desktop/run.gif")
    data.detailsButtonImg = Image.open("Desktop/details.gif")
def loadBackgrounds(data):
    data.mainBackgroundImg = Image.open("Desktop/mainbackground.gif")
    # https://www.vexels.com/png-svg/preview/144170/character-doctor-woman
    data.entryScreenBackground = Image.open("Desktop/entryScreen.gif")

    data.gameOverBackground = data.entryScreenBackground
    #https://www.gizmodo.com.au/2013/02/scientists-claim-to-have-built-a-computer-that-never-crashes/

#################################################
# BACKTRACKING SOLVE
#################################################
# @requires args is however many conditions: string 
# @ensures returns a 2d list containing the lists of medications required
def getMedications(*args):
    n = len(args)
    medicationsList = []
    for c in args:
        # condition is a string
        condition = d[c]
        medications = condition.treatments
        medicationsList.append(medications)
    return medicationsList 
def isSafe(m1, m2):
    contraMeds1 = m1.contraMeds
    contraMeds2 = m2.contraMeds
    for med in contraMeds1:
        if med == m2.name:
            return False
    for med in contraMeds2:
        if med == m1.name:
            return False
    return True

# @requires takes in a 2d list containing the lists of medications required  
# @ensures returns a list containing all the possible solutions to the conditions 
def getValidPrescriptions(medicationsList): 
    def isLegal(curMed, curSolution):
        # a position is legal if the med doesn't contradict with the previous
        for med in curSolution:
            if not(isSafe(med,curMed)):
                return False
        return True
    def solve(medicationsList,resL):
        # print(resL)
        # display(resL)

        if (medicationsList == []):
            return resL
        else:
            # try to place the med in solutions,
            # and then recursively solve the rest of the conditions
            # for i in range(len(medicationsList)):
            medsForCondition = medicationsList.pop(0)
            for j in range(len(medsForCondition)):
                curMed = medsForCondition[j]
                if isLegal(curMed,resL):
                    resL.append(curMed)  # place the med and hope it works
                    solution = solve(medicationsList,resL)
                    if (solution != None):
                        # ta da! it did work
                        return solution
                    resL.pop()
            medicationsList.insert(0,medsForCondition)
            # shoot, can't place the queen anywhere
            return None
    return solve(medicationsList,[])
#################################################
# Init
#################################################
def init(data):
    data.mode = "startMode"
    startModeInit(data)
    entryScreenModeInit(data)
    gameOverModeInit(data)

def startModeInit(data):
    #main screen button 
    loadButtons(data)
    loadBackgrounds(data)
    loadDictionary(data)
    data.mstartButtonPressed = False
    data.mbuttons = [selfDefinedButton(data.width//2,data.height*2//3,data.startButtonImg)]

def entryScreenModeInit(data):
    data.input = ""
    #initializes everything in entryScreen mode
    data.hbackButtonPressed = False
    data.hbuttons = [selfDefinedButton(data.width//2,data.height*5//12,data.backButtonImg), 
                     selfDefinedButton(data.width//2,data.height*7//12,data.runButtonImg), ]

def preloadImages(data):
    #This laods in all the images as PIL format
    pass


def gameOverModeInit(data):
    data.showDetails = False
    data.dbuttons = [selfDefinedButton(data.width//3,data.height*9//10,data.detailsButtonImg),
                     selfDefinedButton(data.width*2//3,data.height*9//10,data.backButtonImg)]
    data.terminalShow = False
#################################################
# MousePressed
#################################################
def mousePressed(event, data):
    if data.mode == "startMode":
        startModeMousePressed(event,data)
    elif data.mode == "entryScreenMode":
        entryScreenModeMousePressed(event,data)
    elif data.mode == "gameOverMode":
        gameOverModeMousePressed(event,data)
        

def startModeMousePressed(event,data):
    for button in data.mbuttons:
        button.redirect(event,data)
    

def entryScreenModeMousePressed(event,data):
    for button in data.hbuttons:
        button.redirect(event,data) 


def gameOverModeMousePressed(event,data):
    for button in data.dbuttons:
        button.redirect(event,data)


#################################################
# KeyPressed
#################################################

def keyPressed(event, data):
    if data.mode == "startMode":
        startModeKeyPressed(event,data)
    elif data.mode == "entryScreenMode":
        entryScreenModeKeyPressed(event,data)
    elif data.mode == "gameOverMode":
        gameOverModeKeyPressed(event,data)

def startModeKeyPressed(event,data):
    pass

def entryScreenModeKeyPressed(event,data):
    pass

def gameOverModeKeyPressed(event,data):
    pass

#################################################
# TimerFired
#################################################

def timerFired(data):
    if data.mode == "startMode":
        startModeTimerFired(data)
    elif data.mode == "entryScreenMode":
        entryScreenModeTimerFired(data)
    elif data.mode == "gameOverMode":
        gameOverModeTimerFired(data)

def startModeTimerFired(data):
    pass

def entryScreenModeTimerFired(data):
    pass

def gameOverModeTimerFired(data): 
    pass

#################################################
# Draw
#################################################

def redrawAll(canvas, data):
    if data.mode == "startMode":
        startModeDraw(canvas,data)
    elif data.mode == "entryScreenMode":
        entryScreenModeDraw(canvas,data)
    elif data.mode == "gameOverMode":
        gameOverModeDraw(canvas,data)
        

def startModeDraw(canvas,data):
    TkFormat = PIL.ImageTk.PhotoImage(data.mainBackgroundImg)
    data.newImg = TkFormat
    #this stores the new image so it doesn't get garbage collected 
    canvas.create_image(data.width/2, data.height/2,image=data.newImg)
    for button in data.mbuttons:
        button.draw(canvas,data)
    Arcade160 = font.Font(family='ArcadeClassic',
        size=160, weight='bold')
    canvas.create_text(data.width/2, data.height*4/7,anchor = S,text="Pocket\n"+"Doctor",font = Arcade160)

def entryScreenModeDraw(canvas,data):
    TkFormat = PIL.ImageTk.PhotoImage(data.entryScreenBackground)
    data.newImg = TkFormat
    #this stores the new image so it doesn't get garbage collected 
    canvas.create_image(data.width/2, data.height/2,image=data.newImg)
    Cambria50 = font.Font(family='Cambria',
        size=50, weight='bold')
    Cambria30 = font.Font(family='Cambria',
        size=30, weight='bold')
    canvas.create_text(data.width/2, data.height/7,text="List your conditions",font = Cambria50)
    canvas.create_text(data.width/2, data.height/5,text='using "," to denote a new condition',anchor = N, font = Cambria30)
    for button in data.hbuttons:
        button.draw(canvas,data) 

def gameOverModeDraw(canvas,data):

    # This is simply for testing purposes
    conditions = loadConditions()
    tokens = processLine(data.input, conditions)
    meds = mkTreatmentList(tokens, data.d)
    data.results = getValidPrescriptions(meds)
    if (data.terminalShow == False and (data.results != None) ) :
        display(data.results)
        data.terminalShow = True
    # 
   

    # TkFormat = PIL.ImageTk.PhotoImage(data.gameOverBackground)
    # data.newImg = TkFormat
    # #this stores the new image so it doesn't get garbage collected 
    # canvas.create_image(data.width/2, data.height/2,image=data.gameOverBackground)
    TkFormat = PIL.ImageTk.PhotoImage(data.gameOverBackground)
    data.newImg = TkFormat
    #this stores the new image so it doesn't get garbage collected 
    canvas.create_image(data.width/2, data.height/2,image=data.newImg)
    for button in data.dbuttons:
        button.draw(canvas,data)
    Arcade90 = font.Font(family='ArcadeClassic',
        size=90, weight='bold')
    text1 = "Results"
    canvas.create_text(data.width/2,data.height/4, anchor = S,text = text1,font = Arcade90)

    displayResult(canvas,data)

def displayResult(canvas,data):
    if (data.results!=None):
        scale = data.height//12
        bias = data.height/4 + scale/2
        for i in range (len(data.results)):
            med = data.results[i]
            header = med.name
            sideEffects = "Side effects: "+('   '.join(str(e) for e in med.sideEffects))+"\n"
            height1 = bias + scale*2*i 
            height2 = bias + scale*(2*i+1) 
            Cambria50 = font.Font(family='Cambria',
            size=50, weight='bold')
            Cambria20 = font.Font(family='Cambria',
            size=20, weight='bold')
            canvas.create_text(data.width/2,height1, anchor = N,text = header,font = Cambria50)
            if data.showDetails == True:
                canvas.create_text(data.width/2,height2, anchor = N,text = sideEffects,font = Cambria20)

class selfDefinedButton(object):
    def __init__(self,x,y,ImgFile):
        self.x = x
        self.y = y
        self.img = ImgFile
        self.width, self.height = self.img.size

    def draw(self,canvas,data):
        TkFormat = PIL.ImageTk.PhotoImage(self.img)
        self.newImg = TkFormat
        #this stores the new image so it doesn't get garbage collected 
        canvas.create_image(self.x, self.y, image=self.newImg)

    def redirect(self,event,data):
        if ((event.x < self.x + self.width/2 and event.x > self.x - self.width/2)
            and (event.y < self.y + self.height/2 and event.y > self.y - self.height/2)):
            self.isPressed = True
            if data.mode == "startMode" and self.img == data.startButtonImg:
            #play is pressed
                entryScreenModeInit(data)
                data.mode = "entryScreenMode"
            elif data.mode == "entryScreenMode" and self.img == data.backButtonImg:
            #back is pressed
                startModeInit(data) 
                data.mode = "startMode"
            elif data.mode == "entryScreenMode" and self.img == data.runButtonImg:
                #run is pressed
                openWindow(data)
                print("window is closed moved to the next line, input =",data.input)
                data.mode = "gameOverMode"
            elif data.mode == "gameOverMode" and self.img == data.backButtonImg:
                startModeInit(data)
                data.mode = "startMode"
            elif data.mode == "gameOverMode" and self.img == data.detailsButtonImg:
                data.showDetails = True
####################################
# use the run function as-is
####################################
def openWindow(data):
    root2 = Tk()
    Label(root2, text="Conditions").grid(row=0)

    e1 = Entry(root2)
    e1.grid(row=0, column=1)
# button = Button(root2, text='Get prescription', command=root2.quit).grid(row=3, column=0, sticky=W, pady=4)
    
    #lamda data: data.input = e1.get()
    def fn():
        data.input = e1.get()
        return
    Button(root2, text='get prescription',command=fn).grid(row=3, column=0, sticky=W, pady=4)
    Button(root2, text='quit',command=root2.quit).grid(row=3, column=1, sticky=W, pady=4)
    
    mainloop()

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

#################################################
# main
#################################################
def PocketDoctor():
    run(1000, 750)

PocketDoctor()