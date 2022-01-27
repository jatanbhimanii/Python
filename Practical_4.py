n = int(input("Enter number of elements : "))
 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
b = []

a.sort()

for i in range(len(a)):
    if a[i]<max(a):
        b.append(a[i])
        
print(max(b))