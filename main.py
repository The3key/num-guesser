import random



r = random.randint(1,10)

#if you want to inprove on this code, add "print(r)" for debuging purpusese.

def guess():
  
  i = input("guess")
  i = int(i)


  if r < 5:
     print("its lower than 5")

  if r == 5:
    print("its 5")
    quit()

  if r > 5:
    print("its higher than 5")
 
  if i == r:
    print("correct")
    quit()
  else:
    print("try again")
    
while 1:
  guess()
      
  
