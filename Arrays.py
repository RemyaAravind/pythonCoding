



numbers = [10, 20, 30, 40]    
print(numbers)

print(numbers[0])     # First element
print(numbers[-1])    # Last element

numbers[1] = 25
print(numbers)  # 10,25,20,30,40

numbers.append(50)
numbers.insert(1, 15)

numbers.remove(25)
numbers.pop()        # Removes last item
del numbers[0]       # Removes item at index
del numbers[1:3]   # index 1 and index 2
del numbers         # delete the entire array

for num in numbers:
    print(num)



#Array Module (Fixed type Arrays)
# i for int ,f for float and d for double

    import array

# 'i' means integer
arr = array.array('i', [1, 2, 3, 4])
print(arr[2])


arr.append(5)
arr.insert(2, 100)
arr.remove(3)
print(arr.tolist())  # Convert to list


