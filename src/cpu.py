#import api call code
from env import instructions
from env import opcodes
from register import Register
from alu import ALU

class CPU:
    def __init__(self, num_registers) -> None:
        self.registers = [Register()] * num_registers
        self.alu = ALU()

    def parse_instruction(self) -> None:
        for instruction in instructions:
            parts = instruction.split()
            opcode = parts[0]
            operands = ' '.join(parts[1:])
            # print("LINE: " + str(line))
            # print("PARTS: " + str(parts))
            # print("OPCODE: " + str(opcode))
            # print("OPERANDS: " + str(operands))

            # self.execute_instruction(opcode, operands)
            print("Registers")
            # for register in self.registers:
                # print(register.read())
            

    def execute_instruction(self, opcode, operands):
        if opcode == "LOAD":
            self.load(operands[0])
        
        if opcode == "MOVE":
            self.write(operands[0], operands[1])
        # return {"STORE":[], "xy": []}
    
    def load(self, register):
        print(register)
        return self.registers[int(register[1])].read()
    
    def write(self, register, value):
        self.registers[str(register[1])].write(value)