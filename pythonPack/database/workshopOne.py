

def bin_cart(set_u, set_v):
    cartesian_product = {(a, b) for a in set_u for b in set_v}
    return  cartesian_product

def bin_concat (set_l0, set_l1):
    binary_concatenation = set()
    for n in set_l0:
        for x in set_l1:
            binary_concatenation.add(n + x)
    return  binary_concatenation

def bin_concat_variation (set_l0, set_l1):
    return set(map(lambda x: x[0] + x[1], bin_cart(set_l0, set_l1)))