import random
import time

operators = ["+", "-", "*"]
MIN_VALUE = 1
MAX_VALUE = 10

def generate_math():
    left_number = random.randint(MIN_VALUE, MAX_VALUE)
    right_number = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(operators)
    expr = str(left_number) + " " + operator + " " + str(right_number)
    return expr, eval(expr)

correct_ans = 0
ans_cheat_sheet = []
problem_count = input("How many problems do you want to solve under 1 minute? ")


if not problem_count.isdigit():
    print("Invalid entry")
else:
    input("Press enter once you're ready!")
    print("------------------------------")
    start_time = time.time()
    problem_count = int(problem_count)
    for i in range(problem_count):
        expr, ans = generate_math()
        ans_cheat_sheet.append(ans)
        user_ans = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if user_ans == str(ans):
            correct_ans += 1
    print("------------------------------")
    end_time = time.time() - start_time
    print("Your total score is :", correct_ans, " out of ", problem_count)
    print("\nYou took ", round(end_time), " seconds!")
    print("\nHere are the correct answers :", ans_cheat_sheet)