import random 

rand = random.randint(0,10)
while True:
  n = int(input("guess a number:"))
  if n>rand:
    print("too high")
  elif n<rand:
    print("too low")
  else:
    print("Your guess number: %d is correct!!!" %n)
    break
    
