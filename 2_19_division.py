i = 1
n = 120
count = 0

while i <= n:
    if n % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개입니다.".format(n, count))
