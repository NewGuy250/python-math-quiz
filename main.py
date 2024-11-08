import random
import time

# Function for creating each problem
def create_problem(operand, num1, num2):
    while True:
        try:
            problem = f"{num1} {operand} {num2}"
            answer = int(input(problem + " = "))
            if answer == eval(problem):
                return True
            return False
        except ValueError:
            print("Please enter a valid number.")
            continue

def get_difficulty():
    while True:
        answer = input("Enter your difficulty (E, M, H): ").lower()
        if answer not in ["e", "m", "h"]:
            print("Please enter a valid option (E, M, H).")
            continue
        return answer

def main():
    # Greeting
    print("Welcome to my Math Quiz!")
    print("You will have 1 minute to answer 10 questions no matter the difficulty. Good Luck!\n")

    OPERANDS = ["+", "-", "*"]
    quiz_length = 10
    difficulty = get_difficulty()
    max_range = 10 if difficulty == "e" else 50 if difficulty == "m" else 100
    score = 0

    print(max_range)
    for _ in range(quiz_length):
        res = create_problem(random.choice(OPERANDS), random.randint(0,max_range), random.randint(0,max_range))
        if res:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"Final Score: {score}/{quiz_length}")


if __name__ == "__main__":
    main()