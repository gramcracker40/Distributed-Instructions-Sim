class ALU:
    def execute(self, operation, operands) -> int:
        # Addition
        if operation == "ADD":
            return operands[0] + operands[1]

        # Subtraction
        if operation == "SUB":
            return operands[0] - operands[1]

        # Multiplication
        if operation == "MUL":
            return operands[0] * operands[1]

        # Division
        if operation == "DIV":
            return operands[0] / operands[1]

        # Absolute Subtraction
        if operation == "ASUB":
            return abs(operands[0] - operands[1])