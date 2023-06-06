import random # I thought this could be fun to add!

#setting
# screen variables 
w=1300
h=800
tile_size = 32

OVERLAYER_POSITIONS = {
    'tool' : (35, h),
    'seed': (80,h)
}

LAYERS = { # layers are in level of what is at the bottom to what is on top 
    'ground': 0,
    'House Walls/bottom': 1,
    'Hills': 2,
    'Water': 3,
    'Flowers/trees': 4,
    'Furniture': 5,
    'main': 6
}

APPLE_POSITION= {
    'tree': [(-5,78),(18,17),(50,27),(30,37),(80,47),(90,10)]
}

sell_prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10000]
sell_random_select = sell_prices[randint(0, 10)]

SELL_STUFF = {
        'tree_wood': sell_random_select,
        'apple': sell_random_select,
        'corn': sell_random_select,
        'tomato': sell_random_select
        }

BUY_STUFF = {
        'corn_seed': 5, 
        'tomato_seed': 5 
        }
