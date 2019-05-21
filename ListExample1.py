menuList = []
priceList = []
def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for food in range(len(menuList)):
        print(menuList[food], priceList[food])
    for price in range(len(priceList)):
        totalPrice += int(priceList[price])
    print("Total price = %d THB"% totalPrice)
while True :
    menuName = input("Please enter your menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
