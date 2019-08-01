x11=int(input())
l=list(map(int,input().split()))
for p in range(x11):
	if l[p]>l[p-1] and l[p+1]<l[p]:
		print(l[p])
