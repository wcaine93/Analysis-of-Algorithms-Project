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

# use mergesort and binary search to count
# the number of occurrences of 53 in numbers
import mergesort as ms
import binary_search as bs
ms.mergesort(numbers)
pos = bs.binary_search(numbers, 53)
# count 53's after and before found 53
count = 0
i = pos;
while numbers[i] == 53:
    count += 1
    i += 1
i = pos-1;
while numbers[i] == 53:
    count += 1
    i -= 1
print(count)