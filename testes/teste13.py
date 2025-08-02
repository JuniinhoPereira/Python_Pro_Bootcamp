import random


# 1st Option
friends = ["Alice", "Bob", "Charlie"]
friend = random.choice(friends)
print(friend)

# 2nd Option
random_index = random.randint(0, 2)
print(friends[random_index])
