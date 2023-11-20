# Array are mutable

nums = [1, 2, 3, 4, 5]

# Sub array
print(nums[1:4])

# Functions for array

nums.append(6)
print(nums)  # [1,2,3,4,5,6]

# we need to pass two arguments that is (index , what we need to insert)
nums.insert(2, 9)
print(nums)  # [1,2,9,3,4,5,6]

nums.pop()  # remove last element
print(nums)  # [1,2,9,3,4,5]

ans = nums.count(1)  # will return the count of 1 inside the list
print(ans)  # 1

array_length = len(nums)  # to get the array length
print(array_length)  # print the array length i.e = 6

nums.pop(1)  # will remove 1st index value
print(nums)  # [1,9,3,4,5]

# if we want to delete the multiple value use "del"

del nums[2:]  # removes the elements from 2 index to last index
print(nums)  # [1,9]

# if we want to add the multiple value to array use ".extends"

nums.extend([2, 3, 4, 5])
print(nums)  # [1,9,2,3,4,5]

# inbuilt functions  ---------------------------

print(min(nums))  # 1
print(max(nums))  # 9
print(sum(nums))  # 24

nums.sort(reverse=True)  # will sort the array in reverse order
print(nums)
