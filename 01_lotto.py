import random

numbers = []
n = 0
while n < 6:
  num = random.randint(1,45)
  if num not in numbers:
    numbers.append(num)
    n = n + 1
numbers.sort()
print(numbers)