from .exceptions import DivisionByZeroError

class MathOperations:
    """数学运算核心类"""
    
    def __init__(self, logger=None):
        self.logger = logger
    
    def add(self, a, b):
        """加法运算"""
        result = a + b
        if self.logger:
            self.logger.info(f"Adding {a} and {b}: {result}")
        return result
    
    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        if self.logger:
            self.logger.info(f"Subtracting {b} from {a}: {result}")
        return result
    
    def multiply(self, a, b):
        """乘法运算"""
        result = a * b
        if self.logger:
            self.logger.info(f"Multiplying {a} and {b}: {result}")
        return result
    
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        
        result = a / b
        if self.logger:
            self.logger.info(f"Dividing {a} by {b}: {result}")
        return result
    
    def power(self, base, exponent):
        """幂运算"""
        result = base ** exponent
        if self.logger:
            self.logger.info(f"Raising {base} to power {exponent}: {result}")
        return result