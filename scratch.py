import random


score = 0
total_score = 0

for i in range(5):
    result = random.randint(1, 2)
    if result == 1:
        print("Congratulation! You found the Treasure.")
        print("You got 500 points.")
        score += 500
        total_score += score
        print("Your score is " + str(total_score))


    else:
        print("Unfortunately! No any Treasure. Try your luck in next destination.")
        print("no points.")
        score += 0
        total_score += score
        print("Your score is " + str(total_score))

print(total_score)


