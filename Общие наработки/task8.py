string = input().split()
a = []
i = 0
sum_m = 0

while string[0] != 'end':
    a.append([])
    a[i] = string
    i += 1
    string = input().split()

for i1 in range(i):
    for j1 in range(len(a[0])):
        if (j1 - 1) < 0 :
            sum_m = sum_m + int(a[i1][len(a[0]) - 1])
        else :
            sum_m = sum_m + int(a[i1][j1 - 1])
        if (j1 + 1) > len(a[0]):
            sum_m = sum_m + int(a[i1][0])
        else :
            sum_m = sum_m + int(a[i1][j1 + 1])
        if (i1 - 1) < 0 :
            sum_m = sum_m + int(a[i1][j1])
        else :
            sum_m = sum_m + int(a[i - 1][j1])
        if (i1 + 1) > i :
            sum_m = sum_m + int(a[0][j1])
        else :
            sum_m = sum_m + int(a[i1 + 1][j1])
        print(sum_m, end = " ")
        sum_m = 0
    print()





'''while string != "end":
    a[i] = string
    i+=1
print(a)
while string[0] != 'end':
    #list = [[int(z) for z in input().split()] for z in input()]
print(list)'''

