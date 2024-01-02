"""
Chapter Two: Arrays

Solutions to the problems

"""

# 1. Create an array that looks like: [1, 4, 6, 7, 9, 10].
solution_array = [1, 4, 6, 7, 9, 10]

# 2. Remove the element 7 from the array you created above.
solution_array.remove(7)  # Or, we can use solution_array.pop(solution_array.index(7))

# 3. Update the element at index 2 to be the integer 3.
solution_array[2] = 3

# 4. Pop the last element from the array and print the result.
result = solution_array.pop()
print(result)  # This will print out 10
