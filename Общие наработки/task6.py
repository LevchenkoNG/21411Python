n = int(input())
k = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        if(k > n):
            break
        k+=1
        print(i, end=" ")


