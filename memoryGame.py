from graphics import *
import random
import time 

# This function contains the grid of the game
def gameGrid(memoryGame, win):
    vline1 = Line(Point(1,0), Point(1,3))
    vline1.draw(win)
    memoryGame.append(vline1)
    
    vline2 = Line(Point(2,0), Point(2,3))
    vline2.draw(win)
    memoryGame.append(vline2)
    
    hline1 = Line(Point(0,1), Point(3,1))
    hline1.draw(win)
    memoryGame.append(hline1)
        
    hline2 = Line(Point(0,2), Point(3,2))
    hline2.draw(win)
    memoryGame.append(hline2)

# This function generates a square with random points
def randomSquare(win, x1, y1, x2, y2):
    square = Rectangle(Point(x1, y1), Point(x2, y2))           
    square.setFill("black")
    square.draw(win)
    time.sleep(1)
    square.undraw()
    time.sleep(.5)

# This function verifies if he clicked the correct square
def clickDetector(click, x1, y1, x2, y2, win, memoryGame):
    square = Rectangle(Point(x1, y1), Point(x2, y2)) 
    
    # If he clicks the rigth square it will turn white 
    if(click.getX() > x1 and click.getX() < x2 and click.getY() > y1 and click.getY() < y2):
        square.setFill("yellow")
        square.draw(win)
        time.sleep(1)
        square.undraw()
        return 1
    
    # If he clicks the wrong square it will turn red, the grid will be deleted,
    # you would have lost and you will be asked if you want to play again or not
    else:      
        square.setFill("red")
        square.draw(win)
        time.sleep(1)
        square.undraw()
        
        for mG in memoryGame:
            mG.undraw()
            
        win.setBackground("red")
        gameOver = Text(Point(300, 300), "You Lost!")
        gameOver.setSize(36)
        gameOver.draw(win)
        playAgainOrGameOver(win)
        return 0

# This function creates the winning trophy and the message that you won
def winningTrophy(win):
    win.setCoords(0, 600, 600, 0)
    
    stick = Rectangle(Point(290, 340), Point(310, 260))
    stick.setWidth(3)
    stick.setFill(color_rgb(255,231,129))
    stick.draw(win)

    cup = Oval(Point(220, 280), Point(380, 60))
    cup.setWidth(3)
    cup.setFill(color_rgb(255,231,129))
    cup.draw(win)
        
    cupCover = Rectangle(Point(0, 60), Point(600, 170))
    cupCover.setWidth(3)
    cupCover.setFill("white")
    cupCover.setOutline("white")
    cupCover.draw(win)
        
    cupTop = Rectangle(Point(220, 170), Point(380, 173))
    cupTop.setFill("black")
    cupTop.setOutline("black")
    cupTop.draw(win)
        
    circ = Circle(Point(300, 320), 25)
    circ.setWidth(3)
    circ.setFill(color_rgb(255,231,129))
    circ.draw(win)

    base1 = Rectangle(Point(250,320), Point(350,370))
    base1.setWidth(3)
    base1.setFill(color_rgb(165,82,7))
    base1.draw(win)
        
    base2 = Rectangle(Point(220,360), Point(380,380))
    base2.setWidth(3)
    base2.setFill(color_rgb(214,215,216))
    base2.draw(win)
        
    title = Text(Point(300, 450),"You Won!")
    title.setStyle("bold")
    title.setSize(36)
    title.draw(win)

