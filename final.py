import time, os, importlib, random
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root@123',
    autocommit=True
)



###generate number of airport
def count_airport():
    sql = "select count(airport.name) from airport " \
          "inner join country on airport.iso_country=country.iso_country " \
          "where country.name='" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    for num in result:
        print(num)



###generate list of airport
def airport_selection():
    sql = "select airport.name from airport " \
          "inner join country on airport.iso_country=country.iso_country " \
          "where country.name='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = [result]
    for x in range(len(airports)):
        print(airports)


### to generate random code
def code():
    lock = ["Abra", "Dabra", "Abra-Dabra"]
    print(random.sample(lock, 1))

code()


name = input("Enter name of the country: ")
num = count_airport()
airport_selection()

### select random airport
def randmom_selection():
    sql = "select airport.name from airport " \
          "inner join country on airport.iso_country=country.iso_country " \
          "where country.name='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = [result]
    for x in airports:
        print(*random.sample(x, 3), sep="\n")
    return airports


###select item in list
def item_list():
    sql = "select airport.name from airport " \
          "inner join country on airport.iso_country=country.iso_country " \
          "where country.name='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = [result]
    location = []
    for y in range(3):
        for x in airports:
            location.append(random.sample(x, 1))
    print(f"1. " + str(location[0]))
    print(f"2. " + str(location[1]))
    print(f"3. " + str(location[2]))
    return location



### print random name using dictionary
def random_selection():
    sql = "select airport.name from airport " \
          "inner join country on airport.iso_country=country.iso_country " \
          "where country.name='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = [result]
    aero_plane = ["", "", ""]

    for i in range(3):
        location = []
        for x in airports:
            location.append(random.sample(x, 3))
        aero_plane[i] = location[0][0][0]
    print(f"1. {aero_plane[0]}")
    print(f"2. {aero_plane[1]}")
    print(f"3. {aero_plane[2]}")
    return aero_plane

###
print("****************  Wel-Come To Game Treasure Hunt  ***************")
name = input("Enter name of the country: ")
random_selection()


###To find treasure
def treasure():
    result = random.randint(1, 2)
    while True:
        if result == 1:
            print("Congratulation! You found the Treasure.")
            break

        else:
            print("Unfortunately! No any Treasure. Try your luck in next destination.")
            break
        return

import random



### To find treasure and guess code
def treasure():
    result = random.randint(1, 2)

    while True:
        lock = ["Abra", "Dabra", "Abra-Dabra"]
        chosen = random.choice(lock)
        print(chosen)

        if result == 1:
            print("Congratulation! You found the Treasure.\n")
            print("Choose the lock to open your treasure.")
            print(f"1. {lock[0]}")
            print(f"2. {lock[1]}")
            print(f"3. {lock[2]}\n")

            player1 = input("Enter number 1, 2, 3: ")

            if int(player1) == 1:
                if lock[0] == chosen:
                    print("Congratulation! You have unlocked the Treasure.")
                    break

                else:
                    print("OOPs! Wrong code.")
                    print("The correct code was *** " + chosen + " ***")
                    break

            elif int(player1) == 2:
                if lock[1] == chosen:
                    print("Congratulation! You have unlocked the Treasure.")
                    break

                else:
                    print("OOPs! Wrong code.")
                    print("The correct code was *** " + chosen + " ***")
                    break

            elif int(player1) == 3:
                if lock[2] == chosen:
                    print("Congratulation! You have unlocked the Treasure.")
                    break

                else:
                    print("OOPs! Wrong code.")
                    print("The correct code was *** " + chosen + " ***")
                    break

            else:
                print("Sorry, Wrong input.")
                break

        else:
            print("Unfortunately! No any Treasure. Try your luck in next destination.")
            break
    return


treasure()


###Calculate points


score = 0
current_score = 0
Total_score = current_score + score


for i in range(5):
    player = input("Enter 1 or 2.")
    if int(player) == 1:
        print("You got 500 points.")
        score = 500
        Total_score += current_score + score
        print("Your score is " + str(Total_score))

    else:
        print("no points.")
        score = 0
        Total_score += current_score + score
        print("Your score is " + str(Total_score))

print(Total_score)


###kilometer


def distance():

    milage = 0
    current_milage = 0
    Total_milage = current_milage + milage

    for i in range(5):
        if Total_milage < 1000:
            player = input("Enter 1 or 2.")
            if int(player) == 1:
                print("You distance is 500 km.")
                milage = 500
                Total_milage += current_milage + milage
                print("Your milage is " + str(Total_milage))

            else:
                print("no points.")
                milage = 0
                Total_milage += current_milage + milage
                print("Your milage is " + str(Total_milage))

    else:
        print("game over.")
    return