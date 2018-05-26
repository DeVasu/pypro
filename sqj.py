a=int(input())
b=int(input())
c=list(int(input().split()))
k=0
print(c)
for i in range(a):
    if c[i]%b==0:
        k+=1
print(k)
