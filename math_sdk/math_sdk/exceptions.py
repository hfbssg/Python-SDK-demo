class MathSdkError(Exception):
    """SDK基础异常类"""
    pass

class DivisionByZeroError(MathSdkError):
    """除零异常"""
    pass