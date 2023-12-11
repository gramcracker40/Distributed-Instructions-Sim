class ALU:
    def execute(self, operation, value1, value2) -> int:
        # Addition
        if operation == "ADD":
            return value1 + value2

        # Subtraction
        if operation == "SUB":
            return value1 - value2

        # Multiplication
        if operation == "MUL":
            return value1 * value2

        # Division
        if operation == "DIV":
            return value1 / value2

        # Absolute Subtraction
        if operation == "ASUB":
            return abs(value1 - value2)