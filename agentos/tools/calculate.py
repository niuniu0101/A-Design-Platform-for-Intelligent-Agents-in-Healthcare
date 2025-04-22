
class calculator:
    def __init__(self):
        pass

    def run(self,expression:str):
        """
        calculator:A basic calculator function that takes a mathematical expression as a string and returns the result of the calculation.

        Args:
            expression (str): The mathematical expression you want to calculate.
        """
        try:
            result = eval(expression)
        except Exception as e:
            return f"错误: {e}"
        
        return result
    