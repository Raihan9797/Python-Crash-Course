def make_pizza(size, *toppings): # size first, then *toppings
    """summarizes our pizza"""
    print('\nmaking a ' + str(size)
    + '-inch pizza with:')

    for t in toppings:
        print('- ' + t)
