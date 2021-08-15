import random
 
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# creating array
arr = [item for item in range(1, 100)]
print(arr)

#choosing random number to make entire array random accordingly
a = random.randint(1, 2)
new_arr = []
#keep odd numbers
if a==1:
    for num in arr: 
        # checking condition 
        if num % 2 != 0: 
            new_arr.append(num)

else:
    for num in arr:      
    # checking condition 
        if num % 2 == 0: 
            new_arr.append(num)

x = int(input("Enter number within range 1- 100 to search:- "))
 
# Function call
result = binary_search(new_arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
    print('')
    print(new_arr)
else:
    print("Element is not present in array")
    print('')
    print(new_arr)