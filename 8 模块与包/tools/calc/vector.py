def add(vec1, vec2):
    """向量加法"""
    return tuple(val1 + val2 for val1, val2 in zip(vec1, vec2))


def mul(vec1, vec2):
    """向量乘法"""
    sum_val = 0
    for val1, val2 in zip(vec1, vec2):
        sum_val += val1 * val2
    return sum_val
