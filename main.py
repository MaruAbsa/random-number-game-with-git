import random
num = 0

def generate_random_number():
  return random.randint(1,100)



def difference_from_answer(guess,answer):
  if guess == answer:
    return "Correct"
  elif guess > answer:
    return "Guess is too high"
  else:
    return "Guess is too low"


def make_a_guess():
   user = int(input("Guess a number between 1 and 100 "))
   random_number = generate_random_number()
   return difference_from_answer(user,random_number)


print(make_a_guess())