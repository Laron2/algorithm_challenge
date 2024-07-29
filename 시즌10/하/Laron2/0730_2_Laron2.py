n = int(input())
k = [[0] * 100 for _ in range(100)]

for i in range(n):
    a, b = map(int, input().split())
    
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            k[i][j] = 1
            
su = 0
for i in range(100):
    su += k[i].count(1)
print(su)
