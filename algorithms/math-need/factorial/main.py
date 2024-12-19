def num_possible_orders(num_posts):
    factorial = num_posts
    for _ in range(num_posts - 1):
        num_posts = num_posts -1
        factorial *= num_posts

    return factorial

