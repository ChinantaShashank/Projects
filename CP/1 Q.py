
N=int(input())
arr=list(map(int,input().split()))
sums=0
for i in arr:
    sums=sums+i
mins=arr[0]
for j in arr:
    if(j<mins):
        mins=j
if(mins==arr[0]):
    maxs=arr[1]
    for w in arr:
        if(w>maxs):
            maxs=w
else:
    maxs=arr[0]
    for w in arr:
        if(w>maxs):
            maxs=w
ave=sums/len(arr)
print(sums)
print(mins)
print(maxs)
print(ave)
