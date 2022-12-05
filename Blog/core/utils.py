def apply_likes_count(food):
    food.likes_count = food.foodlike_set.count()
    return food


def apply_user_liked_food(food):
    food.is_liked_by_user = food.likes_count > 0
    return food


