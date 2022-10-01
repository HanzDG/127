#Name: Hanz De Guzman
#Email: hanz.deguzman87@myhunter.cuny.edu
#Date: September 13, 2021
#This program prints a phrase, reverses it and finds the last letters of that phrase

a = input("Enter a phrase: ")
b = a.split()
print("Reversed phrase: ",a[::-1])
c = ""
for i in b:
    c += (i[-1])[-1]

print("Last letters of reverse phrase: ",c)
   

    






