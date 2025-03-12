class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = sum(nums)
        return self.div(s, len(nums))

# Пример использования
if __name__ == "__main__":
    calc = Calculator()

    num1 = int(input('First number:'))
    num2 = int(input('Second number:'))
    nums = [num1, num2]
    print(f"Addition: {calc.add(num1, num2)}")
    print(f"Subtraction: {calc.subtract(num1, num2)}")
    print(f"Multiplication: {calc.multiply(num1, num2)}")
    print(f"Division: {calc.divide(num1, num2)}")
    #print(f"Average: {calc.avg([num1, num2])}") # or print(f"Average: {calc.avg(nums)}")