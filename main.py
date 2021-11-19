n = int(input())
sp = []
for _ in range(n):
    sp.append(input())
sp.reverse()
for i in range(n):
    print(sp[i][::-1])
print('goodbye')
print('hi')