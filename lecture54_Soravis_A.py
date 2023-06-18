def login():
    usernameInput = input('Username :')
    passwordInput = input('Password :')
    if usernameInput == 'admin' and passwordInput == '1234':
        return True
    else:
        return False
def showMenu():
    print('-----iShop----')
    print('1. Vat calculator')
    print('2. Price Calculator')
def menuSelect():
    userselected = int(input('>>'))
    return userselected
def vatCalculate(tprice):
    vatpercent = 1.07
    return tprice*vatpercent
def priceCalculate():
    price1 = int(input('First product price :'))
    price2 = int(input('Second product price :'))
    return vatCalculate(price1+price2)
if login() == True:
    showMenu()
    print('Total price is %.2f THB'%vatCalculate(priceCalculate()))
else:
    print('You are not admin!!')
