import sys
import importlib.util

# Load modules from folders with spaces in names
lexer_spec = importlib.util.spec_from_file_location("lexer", "week 2/lexer.py")
lexer = importlib.util.module_from_spec(lexer_spec)
lexer_spec.loader.exec_module(lexer)

tac_spec = importlib.util.spec_from_file_location("tac_generator", "week 7/tac_generator.py")
tac_module = importlib.util.module_from_spec(tac_spec)
tac_spec.loader.exec_module(tac_module)

opt_spec = importlib.util.spec_from_file_location("optimizer", "week 8/optimizer.py")
opt_module = importlib.util.module_from_spec(opt_spec)
opt_spec.loader.exec_module(opt_module)

cg_spec = importlib.util.spec_from_file_location("codegen", "week 10/codegen.py")
cg_module = importlib.util.module_from_spec(cg_spec)
cg_spec.loader.exec_module(cg_module)

tokenize = lexer.tokenize
TACGenerator = tac_module.TACGenerator
Optimizer = opt_module.Optimizer
CodeGenerator = cg_module.CodeGenerator

code = """
int x = 5;
x = x - 1;
"""

print("===== SOURCE CODE =====")
print(code)

print("\n===== TOKENS =====")
tokens = tokenize(code)
for t in tokens:
    print(t)

print("\n===== THREE ADDRESS CODE =====")
tac = TACGenerator()
t1 = tac.generate_expression("x", "-", "1")
tac.generate_assignment("x", t1)
tac.display()

print("\n===== OPTIMIZED CODE =====")
opt = Optimizer(tac.code)
opt.constant_folding()
opt.dead_code_elimination()
opt.display()

print("\n===== MACHINE CODE =====")
cg = CodeGenerator()
cg.generate(opt.code)
cg.display()
