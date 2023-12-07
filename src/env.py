instructions = [
    "LOAD R1 139",
    "LOAD R2 232",
    "LOAD R3 175",
    "LOAD R4 789",
    "LOAD R5 342",
    "LOAD R6 3",
    "ADD R3 R4",
    "ADD R3 R5",
    "DIV R3 R6",
    "STORE (R3,R3,R3) (R1,R2)"
]

opcodes = {
    "LOAD": "1010",
    "ADD": "1011",
    "SUB": "1100",
    "MUL": "1101",
    "DIV": "1110",
    "STORE": "1111",
}