n=int(input())
#if n==0:
    #print(n, "программистов")
if n==1:
    print(n,"программист")
if n>1 and n<5:
    print(n, "программиста")
#if n>4 and n<20:
    #print(n, "программистов")
if n>20 and n<100 and 1<n%10<5:
    print(n, "программиста")
if 100<n<1000 and 1<n%100<5:
    print(n,"программиста")
if n%100==1:
    print(n, "программист")
if n%10<1 and n%10>5:
    print(n,"программистов")
elif n%100<1 and n%100>5:
    print(n, "программистов")
