a = int(input())
b = int(input())
d = int()
if a > b:
    d = a
else:
    d = b
while d%a != 0 or d%b != 0:
    d+=1
print(d)









