
total_score = 0

for i in range(5):
    player = input("Enter 1 or 2.")
    if int(player) == 1:
        print("You got 500 points.")

        total_score += 500
        print("Your score is " + str(total_score))

    else:
        print("no points.")

        total_score += 0
        print("Your score is " + str(total_score))

print(total_score)