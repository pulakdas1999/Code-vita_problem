N = int(input())
a = 0
b = 1
for i in range(0,N):
    tmp = a + b
    a = b
    b = tmp
print(b)