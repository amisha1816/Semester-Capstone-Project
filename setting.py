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

sell_prices = [1, 1, 4, 6, 8, 11, 12, 14, 16, 18, 21, 1, 24, 1, 28, 1, 32, 1, 36, 1, 1, 42, 44, 1, 1, 51, 1, 54, 1, 1, 60, 1, 1, 66, 1, 71, 1, 1, 1, 78, 81, 1, 84, 86, 1, 91, 1, 1, 96, 81, 10000]
sell_random_select = sell_prices[random.randint(1, 49)]

if self.fm_active:
    SELL_STUFF = {
            'apple': sell_random_select,
            'corn': sell_random_select,
            'tomato': sell_random_select
            }

    BUY_STUFF = {
            'corn_seed': 5, 
            'tomato_seed': 5 
