class Register:
    def __init__(self):
        self.value
    
    def read(self):
        return self.value
    
    def write(self, new_value):
        self.value = new_value

class Memory:
    def __init__(self, size=8):
        self.registers = [0] * size

    def read(self, reg_num):
        return self.registers[reg_num]

    def write(self, reg_num, value):
        self.registers[reg_num] = value