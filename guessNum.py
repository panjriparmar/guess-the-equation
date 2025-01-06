#Names: Panjri and Hafsa
#Date: Jan 19
#Title: Number Wordle
#Description: Wordle-like game that allows users to guess a computer generated equation with hints


from graphics import  *
from button import Button
import random

#Create a window with width = 500 and height = 500
win = GraphWin("Draw Point", 500, 500)
win.setCoords(0, 0, 500, 500)


#Add your code below this point

def welcome(): #Function prints title
    text = Text(Point(250,470), "Welcome to Number Wordle!") #Displays message
    text.setFace("courier") #Sets font
    text.setSize(15) #Sets size
    text.draw(win) #Outputs text

def instructions(): #Function displays intstructions for a given amount of time
    import time

    #Creates black rectangle
    box = Rectangle(Point(100,100),Point(400,300))
    box.setFill("black")

    #Creates instruction text
    intro = Text(Point(250,250), "Enter an 8 digit equation\nOnly use numbers 0 - 9\n and +, -, *, / or =") 
    intro.setTextColor("red")
    
    greenHint = Text(Point(250,200), "Values in the right spot turn green")
    greenHint.setTextColor("green")
    
    orangeHint = Text(Point(250,160), "Values in the equation\nbut in the wrong spot turn orange")
    orangeHint.setTextColor("orange")
    
    greyHint = Text(Point(250,120), "Values not in the equation turn grey")
    greyHint.setTextColor("grey")
    

    #Displays intructions for 5 seconds
    box.draw(win)
    intro.draw(win)
    greenHint.draw(win)
    orangeHint.draw(win)
    greyHint.draw(win)
    time.sleep(7)

    #Removes instruction
    intro.undraw()
    box.undraw()
    greenHint.undraw()
    orangeHint.undraw()
    greyHint.undraw()
    
  
   
def getEquation():  #Function allows user to input equation

    #Creates a box for user to input in
    inputBox = Entry(Point(250,420), 8)
    inputBox.setTextColor("white") #Sets text colour
    inputBox.setFace("courier") #Sets text font
    inputBox.setSize(14) #sets text size
    inputBox.draw(win) #Displays box
    
    return inputBox

def random_equation(): #Function creates 8 digit equation

    #Initialize variables
    operators= ['+', '-', '*', '/']
    valid=False
    randOper= ''
    result= 0
    
    while(not valid):
        randNum1= random.randint(1,99) #Generates random numbers
        randNum2= random.randint(1,99)
        randOper= operators[random.randint(0, 3)] #Chooses random operator
                
        if (randOper == '+'): #addition equation
            result= randNum1 + randNum2
            
        elif (randOper == '-'): #subtraction equation
            result= randNum1 - randNum2
            
        elif (randOper == '*' ): #multiplication equation
            result= randNum1 * randNum2
            
        elif (randOper == '/'  ): #Division equation
            
            while (randNum1 % randNum2 != 0): #Checks that there is no remainder
                randNum1= random.randint(1,99)
                randNum2= random.randint(1,99)
            result= randNum1 // randNum2
            
        if(result >= 0 ): #Ensures answer is not negative
            if(randNum1 >=10 and randNum2 >= 10 ):
                if(result < 100): #Ensures result is less than 100
                    valid=True
            else: 
                valid= True

        #Converts numbers to string and list      
        num1= str(randNum1) 
        num1= list(num1)
        num2= str(randNum2)
        num2= list(num2)

        finalResult= str(result)
        finalResult= list(finalResult)
       
        totalLength= len(num1) + len(num2) +len(finalResult) + 2 #Finds length of equation
        if(totalLength < 8):
            valid= False #Loops if equation length is not 8
    
    equation1= str(randNum1) + str(randOper) + str(randNum2) + "=" + str(result) #Puts equation together

    return equation1

def boxes(): #Function generates boxes
    
    for i in range(6): #Loop creates columns
        if i == 0: 
            y1 = 10
            y2 = 50

        else:
            y1 = y1 + 60
            y2 = y2 + 60

        for x in range(8): #loop creates rows
            if x == 0:
                x1 = 30
                x2 = 70
            
            else:
                x1 = x1 + 60
                x2 = x2 + 60
        
            rect = Rectangle(Point(x1, y1), Point(x2, y2)) #Draws boxes
            rect.draw(win)

