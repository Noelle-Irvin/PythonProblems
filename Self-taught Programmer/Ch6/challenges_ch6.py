# 1.
string = "Camus"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])

# 2.
response_one = input("Give me an object:")
response_two = input("Now give me a person:")
string = "Yesterday I wrote a {}. I sent it to {}."
print(string.format(response_one, response_two))

# 3.
string = "aldous Huxley was born in 1894."
print(string.capitalize())

# 4.
string = "Where now?, Who now?, When now?"
print(string.split(", "))

# 5.
listFox = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(listFox)[:-2] +".")

# 6.
string = "A screaming comes across the sky."
print(string.replace("s", "$"))

# 7.
string = "Hemingway"
print(string.index("m"))

# 8.
print("Find dialoque in your favorite book \"(containing quotes)\" and turn it into a string.")

# 9.
string = "three"
print(string + string +string)
print(string * 3)

# 10.
string = "It was a bright cold day in April, and the clocks were striking thirteen."
print(string[:33])
