def median_followers(nums):
    lenght = len(nums)
    sorted_nums = sorted(nums)
    print(sorted_nums)
    if nums:
        if lenght < 2:
            return nums[0]
        elif lenght % 2 != 0:
            lenght = int((lenght / 2))
            median = sorted_nums[lenght]
            return median
        else:
            lenght = int(lenght / 2)
            median = (sorted_nums[lenght - 1] + sorted_nums[lenght]) / 2
            return median
    return None
