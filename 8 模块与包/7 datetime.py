# 第1个datetime是模块名，第2个datetime是类名
from datetime import datetime, timedelta

# 创建一个当前时间的 datetime 对象
dt = datetime.now()
print(dt, type(dt))

# 创建一个指定时间的 datetime 对象
dt = datetime(year=2026, month=1, day=1, hour=10, minute=10, second=10)
print(dt, type(dt))

# datetime => 时间字符串
# %Y 4位年，2026
# %m 2位月（01~12）
# %d 2位日（01~31）
# %H 24小时制的2位小时（00~23）
# %M 2位分钟（00~59）
# %S 2位秒（00~59）
# %A 星期 如 Sunday
# %a 星期 如 Sun
dt_str = dt.strftime('%Y-%m-%d %H:%M:%S %a')
print(dt_str, type(dt_str))

# 时间字符串 => datetime
dt = datetime.strptime('2026-01-01 12:32:08', '%Y-%m-%d %H:%M:%S')
print(dt, type(dt))

# datetime => 时间戳（距离1970-1-1 0:0:0的ms值，float类型，精确到ns）
timestamp = dt.timestamp()
print(timestamp, type(timestamp))

# 时间戳 => datetime
dt = datetime.fromtimestamp(1111111111.11)
print(dt, type(dt))

# datetime 对象拆成 date 对象和 time 对象
date1 = dt.date()
print(date1, type(date1))
time1 = dt.time()
print(time1, type(time1))

# datetime 对象可以获取年,月,日,星期几,时,分,秒
# date 对象只能获取年,月,日,星期几,
# time 对象只能拿到时,分,秒
print(dt.year)
print(dt.month)
print(dt.day)
# weekday(): 0=周一, 1=周二, ..., 6=周日
# isoweekday(): 1=周一, 2=周二, ..., 7=周日
print(dt.weekday())
print(dt.isoweekday())
print(dt.hour)
print(dt.minute)
print(dt.second)

# 两个 datetime 对象相减得到 timedelta 对象
dt1 = datetime(2026, 6, 1)
dt2 = datetime(2027, 1, 1)
td = dt2 - dt1
print(td, type(td))

# datetime 对象 + timedelta 对象
dt2 = dt1 + timedelta(100)
print(dt2, type(dt2))
