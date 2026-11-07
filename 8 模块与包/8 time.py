import time
from datetime import datetime

# 暂停3s，同步操作
time.sleep(3)

# 获取当前时间戳
print(datetime.now().timestamp())
print(time.time())
