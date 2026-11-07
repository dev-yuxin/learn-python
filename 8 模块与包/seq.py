_msg2 = "序列"


def add(seq1, seq2):
    """序列的拼接"""
    return seq1 + seq2


def mul(seq, count):
    """序列的重复"""
    return seq * count


print(f"加载{_msg2}模块")

if __name__ == '__main__':
    print(mul((1, 2, 3), 4))
