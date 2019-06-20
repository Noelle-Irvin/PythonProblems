#CHAPTER 8
# 1. Call a different function from the statistics module

# 2. Create a module named cubed with a function that takes a number as a parameter,
# and returns the number cubed. Import and call the function from another module.

import statistics
import cubed 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(statistics.median_high(numbers))

print(cubed.cubed(4))
