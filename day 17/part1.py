import time
with open(r"day 17\input.txt", "r") as file:
    data = file.read()
data =  data.split("\n\n")
register, program = data
register = register.split("\n")
a,b,c = int(register[0][register[0].find(":")+1:]), int(register[1][register[1].find(":")+1:]), int(register[2][register[2].find(":")+1:]),

program = [int(x) for x in program.split()[1].split(",")]
print(program)
output = []
pc = 0

def combo_operand(operand):
    global a,b,c
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            return
        case _:
            return operand
        
def perform_opcode(opcode):
    global pc, a, b, c, output
    jump = False
    operand = program[pc+1]
    match opcode:
        case 0:
            a = a//2**combo_operand(operand)
        case 1:
            b = b^operand
        case 2:
            b = combo_operand(operand)%8
        case 3:
            if a == 0:
                pass
            else:
                pc = operand
                jump = True
        case 4:
            b = b^c
        case 5:
            output.append(combo_operand(operand)%8)
        case 6:
            b = a//2**combo_operand(operand)            
        case 7:
            c = a//2**combo_operand(operand)
    if not jump:
        pc+=2
        
while pc<len(program)-1:
    print(program[pc], program[pc+1], pc,output, a, b, c)
    perform_opcode(program[pc])
    
print(",".join([str(x) for x in output]))