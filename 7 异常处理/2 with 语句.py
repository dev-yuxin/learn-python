def div(output_filepath: str):
    try:
        # with 能够自动关闭资源，不用手动写 finally
        with open(output_filepath, "at", encoding="utf-8") as f:
            num1 = float(input("请输入被除数："))
            num2 = float(input("请输入除数："))
            result = num1 / num2
            f.write(f"{num1} / {num2} = {result}\n")
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
    else:
        print(f"写入{output_filepath}成功")
    print("函数结束")


div("./assets/test.txt")
