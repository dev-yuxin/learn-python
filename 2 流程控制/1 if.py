# 单分支
year = int(input("请输入年份"))
day_of_year = 365
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    day_of_year += 1
# 这一条没有缩进，不归分支管，不管分支走哪一条最后都会走到这一条
print(f"{year}年有{day_of_year}天")

# 双分支
num = int(input("请输入一个整数"))
if num % 2 == 1:
    print(f"{num}是奇数")
else:
    print(f"{num}是偶数")

# 多分支
score = int(input("请输入成绩（0~100）"))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

"""
输入  输出
2    2的倍数
3    3的倍数
5    5的倍数
9    9的倍数
15   3的倍数 5的倍数
30   2的倍数 3的倍数 5的倍数   
"""
num = int(input("输入一个正整数"))
if num % 2 == 0:
    print("2的倍数", end=" ")
if num % 3 == 0:
    print("3的倍数", end=" ")
if num % 5 == 0:
    print("5的倍数", end=" ")
print()
