#Name: Hanz De Guzman
#Email: hanz.deguzman87@myhunter.cuny.edu
#Date: September 13, 2021
#This program shifts the characters by 5

a = input("Enter a message: ")

for i in a:
    b = c = ord(i) + 5
    c = chr(b)
    print(i,"shifted by 5 characters is:",c )
