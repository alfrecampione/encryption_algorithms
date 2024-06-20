def gcd_euclidian_algorithm(a, b):    
    while b != 0:
        a, b = b, a % b    
    return a

def extended_euclidian_algorithm(a, b):    
    if a == 0:
        return b, 0, 1    
    else:
        gcd, x, y = extended_euclidian_algorithm(b % a, a)        
        return gcd, y - (b // a) * x, x