# 已知 2026 是马年，输入一个年份，求生肖年
year = int(input("请输入年份（正整数）："))
match year % 12:
    case 0:
        print("猴")
    case 1:
        print("鸡")
    case 2:
        print("狗")
    case 3:
        print("猪")
    case 4:
        print("鼠")
    case 5:
        print("牛")
    case 6:
        print("虎")
    case 7:
        print("兔")
    case 8:
        print("龙")
    case 9:
        print("蛇")
    case 10:
        print("马")
    case 11:
        print("羊")

month = int(input("请输入月份（1~12）"))
match month:
    case 12 | 1 | 2:
        print("冬")
    case 3 | 4 | 5:
        print("春")
    case 6 | 7 | 8:
        print("夏")
    case 9 | 10 | 11:
        print("秋")
    # 兜底
    case _:
        print("输入错误")
