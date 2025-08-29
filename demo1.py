from math_sdk.math_sdk import MathOperations, DivisionByZeroError

# 创建实例
math = MathOperations()

# 使用各种运算
result = math.add(2, 3)  # 5
result = math.divide(10, 2)  # 5.0
result = math.power(2, 8)  # 256

# 处理异常
try:
    result = math.divide(5, 0)
except DivisionByZeroError as e:
    print(e)  # "Cannot divide by zero"