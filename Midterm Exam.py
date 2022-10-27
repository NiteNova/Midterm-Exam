#-------------Question 1-------------#
user = int(input("How many cookies do you have?: "))
if user < 3:
    print("You don't have enough cookies.")
elif user < 11:
    print("You have a good amount of cookies")
else:
    print("You have too many cookies, you should give me one.")


#-------------Question 2-------------#
user = input("Are you a sith or jedi?: ")
if user == 'j' or user == 'jedi' or user == 'J' or user == 'Jedi':
    print("You get a green lightsaber")
elif user == 's' or user == 'sith' or user == 'S' or user == 'Sith':
    print("You get a red lightsaber")
else:
    print("You get a breadstick")


#-------------Question 3-------------#
for i in range(4, 41, 2):
    print(i)


#-------------Question 4-------------#
k = 100
while k > 49:
    print(k)
    k -= 10
    

#-------------Question 5-------------#
j = False
while j != True:
    user = input("Knock Knock, who's there... banana!: ")
    if user == 'orange' or user == 'Orange':
        print("Orange you glad I didn't say banana?!")
        j = True
        
        
#-------------Question 6-------------#
def para(x, y, z):

    return(x * y * z)

print (para(2, 3, 4))


#-------------Question 7-------------#
def bottle(i): 
    for j in range (i, 0, -1):
        print(j, "bottles of root beer on the wall")
        

number = int(input("Enter a number: "))
bottle(number)