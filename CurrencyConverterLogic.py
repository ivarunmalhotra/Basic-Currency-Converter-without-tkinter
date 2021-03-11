#Install package before running this code
#To install package open command prompt and type- pip install forex-python

#Importing package for real time currency rates and some converting features
from forex_python.converter import CurrencyRates, CurrencyCodes

#Function which will convert one money into another
def converter():
    print("\n---------------------------------------------------------------\n")
    print("\tCURRENCY CONVERTER MENU\n\t********* ********* *****")
    
    money_1 = input("\nEnter currency name which you want to convert: ").upper()
    money_2 = input("Enter currency name you want to convert into: ").upper()
    amount = float(input("Enter amount you want to convert: "))

    #Calling CurrencyRates() method from package
    c = CurrencyRates()
    
    print("\n", amount, money_1, "=", c.convert(money_1, money_2, amount), money_2)
    print("\n---------------------------------------------------------------\n")


#Function for printing currency symbol
def symbol():
    print("\n---------------------------------------------------------------\n")
    print("\tCURRENCY SYMBOL MENU\n\t********* ****** *****")
    
    curr = input("\nEnter Currency: ").upper()

    #Calling CurrencyCodes() method from package
    c = CurrencyCodes()
    
    print(curr.upper(), "=", c.get_symbol(curr.upper()))
    print("\n---------------------------------------------------------------\n")



#Function for printing currency name 
def name():
    print("\n---------------------------------------------------------------\n")
    print("\tCURRENCY NAME MENU\n\t********* **** *****")
    
    curr = input("\nEnter Currency: ").upper()

    #Calling CurrencyCodes() method from package
    c = CurrencyCodes()
    
    print(curr, "=", c.get_currency_name(curr))
    print("\n---------------------------------------------------------------\n")


def unkn():
    print("Invalid Choice")


ch = 'y'

while ch=='y':
    print("\n---------------------------------------------------------------\n")
    print("\t     CURRENCY CONVERTER\n\t     ********* *********")
    print("\n1. Convert Currency\n2. Find Currency Symbol\n3. Find Currency Name")
    print("\n---------------------------------------------------------------\n")
    
    choice = int(input("Enter your choice: "))

    #Calling above defined functions
    if choice==1:
        converter()    
    elif choice==2:
        symbol()    
    elif choice==3:
        name()   
    else:
        unkn()
    
    ch = input("Do you want more operations(y/n): ")

print("\nTHANK YOU.............")
