from codegen import CodeGenerator

tac = [
    "t1 = x - 1",
    "x = t1"
]

cg = CodeGenerator()
cg.generate(tac)
cg.display()
