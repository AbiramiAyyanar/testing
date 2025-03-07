n=int(input("enter a number:"))
for i in range(n):
    if i<=n//2:
        print(' '*(n//2-i)+'*'*(2*i+1))
    else:
        print(' '*(i-n//2)+'*'*(2*(n-i)-1))