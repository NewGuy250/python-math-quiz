import random

# Function for creating each problem
def create_problem(operand, num1, num2):
    while True:
        try:
            problem = f"{num1} {operand} {num2}"
            answer = int(input(problem + "= "))
            if answer == eval(problem):
                return True
            return False
        except ValueError:
            print("Please enter a valid number.")
            continue

def main():
    OPERANDS = ["+", "-", "*"]

if __name__ == "__main__":
    main()