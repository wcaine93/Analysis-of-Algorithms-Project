# generate 100,000 numbers randomly in the range (0,125) inclusive
import random
numbers = [random.randint(1, 125) for i in range(100000)]

# sequential search for the first occurrence of 53 in numbers
for number,i in enumerate(numbers):
    if number == 53:
        print("53 found at", i)
        break

# count the number of occurrences of 53 in numbers
count = 0
for number in numbers:
    if number == 53: count += 1
print(count)