def numberGame():
  import random
  mynum = random.randint(0, 9)


  while True:
    guess = int(input("Can you guess my number?: "))

    if (guess == mynum):
      print("Congrats! You guessed correctly")
      break
    elif(guess > mynum):
      print("My number is smaller than your guess. Try again.",end="\n\n")
    else:
      print("My number is larger than your guess. Try again.",end="\n\n")
