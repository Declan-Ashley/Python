#Boolean in Python

#tells the data type
type(15.00)


#def are_you_sad(is_rainy, has_umbrella):
#    if is_rainy == True and has_umbrella == False:
#        return True
#    else:
#        return False
#^^The above function is simplified below

def are_you_sad(is_rainy, has_umbrella):
    #returns True if is_rainy IS True AND has_umbrella IS False
    return is_rainy and not has_umbrella


#Exercise
def c_greater_than_d_plus_e(c, d, e):
    #returns True if c IS greater, False if NOT greater
    return c > d + e
