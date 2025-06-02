Implement the CommissionEmployee class with init , earnings, and repr methods. Include
properties for personal details and sales data. Create a test script to instantiate the object, display
earnings, modify sales data, and handle data validation errors for negative values.

Ans:
    class CommissionEmployee:
    def __init__(self, name, sales, rate):
        self.name = name
        self.set_sales(sales)
        self.rate = rate

    def earnings(self):
        return self.sales * self.rate

    def set_sales(self, value):
        if value < 0:
            raise ValueError("Sales cannot be negative")
        self.sales = value

    def __repr__(self):
        return f"{self.name} earned: ${self.earnings()}"

e = CommissionEmployee("Sam", 1000, 0.1)
print(e)
e.set_sales(1500)
print(e)
