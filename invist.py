import time, os, importlib, random
import mysql.connector
from geopy import distance
import random_airports
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root@123',
    autocommit=True
)

version_of_the_game = "Airport Game v.1"
global airport_selections
airport_selections = []

#Game - Main Function
def game(difficulty):
    def startlocation():
        return "Helsinki Vantaa Airport"
    def new_turn(new_location, coleft, current_score):
        #FUNCTIONS
        start = "Finland"
        def airport_and_package(airport_number):
            def pkgtype():
                type = random.randint(1, 3)
                if type == 1:
                    type = "Silver"
                elif type == 2:
                    type = "Bronze"
                elif type == 3:
                    type = "Gold  "
                return type
            def airportdist1():
                sql = "select airport.latitude_deg, airport.longitude_deg from airport " \
                      "where airport.name = '"+new_location+"'"
                cursor = connection.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    y = (row[0],row[1])
                return y
            def airportdist2():
                sql = "select airport.latitude_deg, airport.longitude_deg from airport " \
                      "where airport.name = '"+random_airport+"'"
                cursor = connection.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    x = (row[0],row[1])
                return x
            # RANDOM AIRPORT
            random_airport =  airport_selections[airport_number] #airport()
            dist = int(((int(distance.distance(airportdist2(), airportdist1()).km))*112)/1000)
            airport_pkg = [f"{pkgtype()}", f"{random_airport}", f"{dist}"]
            return airport_pkg

        ### WEATHER & POINT CALCULATION
        def calculations(airport_pkg, co2_left, score):
            distance_to = int(airport_pkg[2])
            co2_left = co2_left - distance_to
            airport_pkg.append(co2_left)

            if co2_left <= 0:
                airport_pkg.append(score)
                returnlist = airport_pkg
                return returnlist

            if airport_pkg[0] == "Bronze":
                amount_points = weather(1)
                time.sleep(2)
            elif airport_pkg[0] == "Silver":
                amount_points = weather(2)
                time.sleep(2)
            elif airport_pkg[0] == "Gold  ":
                amount_points = weather(3)
                time.sleep(2)
            score = score + amount_points
            airport_pkg.append(score)
            returnlist = airport_pkg
            return returnlist


        player_location = new_location

    #    airport_list = [airport_pkg1,airport_pkg2,airport_pkg3,airport_pkg4,airport_pkg5 ]
    ##    airport_names = random_airports.index_selection(current_airport)

    #    for i in range(len(airport_list)):
    #        airport_list[i] = airport_and_package(i)
    #        airport_list[i].append(i+1)


        airport_pkg1 = airport_and_package(0)
        airport_pkg1.append(1)

        airport_pkg2 = airport_and_package(1)
        airport_pkg2.append(2)

        airport_pkg3 = airport_and_package(2)
        airport_pkg3.append(3)

        airport_pkg4 = airport_and_package(3)
        airport_pkg4.append(4)

        airport_pkg5 = airport_and_package(4)
        airport_pkg5.append(5)


        co2_left = coleft
        score = current_score
        print(f"\n\nYou are in: {player_location}                 "
              f"CO2 left: {co2_left}                 "
              f"Score: {score} "
              f"\n\nChoose next location: "
              f"\n      Type        Airport                                                      Distance (CO2)"
              f"\n{airport_pkg1[3]}.    {airport_pkg1[0]}      {airport_pkg1[1]:<39s}                      {airport_pkg1[2]}"
              f"\n{airport_pkg2[3]}.    {airport_pkg2[0]}      {airport_pkg2[1]:<39s}                      {airport_pkg2[2]}"
              f"\n{airport_pkg3[3]}.    {airport_pkg3[0]}      {airport_pkg3[1]:<39s}                      {airport_pkg3[2]}"
              f"\n{airport_pkg4[3]}.    {airport_pkg4[0]}      {airport_pkg4[1]:<39s}                      {airport_pkg4[2]}"
              f"\n{airport_pkg5[3]}.    {airport_pkg5[0]}      {airport_pkg5[1]:<39s}                      {airport_pkg5[2]}")
        while True:
            Choice = input("Enter: ")

            if int(Choice) == 1:
                returnlist = calculations(airport_pkg1, co2_left, score)
                break
            elif int(Choice) == 2:
                returnlist = calculations(airport_pkg2, co2_left, score)
                break
            elif int(Choice) == 3:
                returnlist = calculations(airport_pkg3, co2_left, score)
                break
            elif int(Choice) == 4:
                returnlist = calculations(airport_pkg4, co2_left, score)
                break
            elif int(Choice) == 5:
                returnlist = calculations(airport_pkg5, co2_left, score)
                break
            else:
                print("Try again")

        return returnlist
    starting_score = 0
    starting_location = startlocation()
    starting_difficulty = difficulty

    airport_selections = random_airports.index_selection("Helsinki Vantaa Airport")
    returnls = new_turn(starting_location,starting_difficulty,starting_score)
    for x in range (1000):
        os.system('cls')
    #    global airport_selections
        airport_selections = random_airports.index_selection(returnls[1])
        if returnls[4] <0:
            break
        returnls = new_turn(returnls[1], returnls[4], returnls[5])
    time.sleep(1)
    os.system('cls')
    print("\n\n\n\n\nGame Over\n\n"
          "You picked an airport that was too far away\n\n")
    print(f"Your score was: {returnls[5]}")
    time.sleep(1)
    return returnls[5]
final_score = game(difficulty)
while True:
    replay_choice = input("\n\nDo you wish to replay? (y/n) \n"
                          "Enter: ")
    if replay_choice == "y":
        time.sleep(0.5)
        os.system('cls')
        final_score = game(difficulty)
    elif replay_choice == "n":
        break
    else:
        print("Check your spelling\n\n")
        continue
###
