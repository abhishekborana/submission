length=int(input())
nPhotos=int(input())
arr=[]
for i in range(nPhotos):
    m,n=map(int,(input().split()))
    arr.append([m,n])
# print(arr)

for i in range(nPhotos):
    if(arr[i][0]<length or arr[i][1]<length):
        print("UPLOAD ANOTHER")
    elif(arr[i][0]==arr[i][1]):
        print("ACCEPTED")
    else:
        print("CROP IT")
