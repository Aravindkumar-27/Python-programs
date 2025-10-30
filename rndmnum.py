import random
crt_num=random.randint(1,100)


while(True):
    guess_num=int(input("Enter your guess"))
    
    if(guess_num>crt_num):
      print("too high ")
    
    elif(guess_num<crt_num):
      print("too low")
    else:
      print("Your guess is right")
    

    


