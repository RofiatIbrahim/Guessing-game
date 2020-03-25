#Guessing Game 
Secret_number= 70
guess_count= 0 
guess_limit= 5
while guess_count < guess_limit: 
 guess = int(input("Guess: "))
 guess_count += 1 
 if guess == Secret_number: 
  print ("You Won🥳🥳")
  break
 elif guess > Secret_number:
  print("Sorry, You Failed! Secret number is lower") 
 else: 
  print("Sorry, You Failed! Secret number is higher")
print(abs(guess - Secret_number))