import random
num = 0

def generate_random_number():
  return random.randint(1,100)
  


def difference_from_answer(guess):
  answer = generate_random_number()
  if guess == answer:
    return "Correct"
  elif guess > answer:
    return "Guess is too high"
  else:
    return "Guess is too low"
print(difference_from_answer(100))