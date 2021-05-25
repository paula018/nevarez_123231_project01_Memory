from graphics import *
import random
import time 

# This class contains the grid of the game
class Grid:
    def __init__(self, memoryGameGrid, x1, y1, x2, y2, win):
        self.memoryGameGrid = memoryGameGrid 
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win
        
        self.line = Line(Point(self.x1, self.y1), Point(self.x2, self.y2))  
        self.line.draw(self.win)
        self.memoryGameGrid.append(self.line)

# This class generates a square with random points        
class RandomSquare:
    def __init__(self, x1, y1, x2, y2, color, time, win):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.win = win
        self.time = time
        
        self.square = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))  
        self.square.setFill(self.color)
        self.square.draw(self.win)
        
        self.time.sleep(1)
        self.square.undraw()
        self.time.sleep(.5)
        
# This class creates texts for the instructions 
class TextInstructions:
    def __init__(self, memoryGameInstructions, x1, y1, message, size, style, win):
        self.memoryGameInstructions = memoryGameInstructions 
        self.x1 = x1
        self.y1 = y1
        self.message = message
        self.size = size
        self.style = style
        self.win = win
        
        self.txt = Text(Point(self.x1, self.y1), self.message)  
        self.txt.setSize(self.size)
        self.txt.setStyle(self.style)
        self.txt.draw(self.win)
        self.memoryGameInstructions.append(self.txt)
        
    
# This class generates figures       
class Figures:
    def __init__(self, p1, p2, figure, fill, outline, width, win):
        self.p1 = p1
        self.p2 = p2
        self.figure = figure
        self.fill = fill
        self.outline = outline
        self.width = width
        self.win = win
        
        self.fig = figure(p1, p2)  
        self.fig.setFill(self.fill)
        self.fig.setOutline(self.outline)
        self.fig.setWidth(self.width)
        self.fig.draw(self.win)

# This class generates texts 
class Texts:
    def __init__(self, x1, y1, message, size, style, win):
        self.x1 = x1
        self.y1 = y1
        self.message = message
        self.size = size
        self.style = style
        self.win = win
        
        self.txt = Text(Point(self.x1, self.y1), self.message)  
        self.txt.setSize(self.size)
        self.txt.setStyle(self.style)
        self.txt.draw(self.win)
        

# This function contains the instructions of the game
def gameInstructions(memoryGameInstructions, win):
    
    TextInstructions(memoryGameInstructions, 1.5, 0.5, "MEMORY GAME", 36, "bold", win)
    TextInstructions(memoryGameInstructions, 1.5, 1, "Memorize the order in which the squares ligth up.", 16, "bold", win)
    TextInstructions(memoryGameInstructions, 1.5, 1.2, "Then, click them in the correct order. If you ", 16, "bold", win)
    TextInstructions(memoryGameInstructions, 1.5, 1.4, "select them in the rigth order in all 5 rounds you ", 16, "bold", win)
    TextInstructions(memoryGameInstructions, 1.5, 1.6, "you win.", 16, "bold", win)
    TextInstructions(memoryGameInstructions, 1.5, 2.1, "LET'S START!", 16, "bold", win)
    
    start = Rectangle(Point(1.1, 2), Point(1.9, 2.2))
    start.setWidth(3)
    start.draw(win)
    memoryGameInstructions.append(start)
    
# This function verifies if he clicked the correct square
def clickDetector(click, x1, y1, x2, y2, win, memoryGameGrid):
    square = Rectangle(Point(x1, y1), Point(x2, y2)) 
    
    # If he clicks the rigth square it will turn white 
    if(click.getX() > x1 and click.getX() < x2 and click.getY() > y1 and click.getY() < y2):
        square.setFill("yellow")
        square.draw(win)
        time.sleep(0.5)
        square.undraw()
        return 1
    
    # If he clicks the wrong square it will turn red, the grid will be deleted,
    # you would have lost and you will be asked if you want to play again or not
    else:      
        square.setFill("red")
        square.draw(win)
        time.sleep(1)
        square.undraw()
        
        for mG in memoryGameGrid:
            mG.undraw()
            
        win.setBackground("red")
        Texts(300, 300, "You Lost!", 36, "normal", win)
        playAgainOrGameOver(win)
        return 0

