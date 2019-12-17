list = [int(z) for z in input().split()]
x = int(input())
bool = False
for z in range(len(list)):
    if(list[z] == x):
        bool = True
        print(z, end=" ")
if(not bool):
    print("Отсутствует")