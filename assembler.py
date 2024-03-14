###
#IMPORTS
import sys
import argparse
###

###
# #utils_lib.py
HEADER='\033[95m'
BLUE='\033[94m'
CYAN='\033[96m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
CLEAR='\033[0m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
###

tokens = {
    "add": ["00", "xx", "xx", "00"], 
    "sub": ["00", "xx", "xx", "01"],
    "sll": ["00", "xx", "xx", "10"],
    "and": ["00", "xx", "xx", "11"],
    "sw": ["01", "xx", "xx", "xx"], # I type
    "lw": ["10", "xx", "xx", "xx"], #I type
    "addi": ["11", "xx", "xx", "xx"], #I type
    "%s0": "00",
    "%s1": "01",
    "%s2": "10",
    "%s3": "11",
}

r_type_ins = ("add", "sub", "sll", "and")
i_type_ins = ("sw", "lw", "addi")
regs = ("%s0","%s1","%s2","%s3")

def assemble(fname, unsafe):
    writeCode = ""
    
    with open(fname) as f:
        text_input = f.read().splitlines()

    for i in text_input:
        linetok = [t2.replace(",", "") for t2 in[t1.lower() for t1 in i.split(" ")]]
        curline = ""
        if linetok[0] in r_type_ins:
            try:
                curline = tokens[linetok[0]][0] + tokens[linetok[1]] + tokens[linetok[2]] + tokens[linetok[0]][3]
            except:
                print(RED + "Error: Could not procces line: " + linetok + CLEAR)
                print(RED + "Exiting." + CLEAR)
                sys.exit()
        elif linetok[0] in i_type_ins:
            try:
                curline = tokens[linetok[0]][0] + tokens[linetok[1]] + tokens[linetok[2]] + f'{int(linetok[3]):08b}'[-2:0] #4th element is the immidiate value turned to 8 bit binary, and then the last 2 bits of it.
            except:
                print(RED + "Error: Could not procces line: " + linetok + CLEAR)
                print(RED + "Exiting." + CLEAR)
                sys.exit()
        else:
            if unsafe:
                print(YELLOW + "Skipping instruction: " + linetok[0] +". Could not proccess" + CLEAR)
                break
            else:
                print(RED + "Error: Could not procces instruction: " + linetok[0] + CLEAR)
                print(RED + "Exiting. Use --unsafe to ignore invalid instructions." + CLEAR)
                sys.exit()
        writeCode = writeCode + curline + "\n"
    ####End for i in text_input
    with open("bin.out", "w") as w:
        w.write(writeCode)


def main():
    #args = parser.parse_args()
    args = sys.argv
    if len(args) < 2:
        print(RED + "Usage: assembler.py [filename]" + CLEAR)
        sys.exit()
    if "--unsafe" in args:
        assemble(args[1], True)
    else:
        assemble(args[1], False)

if __name__ == "__main__":
    main()