a = [1,1]
n = 150
for i in range(2, n+1):
    a.append(a[-1] + a[-2])
print(a[-1])
