arr = [5, -3, 0, 9, -2, 7] 
size = len(arr) 

print("Array elements and their status (P = Positive / A = Negative):")

for i in range(size):
    print(f"Element at index {i} = {arr[i]} --> ", end="")
    
    if arr[i] > 0:
        print("P (Positive)")
    elif arr[i] < 0:
        print("A (Negative)")
    else:
        print("Zero (Neither P nor A)")
