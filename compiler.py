import sys, os, re

file= """
int main() {
    return 2;
}"""

tokens = ['{', '}', r'\(', r'\)', ';', "int", "return", r'[a-zA-Z]\w*', '[0-9]+']

p = re.compile(fr"\s*({'|'.join(tokens)})")
 
def tokenize(w, pattern):
    index = 0
    m = pattern.match(w, index)
    o = []

    while m and index != m.end():
        o.append(m.group(1))
        index = m.end()
        m = pattern.match(w, index)
    return o
 
prog = tokenize(file, p)
print(prog)

# type exp = Const(int)
# type statement = Return(exp)
# type fun_decl = Fun(string, statement)
# type prog = Prog(fun_decl)