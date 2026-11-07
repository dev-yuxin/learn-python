"""
依次输入年月日（保证是整数）
先输入年，合法才继续，不合法就提示
再输入月，合法才继续，不合法就提示
再输入日，合法才继续，不合法就提示
"""
year = int(input("请输入年"))
if year >= 0:
    month = int(input("请输入月"))
    if 1 <= month <= 12:
        date = int(input("请输入日"))
        days_of_month = 30
        match month:
            case 2:
                days_of_month = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                days_of_month = 31
            case _:
                days_of_month = 30
        if 1 <= date <= days_of_month:
            print(f"{year}年{month}月{date}日")
        else:
            print(f"日期输入错误，1<=日<={days_of_month}")
    else:
        print("月份输入错误，1<=月<=12")
else:
    print("年份输入错误，年>=0")
