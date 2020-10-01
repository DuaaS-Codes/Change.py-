#Author: Duaa Shahzad
#Date: November 5th, 2019
#Title: Change

intChange = (int)(input("Enter the change in cents:"))
intQuarters = intChange//25 
intDimes = intChange//10%10
intNickels = intChange//5%1
intPennies = intChange//1%10

print("The minimum number of coins is: ")
print("Quarters: ",intQuarters)
print("Dimes: ",intDimes)
print("Nickels:",intNickels)
print("Pennies:",intPennies) 
