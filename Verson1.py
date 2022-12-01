#INTRODUCTION TO OUR FLIGHT GAME #1
import sys
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

print("✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯")
print("WELCOME TO THE FLIGHT SIMULATION GAME!")
print("✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯")

print("You are a traveller who's goal is to find the golden treasure!")
answer = (input("Would you like to see the tutorial? Press y for 'YES' or n for 'NO': "))
opt1 = 'y'
opt2 = 'n'

if answer == opt1:
    print("""""""""You will use WASD as movement keys:
        W for North
        A for WEST
        S for SOUTH
        D for EAST
        add - to go southeast or southwest, add + to go to northwest or southeast
        Then add an longitude angle. 5,15,45 or 85. If you think you don't need an angle just enter the direction example: S
        Also add distance to go to the closest airport in KM
        First guess the distance (example: 350)
        Secondly enter the angle then direction (example: +45A) 
        You will always start from Finland, your goal is to fly to the target country with highest efficiency.
        If you take a wrong turn you lose the game!
        ✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯""""""""")
elif answer == opt2:
    print("Woah you must be good at this game!")
else:
    print("Either you had a typo or you don't like tutorials, that's fine.")

#CHOOSING THE DIFFICULTY
print("Choose what country you would like to travel to (write the difficulty)")
country_dif = ("For EASY Press 1: "
               "\nFor MEDIUM Press 2: "
               "\nFor EXTREME Press 3: ")
print(f"{country_dif}")
answer2 = (input("Choose difficulty level:"))

country1 = '1'
country2 = '2'
country3 = '3'

