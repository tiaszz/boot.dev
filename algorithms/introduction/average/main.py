def average_followers(nums):
    deno = len(nums)
    sum = 0
    if nums:
        for num in nums:
            sum += num
        average = sum / deno
        return average
    return None
