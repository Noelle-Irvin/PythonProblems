#CHAPTER 7
# 1. Print each item in the following list
listOfItems = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in listOfItems:
    print(show)

# 2. Print all numbers from 25 to 50

# for i in range(25, 51):
#    print(i)

# 3. Print each item in the list from the first challenge and their indexes

for i, show in enumerate(listOfItems):
    print(show + ' ' + str(i))

# 4. Write a program with an infinite loop (with the option to type q to quit) and a list
# of numbers. Each time through the loop ask the user to guess a number on the list and tell them
# whether or not they guessed correctly

while True:
    print("type q to quit")
    x = input("Number:")
    list = [ "1", "2", "3"]
    if x in list:
        print("You got it")
    elif x == "q":
        break;
    else:
        print("wrong")
    

# 5. Mulitply all the numbers in the list [ 8, 19, 148, 4] with all the numbers
# in the list [9, 1, 33, 83] and append each result to a third list
thirdList = []

for x in [8, 19, 148, 4]:
    for y in [9, 1, 33, 83]:
        thirdList.append(x * y)

print(thirdList)
