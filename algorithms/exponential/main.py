def decayed_followers(intl_followers, fraction_lost_daily, days):
    remaining_total = intl_followers * ((1-fraction_lost_daily) ** days)
    return remaining_total

