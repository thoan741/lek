import math

n = int(input('whatvalue?'))
ans = 0

while n > 0:
    ans = ans + n % 10
    n = int(n / 10)

print(ans)
