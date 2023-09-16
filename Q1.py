class Calculator:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

calculator = Calculator()
result1 = calculator.multiply(2, 3)
result2 = calculator.multiply(2, 3, 4)
result3 = calculator.multiply(2, 3, 4, 5)

print(result1)
print(result2)
print(result3)
