#frequency of all occurences.

arr=list(map(int,input("Enter the array elements:").split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

for key in freq:
    print(key,":",freq[key],"times.")