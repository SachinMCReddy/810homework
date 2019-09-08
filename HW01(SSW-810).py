# Rock,Paper,Scissors
#The rock, paper, scissors combination contains 9 possible combination outputs to be considered 
# input choice are provided to human and computer choice is generated randomly 

import random # Random choice from computer
moves = ["r", "p", "s"] #r- rock, p - paper, s-scissors 
play_until = "q" 
while play_until == "q": #the game can played until q is entered by human through keyboard
   humanmove = input(" please enter: p,q,r or q to quit: ") #the human needs to input from the keyboard
   computermove = random.choice(moves)  #random.choice() is built in function 
   
   
   print("the computermove",computermove)
 # when the computer input and human output is same the it is considered as a tie 
   if computermove == humanmove:
      print("tie")
 #the combination result for humanmove (rock)
   elif humanmove == "r" and computermove == "s":
      print("human wins")
   elif humanmove == "r" and computermove == "p":
      print("computer wins")
 #the combination result for humanmove (paper)
 
   elif humanmove == "p" and computermove == "s":
      print("computer wins")
   elif humanmove == "p" and computermove == "r":
      print("human wins")

 #the combination result for humanmove (scissors) 
   elif humanmove == "s" and computermove == "p":
      print("human wins")
   elif humanmove == "s" and computermove == "r":
      print("computer wins")

   elif humanmove == "q":
      print("end game")
      break     #this ends the while loop from being in loop continously 
   play_until = "q"




