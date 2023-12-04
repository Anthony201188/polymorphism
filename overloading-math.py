class MathOperations:
    def add(slef, *args):
        return sum(args)
        

    def subtract(self, *args):
      for index, num in enumerate(args): # subtracts the next number in the sequence from the one before
        result = num - args[index+1]
        return result

    # def multiply(....): ## not completed yet
    #     pass
    
def main():
    math_ops = MathOperations()

    # Addition
    result = math_ops.add(2, 3)
    print(f"Addition Result: {result}")

    result = math_ops.add(4, 6, 8)
    print(f"Addition Result: {result}")

    # Subtraction
    result = math_ops.subtract(10, 3)
    print(f"Subtraction Result: {result}")

    result = math_ops.subtract(20, 5, 3)
    print(f"Subtraction Result: {result}")

    # # Multiplication
    # result = math_ops.multiply(2, 5)
    # print(f"Multiplication Result: {result}")

    # result = math_ops.multiply(3, 4, 2)
    # print(f"Multiplication Result: {result}")


main()