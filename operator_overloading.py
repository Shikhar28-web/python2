class SimpleCalculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return SimpleCalculator(self.value + other.value)

    def __sub__(self, other):
        return SimpleCalculator(self.value - other.value)

    def __mul__(self, other):
        return SimpleCalculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return SimpleCalculator(self.value / other.value)
        else:
            raise ValueError("Cannot divide by zero")

    def __str__(self):
        return f"Result: {self.value}"

# Example usage
calc1 = SimpleCalculator(10)
calc2 = SimpleCalculator(3)
result = (calc1 + calc2 - SimpleCalculator(2)) * SimpleCalculator(4) / SimpleCalculator(2)
print(result)  # Output: Result: 22.0
