# Memory Game

## Introduction
Memory is a game in which you have to memorize the squares that ligth up in a particular order and then click the squares in this order.

## Libraries
The libraries used during this project where graphics, random and time.

## Code Explanation
  - I started by importing * from the graphics library, the random library and the time library. Then,  created the graphics window, and set up the backgroung color and coordinates. Also, I created the grid of the game. 
  - After we had all that, I created a for loop in a range of 5 that contains the core of the game. Inside this loop I created a counter variable that will count the number of rounds won. Then, I created variables that will select random points within a limit. Once that is done, I used if's to create the random squares with the points obtained and to display the correct number of squares in each round. Then, I verified if the player clicked the correct square in each round. If he did the square turns yellow and if he got everything in the round correct sums one to the counter. If he didn't he will loose the game. If the counter is 5, the player would have won the game. 
  - Once the game is finished I undraw the grid and changed the background. Then, displayed a win or lost message.
  - At last, we ask the player if he wants to play again or quit, if the player choses to play again the page will close and another game will start and if he chooses to quit the  window will close