def answerBoxes(equation, answer): #Function puts user input in boxes to display with correct colour

#Initalize variables
    i = 50
    equation= list(equation)
    answer=list(answer)



    for x in range(len(equation)): #Loop places input in correct coordinates
        num = Text(Point(i,(30 + ((tries - 1) * 60))), equation[x])
        
        if(equation[x] == answer[x]): #Makes number green if it is in correct spot
            answer[x]= ''

            num.setTextColor("green")
 
            
        elif(equation[x] in answer): #Makes number orange if it is in wrong spot
            #checking if the current number comes later on in the answer 
            if (equation.index(equation[x]) <  answer.index(equation[x])):
                indexInAns= answer.index(equation[x])
                # check if its at the right place later on
                if(equation[indexInAns] == answer[indexInAns]):
                    num.setTextColor("grey")

                else:
                    num.setTextColor("orange")
            else:
                num.setTextColor("orange")
                
        else:
            num.setTextColor("grey") #Makes number grey if it is not in equation

        num.draw(win) #Draws number
        num.setSize(15) #Changes size
        numList.append(num) #adds to list
        
        i = i + 60 #Loops to change coordinates
        

        
    
def lengthError(): #Function prints message if user entered equation that isn't 8 digits
    rangeError = Text(Point(390,420),"Enter 8 digit equation")#Text message
    rangeError.setTextColor("red") #Sets colour
    rangeError.draw(win) #Draws text
    
    return rangeError
    
def integerError(): #Function prints message is user didn't enter appropriate values
    numError = Text(Point(390,400),"Enter only digits, operators\n and =.") #Text message
    numError.setTextColor("red") #Sets colour
    numError.draw(win) #Draws text
    
    return numError

def mathError(): #Function prints message if user equation isn't valid
    validError = Text(Point(390,420),"Enter a valid equation!") #Text message
    validError.setSize(10) #Sets size
    validError.setTextColor("red") #Sets colour
    validError.draw(win) #Draws text
    
    return validError
                
def integerTest(equation): #Function tests if appropritae values are used

    #Intializes variables
    nonInt = 0
    values = "0123456789+-/*="
    
    for x in range(len(equation)): #Checks each value to see if it is valid
        if equation[x] not in values: #If value isn't valid it is an error
            nonInt += 1
        else:
            nonInt += 0
            
    return nonInt
    
def validTest(equation): #Function tests if equation is valid
        for c in equation:
            if (c in "+-*/"): #checks which operator is in equation
                indexOper= equation.index(c)
            if (c == "="):  #checks where '=' is
                indexEqual= equation.index(c)
        try:
            num1= int(equation[0:indexOper]) #Identifies numbera]s
            num2= int(equation[indexOper+1: indexEqual])
            result= int(equation[indexEqual+1: ]) #Identifies result

            #Initalizes result
            oper = equation[indexOper]
            correctResult = ''
            
            if(oper == "+"): #Checks if addition equation is valid
                correctResult= num1+num2
                
            elif(oper == "-"): #Checks if subtraction equation is valid
                correctResult= num1-num2
                
            elif(oper == "*"): #Checks if mutliplication equation is valid
                correctResult= num1*num2
                
            elif(oper == "/"): #Checks if division equation is valid
                correctResult= num1//num2
                
            else:
                return False
            return correctResult == result #Returns validity

        except:
            return False
        
    
def winner(): #Function prints message for winner
    congratsMessage = Text(Point(100,420), "Yay you win!!") #Text message
    congratsMessage.setSize(15) #Sets size
    congratsMessage.setTextColor("green") #Sets colour
    congratsMessage.setFace("courier") #Sets font
    congratsMessage.draw(win) #Draws text
    
    image = Image(Point(250, 200), "winner.png") #Imports image
    image.draw(win) #Prints message
    
    return congratsMessage, image
  
    
def fail():#Function prints messages for loser
    failMessage = Text(Point(100,420), "You Lose :(") #Text message
    failMessage.setSize(13) #Sets size
    failMessage.setTextColor("red") #Sets colours
    failMessage.setFace("courier") #Sets font
    failMessage.draw(win) #Draws text
    
    rightAnswer_ = Text(Point(100,390), ("The right answer was")) #Text message
    rightAnswer_.draw(win)#Draws text
    
    rightAnswer = Text(Point(100,370), answer)#Displays answer
    rightAnswer.draw(win)#Draws answer

    return failMessage, rightAnswer, rightAnswer_


