# CHAPTER 9
# 1. Find a file on your computer and print its contents using Python.

with open("file.txt", "r") as file:
    print(file.read())


# 2. Write a program that asks a user a question , and saves their answer to a file

answer = input("What is your favorite color?")
st = open("color.txt", "w")
st.write(answer)
st.close()

# 3. Take the items in this list of lists:

listOfLists = [["Top Gun", "Risky Business", "Minority Report"],
               ["Titanic", "The Revenant", "Inception"],
               ["Training Day", "Man on Fire", "Flight"]]

# and write them to a CSV file. The data from each list should be a row in the file
# with each item in the list separated by a comma.

import csv

with open("movies.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for list in listOfLists:
        w.writerow(list)
        
