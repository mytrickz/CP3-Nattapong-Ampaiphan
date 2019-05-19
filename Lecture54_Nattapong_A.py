def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showManu()
    else:
        return False
def showManu():
    print("---iNex Shop---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    manuSelect()
def manuSelect():
    userSelect = input("Please select function (1 or 2) : ")
    if userSelect == "1":
        print("Price include vat is",vatCalculate(int(input("Input product price : "))))
    elif userSelect == "2":
        print("Total pricce is",priceCalculate())
def vatCalculate(totalPrice):
    vat = 7/100
    result = totalPrice + (totalPrice*vat)
    return result
def priceCalculate():
    price1 = int(input("1st Product Price : "))
    price2 = int(input("2nd Product Price : "))
    return vatCalculate(price1+price2)

login()