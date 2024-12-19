def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0
    count = 0
    add = 0
    for follower in audiences_followers:
        add += follower
        count += 1
    average_audience_follower = add / count
    estimated_spred = average_audience_follower * (count ** 1.2)
    return estimated_spred



