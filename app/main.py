def greeting(name: str) -> str:
    return f"Hello,{name}!"


# 如果当前这个模块是被“直接运行”的，就执行下面代码。
# 以后如果别的 Python 文件：import app.main，下面的print()就不会自动执行。
if __name__ == "__main__":
    print(greeting("Agent Developer"))