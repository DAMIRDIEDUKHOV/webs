name = "Damir"

age = 13

actuall_age=13.54

math = 5 ** 7 + 6 / 9 * 6 - 4

results = age + actuall_age + math
print(results)



print("Hello, welcom to NetqorkChuck Coffee!!!!!!!!!!!!!")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here " + name + ". Get Out of here!!")
        exit()
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

menu = "Black Coffee, Epresso, Latte, Cappucino"

print( name + ", what would you like from our menu today? Here is what we are serving. \n" + menu)

order = input()
price = 8
quantity = input("How many coffees would you like?\n")
total = price * int(quantity) 
print("Thank you. Your total is: $" + str(total))

print(" Sounds good " + name + ", we'll have your " + quantity +" " + order + " ready for you in a moment." )
