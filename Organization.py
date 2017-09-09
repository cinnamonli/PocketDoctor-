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
# Init
#################################################
def init(data):
    data.input = ""
    data.mode = "startMode"
    startModeInit(data)
    entryScreenModeInit(data)
    gameOverModeInit(data)

def loadButtons(data):
    data.startButtonImg = Image.open("Desktop/start.gif")
    data.backButtonImg = Image.open("Desktop/back.gif")
    data.runButtonImg = Image.open("Desktop/run.gif")
    data.detailsButtonImg = Image.open("Desktop/details.gif")

def loadBackgrounds(data):
    data.mainBackgroundImg = Image.open("Desktop/mainbackground.gif")
    # adapted from https://www.iconfinder.com/icons/310934/compose_draw_graph_line_pencil_write_icon
    data.entryScreenBackground = Image.open("Desktop/entryScreen.gif")

    data.gameOverBackground = data.entryScreenBackground
    #https://www.gizmodo.com.au/2013/02/scientists-claim-to-have-built-a-computer-that-never-crashes/

def startModeInit(data):
    #main screen button 
    loadButtons(data)
    loadBackgrounds(data)
    data.mstartButtonPressed = False
    data.mbuttons = [selfDefinedButton(data.width//2,data.height*2//3,data.startButtonImg)]

def entryScreenModeInit(data):
    #initializes everything in entryScreen mode
    data.hbackButtonPressed = False
    data.hbuttons = [selfDefinedButton(data.width//2,data.height*5//12,data.backButtonImg), 
                     selfDefinedButton(data.width//2,data.height*7//12,data.runButtonImg), ]

def preloadImages(data):
    #This laods in all the images as PIL format
    pass


def gameOverModeInit(data):
    data.dbuttons = [selfDefinedButton(data.width//2,data.height*9//10,data.detailsButtonImg)]



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
        size=120, weight='bold')
    canvas.create_text(data.width/2, data.height/3,anchor = N,text="PocketDoctor",font = Arcade160)

def entryScreenModeDraw(canvas,data):
    TkFormat = PIL.ImageTk.PhotoImage(data.entryScreenBackground)
    data.newImg = TkFormat
    #this stores the new image so it doesn't get garbage collected 
    canvas.create_image(data.width/2, data.height/2,image=data.newImg)
    Arcade90 = font.Font(family='ArcadeClassic',
        size=80, weight='bold')
    canvas.create_text(data.width/2, data.height/9,text="Enter your information",font = Arcade90)
    for button in data.hbuttons:
        button.draw(canvas,data) 

def gameOverModeDraw(canvas,data):
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
    Arcade60 = font.Font(family='ArcadeClassic',
        size=60, weight='bold')
    text1 = "Results"
    text2 = data.input
    canvas.create_text(data.width/2,data.height/4, anchor = S,text = text1,font = Arcade90)
    canvas.create_text(data.width/2,data.height/4, anchor = N,text = text2,font = Arcade90)

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
                print("window is closed moved to the next line, input = ",data.input)
                data.mode = "gameOverMode"
            elif data.mode == "gameOverMode" and self.img == data.backButtonImg:
                startModeInit(data)
                data.mode = "startMode"
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
        print("trying to save data: %s" % e1.get())
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
