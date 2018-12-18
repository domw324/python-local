import random
# numbers에 1부터 45까지 넣기
numbers = list(range(1,46))
# numbers에서 6개 비복원추출
a = random.sample(numbers,6)
a.sort()
# a.sort(reverse = True)
print(a)