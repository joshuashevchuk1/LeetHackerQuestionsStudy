class TwoDArray:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return TwoDArray([
            [self.a[i][j] + other.a[i][j] for j in range(len(self.a[i]))]
            for i in range(len(self.a))
        ])

    def __mul__(self, other):
        return TwoDArray([
            [self.a[i][j] * other.a[i][j] for j in range(len(self.a[i]))]
            for i in range(len(self.a))
        ])

    def __divmod__(self, other):
        quotient = [
            [self.a[i][j] // other.a[i][j] for j in range(len(self.a[i]))]
            for i in range(len(self.a))
        ]
        remainder = [
            [self.a[i][j] % other.a[i][j] for j in range(len(self.a[i]))]
            for i in range(len(self.a))
        ]
        return (TwoDArray(quotient), TwoDArray(remainder))

    def __repr__(self):
        return f"TwoDArray({self.a})"

ob1 = TwoDArray([[1],[2,3],[3,4]])
ob2 = TwoDArray([[1],[2,3],[3,4]])

print(ob1+ob2)
