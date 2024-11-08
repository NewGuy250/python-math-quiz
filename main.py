import random
import time

# Function for creating each problem
def create_problem(operand, num1, num2):
    while True:
        try:
            problem = f"{num1} {operand} {num2}"
            correct_answer = eval(problem)  # Calculating the correct answer
            answer = int(input(problem + " = "))  # Asking user for input

            if answer == correct_answer:
                return True
            return False
        except ValueError:
            print("Please enter a valid number.")
            continue

# Function for getting difficulty level
def get_difficulty():
    while True:
        answer = input("Enter your difficulty (E = Easy, M = Medium, H = Hard): ").lower()
        if answer not in ["e", "m", "h"]:
            print("Please enter a valid option (E, M, H).")
            continue
        return answer

# Main function for the quiz
def main():
    # Greeting
    print("Welcome to my Math Quiz!")
    print("You will have 1 minute to answer 10 questions no matter the difficulty. Good Luck!\n")

    # Difficulty levels and operands
    OPERANDS = ["+", "-", "*"]
    quiz_length = 10
    
    difficulty = get_difficulty()
    max_range = 10 if difficulty == "e" else 50 if difficulty == "m" else 100
    score = 0

    # Timer setup (1 minute to answer 10 questions)
    start_time = time.time()
    time_limit = 60  # Time limit in seconds
    
    print(f"Difficulty: {difficulty.upper()} | Max Range: {max_range}")
    print("Starting the quiz now...\n")
    
    for question_num in range(quiz_length):
        # Check if time is up
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("\nTime's up! You've run out of time.")
            break

        # Ask a question
        operand = random.choice(OPERANDS)
        num1 = random.randint(0, max_range)
        num2 = random.randint(0, max_range)

        res = create_problem(operand, num1, num2)
        if res:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        # Time remaining
        remaining_time = time_limit - int(elapsed_time)
        print(f"Time Remaining: {remaining_time} seconds\n")
    
    # Final score
    print(f"\nFinal Score: {score}/{quiz_length}")

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
