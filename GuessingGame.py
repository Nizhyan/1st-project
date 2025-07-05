answer=25
max_attempts=3
attempts=0
while attempts<max_attempts:
  attempts+=1
  number=int(input("enter your guess from 1 to 50:"))
  if 0<=number<=50:
    if number<answer:
      print('too low')
    elif number>answer:
      print('too high')
    elif number==answer:
      print("congrats!")
  else:
    print("out of range")
if attempts>=max_attempts:
  print("you have lost")