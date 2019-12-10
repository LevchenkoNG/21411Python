#если а часов, то норома, если б часов, то пересып, сейчас н, а<=b
a=int(input())
b=int(input())
h=int(input())
if h>=a and h<=b:
    print("это нормально")
if h>b:
    print("пересып")
if h<a:
    print("недосып")