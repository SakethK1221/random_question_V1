import random
from random_question_v1.data import name_list, Question
from random_question_v1.selector import rand_draw

#while True:
 #   chosen_name, chosen_question = rand_draw(name_list, Question)
  #  print(f"{chosen_name}, please answer: {chosen_question}")
   # user_choice = input("Enter 'Y' to continue, or any other key to quit: ")
    #if user_choice.upper() != 'Y':
     #   break

random.seed() # To get different sequences each time the notebook is run

current_names_pool = []
last_chosen_name = None

print("Starting the random name and question game!\n")

while True:
    # If the current pool of names is empty, refill it and shuffle
    if not current_names_pool:
        current_names_pool = list(name_list)  # Create a fresh copy
        random.shuffle(current_names_pool)  # Shuffle the names for random order

    # Choose a name from the current pool
    chosen_name = current_names_pool.pop(0)  # Get and remove the first name

    # If the chosen name is the same as the last one, and there are other names available,
    # re-insert the chosen name at the end and pick another.
    if chosen_name == last_chosen_name and len(current_names_pool) > 0:
        current_names_pool.append(chosen_name)  # Put it back at the end
        chosen_name = current_names_pool.pop(0)  # Pick a different one from the start

    chosen_question = random.choice(Question)
    print(f"{chosen_name}, please answer: {chosen_question}")

    last_chosen_name = chosen_name  # Update the last chosen name for the next iteration

    user_choice = input("Enter 'Y' to continue, or any other key to quit: ")
    if user_choice.upper() != 'Y':
        break

print("\nGame ended.")