# This function will create the buttons to play again or game over
def playAgainOrGameOver(win):
    win.setCoords(0, 600, 600, 0)
    
    playAgain = Rectangle(Point(475, 555), Point(585, 585))
    playAgain.setWidth(3)
    playAgain.draw(win)
    
    playAgainLabel = Text(Point(530, 570), "PLAY AGAIN")
    playAgainLabel.setStyle("bold")
    playAgainLabel.draw(win)

    # Quit game button
    quitGame = Rectangle(Point(15, 555), Point(65, 585))
    quitGame.setWidth(3)
    quitGame.draw(win)
    
    quitGameLabel = Text(Point(40, 570), "QUIT")
    quitGameLabel.setStyle("bold")
    quitGameLabel.draw(win)

    # If the player choses to play again the page will close and another 
    # game will start and if he chooses to quit the window will close
    mLoc = win.getMouse()
    if mLoc.getX() >= 475 and mLoc.getX() <= 585 and mLoc.getY() >= 555 and mLoc.getY() <= 585:
        win.close()
        main()

    if mLoc.getX() >= 15 and mLoc.getX() <= 65 and mLoc.getY() >= 555 and mLoc.getY() <= 585:
        win.close()

def main():
    memoryGame = []
    
    # Create the graphics window and set the coordinates and background
    win = GraphWin("Memory Game",600,600)
    win.setCoords(0,3,3,0)
    win.setBackground("white")
    
    # Create the game grid
    gameGrid(memoryGame, win)
    
    # Create a for loop that contains the core of the game 
    for i in range(5):
        # Create a counter variable for the rounds won 
        counter = 0
        
        # Crate variables that select random squares
        x1 = random.randrange(1,3)
        x2 = x1 - 1
        y1 = x2
        y2 = x1  
        
        x3 = random.randrange(0,2)
        x4 = x3 + 1
        y3 = x4
        y4 = y3 + 1
        
        x5 = 3
        x6 = 2
        y5 = random.randrange(1,3)
        y6 = y5 - 1
        
        x7 = random.randrange(2,3)
        x8 = x7 - 1
        y7 = x8
        y8 = x7 
        
        x9 = random.randrange(0,2)
        x10 = x9 + 1
        y9 = x10
        y10 = y9 + 1
        
        # Create the random squares
        if i >= 0:
            randomSquare(win, x2, y1, x1, y2)
            
            if i >= 1:
                randomSquare(win, x3, y3, x4, y4)
                
                if i >= 2:
                    randomSquare(win, x6, y6, x5, y5) 
                    
                    if i >= 3:
                        randomSquare(win, x8, y7, x7, y8)
                        
                        if i == 4:
                            randomSquare(win, x9, y9, x10, y10)       
        
        # Verify that the player clicked the correct square in each round
        # if he did add 1 to the counter
        # if he didn't he will loose the game
        if i >= 0:
            click1 = win.getMouse()
            if (clickDetector(click1, x2, y1, x1, y2, win, memoryGame) == 1):
                counter = counter + 1  
            clickDetector(click1, x2, y1, x1, y2, win, memoryGame)      
   
            if i >= 1:
                click2 = win.getMouse()
                if (clickDetector(click2, x3, y3, x4, y4, win, memoryGame) == 1):
                    counter = counter + 1
                clickDetector(click2, x3, y3, x4, y4, win, memoryGame) 
                    
                if i >= 2:
                    click3 = win.getMouse() 
                    if (clickDetector(click3, x6, y6, x5, y5, win, memoryGame) == 1):
                        counter = counter + 1
                    clickDetector(click3, x6, y6, x5, y5, win, memoryGame) 
                        
                    if i >= 3:
                        click4 = win.getMouse() 
                        if (clickDetector(click4, x8, y7, x7, y8, win, memoryGame) == 1):
                            counter = counter + 1
                        clickDetector(click4, x8, y7, x7, y8, win, memoryGame) 
                            
                        if i == 4:
                            click5 = win.getMouse() 
                            if (clickDetector(click5, x9, y9, x10, y10, win, memoryGame) == 1):
                                counter = counter + 1
                            clickDetector(click5, x9, y9, x10, y10, win, memoryGame) 
        
        # If he won all the rounds, it means he won the game 
        # everything will be undraw from the screen, a winning trophy will appear
        # and he will have the option to play again or end the game
        if (counter == 5):
            for mG in memoryGame:
                mG.undraw()
            winningTrophy(win)
            playAgainOrGameOver(win)
                 
main()
