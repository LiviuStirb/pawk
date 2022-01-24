import sys
from typing import List


def arg_param_value(i):
    if i < len(sys.argv):
        return sys.argv[i]
    else:
        return ""


def parse_params():
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith('-'):
            i += 1
            args[arg] = arg_param_value(i)
        else:
            inputs.append(sys.argv[i])
        i += 1


def code():
    if '-f' in args:
        with open(args['-f'], "r") as f:
            return f.readlines()
    else:
        return inputs.pop(0)  # removes first element from the list


def process_file():
    FNR = 0
    with open(FILENAME, "r") as file:
        for line in file:
            process_line(FNR, line)


def process_stdin():
    global  NR
    FNR = 0
    for line in sys.stdin:
        process_line(FNR, line)

def process_line(FNR, line):
    line = line.strip()
    if len(line) == 0:
        return
    global NR
    if FS == '':
        fields: List[str] = line.split()
    else:
        fields = line.split(FS)
    NF = len(fields)
    FNR += 1
    NR += 1
    exec(code)


args = {}
inputs = []
parse_params()
code = code()
NR = 0
FS = ''
if '-F' in args: FS = args['-F']

begin_code = ''
if '-BEGIN' in args: begin_code = args['-BEGIN']
end_code = ''
if '-END' in args: end_code = args['-END']

exec(begin_code)
if not inputs:
    process_stdin()
else:
    for FILENAME in inputs:
       process_file()
exec(end_code)
