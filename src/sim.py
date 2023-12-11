from cpu import CPU

if __name__ == "__main__":
    cpu = CPU(11)
    store = cpu.parse_instruction()
    print(store)