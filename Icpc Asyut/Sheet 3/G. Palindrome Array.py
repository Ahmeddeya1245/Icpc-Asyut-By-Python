n = int(input())
lst = list(map(int,input().split()))
lst1 = []
while n-1 >=0:
    n = n-1
    lst1.append(lst[n])
if lst1 == lst :
    print("YES")
else :
    print("NO")