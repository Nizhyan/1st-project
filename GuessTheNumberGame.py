

import random
#import the random module
x=random.randint(1,101)
#make a variable that selects a random number in a certain range
max_attempts=3
attempts=0
#give the user a certain amount of attempts to to guess the number
while attempts<max_attempts:
    y=int(input("guess a number between 1 and 100:"))
#have the user input the number they're guessing
    attempts+=1
#each time the user guesses wrong the number goes up until it reahes the max_attempts and they lose
    if int(y)>int(x):
        print("too high")
    elif int(y)<int(x):
        print("too low")
    elif int(y)==int(x):
      print("you won!")
      break
#use if-else statements to help the user guess more accurately
else:
    print("you lost")
#print "you lost" if the user runs out of attempts and haven't guessed the right number
