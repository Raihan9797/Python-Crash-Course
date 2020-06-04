### Testing a Function


## passing test
# def get_formatted_name(first, last):
    # """generate a neatly formatted full name"""
    # fullname = first + ' ' + last
    # return fullname.title()


## failing test
# def get_formatted_name(first, mid, last):
    # """generate a neatly formatted full name"""
    # fullname = first + ' ' + mid + ' ' + last
    # return fullname.title()


## resolved failed test
def get_formatted_name(first, last, mid = ''):
    """generate a neatly formatted full name"""
    if mid:
        fullname = first + ' ' + mid + ' ' + last
    else:
        fullname = first + ' ' + last

    return fullname.title()