#import api call code
from env import instructions
# from env import opcodes
from register import Register
from alu import ALU
import re

class CPU:
    def __init__(self, num_registers) -> None:
        self.registers = [Register() for _ in range(num_registers)]
        self.alu = ALU()

    def parse_instruction(self) -> None:
        for instruction in instructions:
            parts = instruction.split()
            opcode = parts[0]
            operands = parts[1:]
            # print("LINE: " + str(line))
            # print("PARTS: " + str(parts))
            # print("OPCODE: " + str(opcode))
            # print("OPERANDS: " + str(operands))

            # self.execute_instruction(opcode, operands)
            if opcode == "LOAD":
                self.load(operands[0], operands[1])
            elif opcode == "STORE":
                # Calculate register indecies for rgb
                rgb_regs = operands[0].split(',')
                xy_regs = operands[1].split(',')

                rgb = []
                for register in rgb_regs:
                    index = self.extract_index(register)
                    value = self.registers[index].read()
                    rgb.append(value)
                
                xy = []
                for register in xy_regs:
                    index = self.extract_index(register)
                    value = self.registers[index].read()
                    xy.append(value)

                return {"user_id": 1, "image_id": 37, "rgb": rgb, "xy": xy}
            else:
                # Obtain registers and their values
                r1 = self.extract_index(operands[0])
                r2 = self.extract_index(operands[1])
                value1 = self.registers[r1].read()
                value2 = self.registers[r2].read()

                # Calculate the result using the ALU
                result = self.alu.execute(opcode, value1, value2)
                
                # Store the result back into the first operand register
                self.registers[r1].write(result)

    # def execute_instruction(self, opcode, operands):
        
    
    def load(self, register, value):
        r = self.extract_index(register)

        self.registers[r].write(int(value))

    def read(self, register):
        r = self.extract_index(register)
        return self.registers[r].read()
    
    def extract_index(self, reg_str):
        # Regular expression pattern to match the numbers after "R"
        pattern = r'R(\d+)'
        index = 0

        # Extract numbers from each string
        match = re.search(pattern, reg_str)
        if match:
            index = int(match.group(1))
        else:
            print(f"ERROR: Register: {reg_str}, No match found")

        return index