if answer2 == country1:
    def india_easy():
        print("You have chosen to look for the treasure in INDIA")
    distance1 = int(input("Enter the distance (Between 400-900): "))
    direction1 = str(input("Enter the direction: "))

    # INDIA PHASE 1
    if distance1 in range(650, 750):
        print("Your are heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction1 == "+15D":
        print(f"You are at Moscow airport (UUDD)")
    else:
        sys.exit("☠GAME OVER!☠")
    question1 = (input("Would you like to know the distance to the airport?(USII)"
                       "YES or NO:"))
    if question1 == 'YES':
        def geticao():

        Cursor_obj = db_connect.cursor()
        ICAO_f = input("Enter the first ICAO code: ")
        Cursor_obj.execute(f"select name from airport where ident = '{ICAO_f}';")
        result = Cursor_obj.fetchall()
        ICAO_s = input("Enter the second ICAO code: ")
        Cursor_obj.execute(f"select name from airport where ident = '{ICAO_s}';")
        result = Cursor_obj.fetchall()
        Cursor_obj.execute(f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_f}' or ident = '{ICAO_s}';")
        Geo_lst = []
        for x in Cursor_obj:
            Geo_lst.append(x)
        print(f"The distance between the selected airports is",
              f"{distance.distance(Geo_lst[0], Geo_lst[1]).km:.2f} km")
        geticao()
    # INDIA PHASE 2
    distance2 = int(input("Enter the distance (Between 800-1100): "))
    direction2 = str(input("Enter the direction: "))

    if distance2 in range(910, 1000):
        print("Your are heading the correct direction")
    else:
        sys.exit("☠GAME OVER!☠")
    if direction2 == "-5D":
        print("You have arrived to Izhevsk airport USII(Above kazakhstan)")
    else:
        sys.exit("☠GAME OVER!☠")
    question2 = (input("Would you like to know the distance to the airport?(UATT):"))
    if question2 == 'YES':
        def geticao():
        Cursor_obj = db_connect.cursor()
        ICAO_f = input("Enter the first ICAO code: ")
        Cursor_obj.execute(f"select name from airport where ident = '{ICAO_f}';")
        result = Cursor_obj.fetchall()
        ICAO_s = input("Enter the second ICAO code: ")
        Cursor_obj.execute(f"select name from airport where ident = '{ICAO_s}';")
        result = Cursor_obj.fetchall()
        Cursor_obj.execute(f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_f}' or ident = '{ICAO_s}';")
        Geo_lst = []
        for x in Cursor_obj:
            Geo_lst.append(x)
        print(f"The distance between the selected airports is",
              f"{distance.distance(Geo_lst[0], Geo_lst[1]).km:.2f} km")
        geticao()
    # INDIA PHASE 3

    distance3 = int(input("Enter the distance (Between 500-2200): "))
    direction3 = str(input("Enter the direction: "))

    if distance3 in range(600, 2000):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction3 == "+45S":
        print("You are in kazakhstan airport")
    else:
        sys.exit("☠GAME OVER!☠")

    # PHASE 4

    distance4 = int(input("Enter the distance (Between 1850-2200: "))
    direction4 = str(input("Enter the direction: "))

    if distance4 in range(1950, 2050):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction4 == "+15S":
        print("You are about to reach India's border")
        print("✪✪✪CONGRATULATIONS YOU REACHED INDIA!✪✪✪")
        print("Unfortunately the golden treasure isn't here")
        sys.exit("press run to play again")
    else:
        sys.exit("☠GAME OVER!☠")
    india_easy()

elif answer2 == country2:
    def germany_via_iceland():
        print("")
    print("You have chosen to search for the treasure in GERMANY")
    print("You must travel to Iceland first to visit your grandmother")
    #GERMANY VIA ICELAND
    distance5 = int(input("Enter the distance (Between 300-500): "))
    direction5 = str(input("Enter the direction: "))

    #GERMANY VIA ICELAND PHASE 1
    if distance5 in range(350,450):
      print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction5 == "A":
        print("You are at Stockholm airport")
    else:
        sys.exit("☠GAME OVER!☠")


#GERMANY VIA ICELAND PHASE 2

    distance6 = int(input("Enter the distance (Between 700-800: "))
    direction6 = str(input("Enter the direction: "))

    if distance6 in range(680,780):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction6 == "+85A":
        print("You are at Ålesund airport (Norway)")
    else:
        sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 3

    distance7 = int(input("Enter the distance (Between 300-500: "))
    direction7 = str(input("Enter the direction: "))

    if distance7 in range(350,450):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction7 == "+85A":
        print("You are in Reykjavik airport")
    else:
        sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 4

    distance8 = int(input("Enter the distance (Between 1400-1700: "))
    direction8 = str(input("Enter the direction: "))

    if distance8 in range(1440-1599):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")

    if direction8 == "+45S":
        print("You are in Dublin airport (Ireland)")
    else:
        sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 5

    distance7 = int(input("Enter the distance (Between 350-550: "))
    direction7 = str(input("Enter the direction: "))

    if distance7 in range(400-500):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction7 == "+85S":
        print("You are in Heathrow airport")
    else:
        sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 6

    distance8 = int(input("Enter the distance (Between 550-750: "))
    direction8 = str(input("Enter the direction: "))

    if distance8 in range(600-700):
        print("Your are at heading the correct direction")
    else:
        sys.exit("☠GAME OVER☠!")
    if direction8 == "+85S":
        print("You are about to reach Frankfurt airport")
        print("✪✪✪CONGRATULATIONS YOU REACHED GERMANY!✪✪✪")
        print("You found a note that says: HAHA I took the treasure "
              "you'll never find me!")
        sys.exit("press run to play again")
    else:
        sys.exit("☠GAME OVER!☠")
    germany_via_iceland()


# ALASKA
elif answer2 == country3:
    def alaska():
        print("You have chosen to go to ALASKA, which is known for their gold")
    direction9 = str(input("Enter the direction: "))
    if direction9 == "A":
        print("You flew across sweden and norway, you are in Iceland (Reykjavik airport)")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 2
    direction10 = str(input("Enter the direction: "))
    if direction10 == "A":
        print("You are in Greenland")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 3
    direction11 = str(input("Enter the direction: "))
    if direction11 == "S":
        print("You are in Thunder Bay airport(Ontario, Canada)")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 4
    direction12 = str(input("You are flying inside Canada's provinces now enter direction: "))
    if direction12 == "A":
        print("You are in the province of Manitoba")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 5
    direction13 = str(input("Enter the direction: "))
    if direction13 == "A":
        print("You are in the province of Saskatchewan")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 6
    direction14 = str(input("Enter the direction: "))
    if direction14 == "W":
        print("You are in the province of Northwest Territories ")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 7
    direction15 = str(input("Enter the direction: "))
    if direction15 == "A":
        print("You are in the province of Yukon (Canada)")
    else:
        sys.exit("☠GAME OVER!☠")

    # ALASKA PHASE 8
    direction16 = str(input("Enter the direction: "))
    if direction16 == "A":
        print("✪✪✪CONGRATULATIONS YOU REACHED ALASKA!✪✪✪")
        print("You found the golden treasure, you have beaten the game!!")
        sys.exit("press run to play again")
    else:
        sys.exit("☠GAME OVER!☠")
    alaska()


else:
    def whatever():
        print("Invalid difficulty or typo")
whatever()