# This function creates the winning trophy and the message that you won
def winningTrophy(win):
    win.setCoords(0, 600, 600, 0)
    
    Figures(Point(290, 340), Point(310, 260), Rectangle, color_rgb(255,231,129), "black", 3, win)
    Figures(Point(220, 280), Point(380, 60), Oval, color_rgb(255,231,129), "black", 3, win)
    Figures(Point(0, 60), Point(600, 170), Rectangle, "white", "white", 3, win)
    Figures(Point(220, 170), Point(380, 173), Rectangle, "black", "black", 1, win)
    Figures(Point(300, 320), 25, Circle, color_rgb(255,231,129), "black", 3, win)
    Figures(Point(250,320), Point(350,370), Rectangle, color_rgb(165,82,7), "black", 3, win)
    Figures(Point(220,360), Point(380,380), Rectangle, color_rgb(214,215,216), "black", 3, win)
    Texts(300, 450, "You Won!", 36, "bold", win)

# This function will create the buttons to play again or game over
def playAgainOrGameOver(win):
    win.setCoords(0, 600, 600, 0)
    
    # Play Again game button
    playAgain = Rectangle(Point(475, 555), Point(585, 585))
    playAgain.setWidth(3)
    playAgain.draw(win)
    
    Texts(530, 570, "PLAY AGAIN", 12, "bold", win)

    # Quit game button
    quitGame = Rectangle(Point(15, 555), Point(65, 585))
    quitGame.setWidth(3)
    quitGame.draw(win)
    
    Texts(40, 570, "QUIT", 12, "bold", win)

    # If the player choses to play again the page will close and another 
    # game will start and if he chooses to quit the window will close
    mLoc = win.getMouse()
    if mLoc.getX() >= 475 and mLoc.getX() <= 585 and mLoc.getY() >= 555 and mLoc.getY() <= 585:
        win.close()
        main()

    if mLoc.getX() >= 15 and mLoc.getX() <= 65 and mLoc.getY() >= 555 and mLoc.getY() <= 585:
        win.close()

def main():
    memoryGameGrid = []
    memoryGameInstructions = []
    
    # Create the graphics window and set the coordinates and background
    win = GraphWin("Memory Game",600,600)
    win.setCoords(0,3,3,0)
    win.setBackground("white")
    
    # Create the game grid when hitted start
    gameInstructions(memoryGameInstructions, win)
    click = win.getMouse()
    if(click.getX() > 1.1 and click.getX() < 1.9 and click.getY() > 2 and click.getY() < 2.2):
        for mG in memoryGameInstructions:
            mG.undraw()
        Grid(memoryGameGrid, 1, 0, 1, 3, win)
        Grid(memoryGameGrid, 2, 0, 2, 3, win)
        Grid(memoryGameGrid, 0, 1, 3, 1, win)
        Grid(memoryGameGrid, 0, 2, 3, 2, win)
    
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
            RandomSquare(x2, y1, x1, y2, "black", time, win)

            if i >= 1:
                RandomSquare(x3, y3, x4, y4, "black", time, win)

                if i >= 2:
                    RandomSquare(x6, y6, x5, y5, "black", time, win) 

                    if i >= 3:
                        RandomSquare(x8, y7, x7, y8, "black", time, win)

                        if i == 4:
                            RandomSquare(x9, y9, x10, y10, "black", time, win)       

        # Verify that the player clicked the correct square in each round
        # if he did add 1 to the counter
        # if he didn't he will loose the game
        if i >= 0:
            click1 = win.getMouse()
            if (clickDetector(click1, x2, y1, x1, y2, win, memoryGameGrid) == 1):
                counter = counter + 1  
            clickDetector(click1, x2, y1, x1, y2, win, memoryGameGrid)      

            if i >= 1:
                click2 = win.getMouse()
                if (clickDetector(click2, x3, y3, x4, y4, win, memoryGameGrid) == 1):
                    counter = counter + 1
                clickDetector(click2, x3, y3, x4, y4, win, memoryGameGrid) 

                if i >= 2:
                    click3 = win.getMouse() 
                    if (clickDetector(click3, x6, y6, x5, y5, win, memoryGameGrid) == 1):
                        counter = counter + 1
                    clickDetector(click3, x6, y6, x5, y5, win, memoryGameGrid) 

                    if i >= 3:
                        click4 = win.getMouse() 
                        if (clickDetector(click4, x8, y7, x7, y8, win, memoryGameGrid) == 1):
                            counter = counter + 1
                        clickDetector(click4, x8, y7, x7, y8, win, memoryGameGrid) 
                        
                        if i == 4:
                            click5 = win.getMouse() 
                            if (clickDetector(click5, x9, y9, x10, y10, win, memoryGameGrid) == 1):
                                counter = counter + 1
                            clickDetector(click5, x9, y9, x10, y10, win, memoryGameGrid) 

        # If he won all the rounds, it means he won the game 
        # everything will be undraw from the screen, a winning trophy will appear
        # and he will have the option to play again or end the game
        if (counter == 5):
            for mG in memoryGameGrid:
                mG.undraw()
            winningTrophy(win)
            playAgainOrGameOver(win)
                 
main()

