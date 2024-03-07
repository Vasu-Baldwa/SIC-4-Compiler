###
#IMPORTS
import sys
import utils_lib
###

tokens = {
    "add": "INSTRUCT_ADD",
    "sub": "INSTRUCT_SUB",
    "sll": "INSTRUCT_SLL",
    "and": "INSTRUCT_AND",
    "sw": "INSTRUCT_SW",
    "lw": "INSTRUCT_LW",
    "addi": "INSTRUCT_ADDI",
    "%s0": "REGISTER_S0",
    "%s1": "REGISTER_S1",
    "%s2": "REGISTER_S2",
    "%s3": "REGISTER_S3",
}

def assemble(fname):
    writeCode = ""
    
    with open(fname) as f:
        text_input = f.read().splitlines()

    for i in text_input:
        for j in i.split(" "):
            curTok = j.lower().replace(",", "")
            if curTok in tokens.keys():
                writeCode = writeCode + tokens[curTok]
            else:
                print(utils_lib.print["RED"] + "Error: Could not match token: " + j + utils_lib.print["ENDC"])
        writeCode = writeCode + "\n"

    with open("bin.out", "w") as w:
        w.write(writeCode)


def main():
    args = sys.argv
    if len(args) != 2:
        print(utils_lib.print["RED"] + "Usage: assembler.py [filename]" + utils_lib.print["ENDC"])
    else:
        assemble(args[1])

if __name__ == "__main__":
    main()