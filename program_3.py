# Program #3: Capital Quiz
#3/20/26
#Josiah Hendley
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random

def capital_quiz():

    # Dictionary of states and capitals
    capitals = {
        "Minnesota": "St. Paul",
        "Wisconsin": "Madison",
        "Iowa": "Des Moines",
        "California": "Sacramento",
        "Texas": "Austin",
        "Florida": "Tallahassee",
        "New York": "Albany",
        "Georgia": "Atlanta",
        "Ohio": "Columbus",
        "Colorado": "Denver"
    }

    correct = 0
    incorrect = 0

    states = list(capitals.keys())

    # Ask 5 random questions
    for _ in range(5):
        state = random.choice(states)
        answer = input(f"What is the capital of {state}? ")

        if answer.strip().lower() == capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The capital is {capitals[state]}.")
            incorrect += 1

    print("\nQuiz complete!")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)


# Run the quiz
if __name__ == "__main__":
    capital_quiz()
