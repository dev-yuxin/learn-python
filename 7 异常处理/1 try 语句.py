def div(output_filepath: str):
    """输入2个数，计算除法，追加写入文件"""
    try:
        # 当代码发生异常时，会抛出一个异常对象。
        # 如果不用 try 包裹将直接终止程序运行
        # 如果用 try 包裹，try 中后面的代码不执行。处理完异常后外面的代码继续执行

        # try 语句及其子句支持嵌套，这里 fw = None 如果不写，发生异常后面代码不执行，那么 finally 里又会发生变量未初始化就使用的异常
        fw = None
        num1 = float(input("请输入被除数："))
        num2 = float(input("请输入除数："))
        result = num1 / num2
        fw = open(output_filepath, "at", encoding="utf-8")
        fw.write(f"{num1} / {num2} = {result}\n")
    # 如果没发生异常则不会进入 except 分支
    # 如果发生异常则按从上到下的顺序只会进入一个 except 分支
    # 最后一般会用一个 Exception 兜底
    # 如果没兜底且发生异常后没有进入任何 except 分支，依然会抛出异常对象并终止程序
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except Exception as e:
        print(e)
    # try 中没发生异常且没有 return 语句才会进入 else
    else:
        print(f"写入{output_filepath}成功")
    # 无论如何都执行（不管 try 中有没有 return 语句，发没发生异常， except 有没有捕获都执行）
    # 一般用于关闭资源
    finally:
        if fw:
            fw.close()
    # try 语句结束后（没发生异常或发生了异常已处理）后面代码继续执行
    print("函数结束")


div("./assets/test.txt")
