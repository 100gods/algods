def increasingTriplet(nums) -> bool:
    if len(nums) < 3:
        return False
    left_min = [False for i in range(len(nums))]
    min_num = nums[0]
    for i in range(len(nums)):
        if nums[i] > min_num:
            left_min[i] = True
        else:
            min_num = nums[i]
    max_num = nums[len(nums) - 1]
    print(left_min)
    for i in range(len(nums) - 2, -1, -1):
        print(nums[i],max_num,left_min[i])
        if nums[i] < max_num and left_min[i]:
            return True
        elif nums[i] > max_num:
            max_num = nums[i]
    return False

print(increasingTriplet([20,100,10,12,5,13]))