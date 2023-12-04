# 4-3. Counting to Twenty:
print(f"numbers from 1 to 20:")
for numbers in range(1, 21, 1):
    print(numbers)

# 4-4. One Million:
#nums = range(1,1000001)
#for nums in nums:
    #print(nums)

# 4-5. Summing a Million:
million = list(range(1,1000001))
first = min(million)
last = max(million)
addition = sum(million)
print(f"min = {first}, max = {last}, sum = {addition}")

# 4-6. Odd Numbers:
print("odds numbers from to 20")
for odd in range(1,21,2):
    print(odd)

# 4-7. Threes:
cubes = range(3,30)
for cube in cubes:
    print(f"cube {cube} equals {cube**3}")

#4-8. Cubes:
cub2s = []
for val in range(1,10):
    cub2 = val ** 3
    cub2s.append(cub2)
    print(cub2)
print(cub2s)
