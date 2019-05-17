username = input("Username : ") # Username = admin
password = input("Password : ") # Password = 1123
if username == "admin" and password =="1123":
    print("----Wellcome to GameShopz----")
    print("Game List :")
    print("1. Mario        100 THB"'\n'"2. Contras      999 THB"'\n'"3. Angry bird     5 THB"'\n'"4. Rockman      300 THB")
    selectGame = int(input("Select your game (1-4) : "))
    if selectGame == 1:
        gameName1 = "Mario"
        price1 = 100
        val = int(input("How many piece : "))
        totalPrice = price1*val
        print("Your game is", gameName1, ": Total price", totalPrice, "THB")
    elif selectGame == 2:
        gameName2 = "Comtras"
        price2 = 999
        val = int(input("How many piece : "))
        totalPrice = price2 * val
        print("Your game is", gameName2, ": Total price", totalPrice, "THB")
    elif selectGame == 3:
        gameName3 = "Angry bird"
        price3 = 5
        val = int(input("How many piece : "))
        totalPrice = price3 * val
        print("Your game is", gameName3, ": Total price", totalPrice, "THB")
    elif selectGame == 4:
        gameName4 = "Rockman"
        price4 = 999
        val = int(input("How many piece : "))
        totalPrice = price4 * val
        print("Your game is", gameName4, ": Total price", totalPrice, "THB")