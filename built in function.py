nums = [10, 20, 30, 40, 50]
print("Original:", nums)

# Adding and removing elements
nums.append(60)
nums.insert(1, 15)
nums.remove(30)
nums.pop()

print("Modified:", nums)

# Sorting and reversing
nums.sort()
print("Sorted:", nums)

nums.reverse()
print("Reversed:", nums)

# List properties
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

# Copying list
new_list = nums.copy()
print("Copied List:", new_list)

# Clearing list
nums.clear()
print("Cleared List:", nums)
