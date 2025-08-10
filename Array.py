arr = []
n = int(input("Enter the number of elements in the array: "))

print(f"Enter {n} elements:")
for i in range(n):
    num = int(input())
    arr.append(num)
    
element = int(input("Enter the element to insert at the end: "))
arr.append(element)  

print("Array after inserting at the end:")
for num in arr:
    print(num, end=" ")
