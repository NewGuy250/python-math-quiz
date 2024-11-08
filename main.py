import random
import time

# Function for creating each problem
def create_problem(operand, num1, num2):
    while True:
        try:
            problem = f"{num1} {operand} {num2}"
            correct_answer = eval(problem)
            answer = int(input(problem + " = "))

            if answer == correct_answer:
                return True
            return False
        except ValueError:
            print("Please enter a valid number.\n")
            continue

# Function for getting difficulty level
def get_difficulty():
    while True:
        answer = input("Enter your difficulty (E = Easy, M = Medium, H = Hard): ").lower()
        if answer not in ["e", "m", "h"]:
            print("Please enter a valid option (E, M, H).\n")
            continue
        return answer

# Main function for the quiz
def main():
    # Greeting
    print("Welcome to my Math Quiz!")
    print("You will have answer 10 questions no matter the difficulty. Good Luck!\n")

    OPERANDS = ["+", "-", "*"]
    quiz_length = 10
    
    difficulty = get_difficulty()
    max_range = 10 if difficulty == "e" else 50 if difficulty == "m" else 100
    score = 0

    start_time = time.time()  
    
    print(f"Difficulty: {difficulty.upper()} | Max Range: {max_range}")
    print("Starting the quiz now...\n")
    
    for question_num in range(quiz_length):
        operand = random.choice(OPERANDS)
        num1 = random.randint(0, max_range)
        num2 = random.randint(0, max_range)

        res = create_problem(operand, num1, num2)
        if res:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")

    end_time = time.time()

    # Calculate total time
    total_time = round(end_time - start_time, 2)
    
    # Final score
    print(f"\nFinal Score: {score}/{quiz_length}\nTime: {total_time} seconds")

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