def clearNums(numList): #Function clears numbers
    for num in numList: #Undraws each value
        num.undraw()

    

#Main Program



numList=[] # initialize an empty list

# initialize variables and call functions

gameOver= False
playAgain= True
instructions()
welcome()


enterButton = Button(win, Point(250,380), 75, 30, "Enter") # create enter button for user to enter equation
enterButton.activate() # activate enter button to allow user to replay when clicked

quitButton = Button(win, Point(50, 480), 50, 30, "Quit") #Creates quit button
quitProgram = False #Assigns false



replay = Button(win, Point(450, 470), 75, 30, "Replay") # create replay button
boxes()

while(playAgain == True): # loop when replay button is clicked
    quitButton.deactivate() #Deactivates quit button when playing
    replay.deactivate() # deactivate button while game is ongoing
    answer = random_equation()
    equation = 0
    tries = 0
    while equation != answer and tries < 6:
        rangeError= Text(Point(390,420),"") # prints error message when equation length entered is more or less than 8
        numError= Text(Point(390,420),"") # prints message when user enters string or disallowed value
        validError= Text(Point(390,420),"") # prints message when user equation is not valid (2+2=6)
        valid = False #loops until true
        tries += 1 # tries increases by 1 every time user is incorrect
        inputStr = getEquation()
        pt = win.getMouse()
        while not enterButton.clicked(pt):
            pt = win.getMouse()

        equation = inputStr.getText()

        while not valid:
            rangeError.undraw() # erases range error
            numError.undraw() # erases number error
            validError.undraw() # erases valid error
            if len(equation) != 8: #loops until equation length is valid
                rangeError= lengthError()
                inputStr = getEquation()
                pt = win.getMouse()
                while not enterButton.clicked(pt):
                    pt = win.getMouse() # user needs to click enter button to input an equation
                equation = inputStr.getText()
            else:
                rangeError.undraw() # erases errors
                numError.undraw()
                validError.undraw()  
                errors = integerTest(equation)
                if errors >=1:
                    valid = False # valid is false when the user's equation has at least 1 error
                    numError= integerError()
                    inputStr = getEquation()
                    pt = win.getMouse()
                    while not enterButton.clicked(pt): # loops until user clicks enter button
                        pt = win.getMouse() # user needs to click the enter button to input equation
                    equation = inputStr.getText()
                else:
                    rangeError.undraw() # erases errors
                    numError.undraw()
                    validError.undraw() 
                    isValid= validTest(equation)
                    if(not validTest(equation) ): # if equation is not valid
                        validError= mathError()
                        inputStr = getEquation()
                        pt = win.getMouse()
                        while not enterButton.clicked(pt): # loops until user clicks on the enter button
                            pt = win.getMouse()# user needs to click button to input equation
                        equation = inputStr.getText()
                    else:
                        valid= True # equation sets to true

       
        rangeError.undraw() #undraws errors
        numError.undraw()
        validError.undraw()   
                

    #Print numbers into boxes
        answerBoxes(equation, answer)


    msg=Text(Point(100,420), "")
    rightAnswer=Text(Point(100,420), "")
    rightAnswer_=Text(Point(100,420), "")

    image=Text(Point(100,420), "") # sets position of image
    
    if answer == equation: # when user wins
        msg, image= winner() # image is printed
        gameOver=True # user can now replay


    if tries > 5: # user loses
        msg, rightAnswer, rightAnswer_=  fail() # fail message, correct answer and printed
        gameOver=True # user can replay


    if(gameOver== True): # loops when the game ends
        
        replay.activate() # replay button is activated so user can click
        quitButton.activate() #quit button activated when game ends
        pt = win.getMouse()
        
   
        if replay.clicked(pt):
            
            playAgain= True #Program loops to play again
            msg.undraw() #Undraws past game
            image.undraw()
            rightAnswer.undraw()
            rightAnswer_.undraw()
            clearNums(numList)
            numList=[]
            
        elif quitButton.clicked(pt): #Closes window/ends game
            quitProgram = True
            win.close()
 













