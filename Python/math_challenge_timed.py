import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QES = 5

def prog():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    expr = str(left) + " " + random.choice(OPERATORS) + " " + str(right)
    answer = eval(expr)
    return expr, answer

input("Press Enter to Start!")
print("* --------------------- *")

start_time = time.time()

for i in range(TOTAL_QES):
    expr, answer = prog()
    while True:
        guess = input(expr + ": ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("*  ---------------------*")
print("Great! You solved them in ", total_time, "seconds!!")

