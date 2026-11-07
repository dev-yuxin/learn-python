# pip install setuptools
from setuptools import setup, find_packages

setup(
    name="tools",  # 打包后的压缩包名称前缀
    version="0.1.0",  # 版本号
    packages=find_packages(),  # 自动识别主包下的所有子包
    python_requires=">=3.12",  # 指定python版本
)

# 控制台运行（注意文件路径） python setup.py sdist
