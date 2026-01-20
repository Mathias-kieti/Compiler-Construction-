# Simple test for week 6 intermediate code
from importlib import util

spec = util.spec_from_file_location('intermediate_code', 'week 6/intermediate_code.py')
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

ic = mod.IntermediateCode()
print('Translating simple expression ["x","+","2"]')
t = ic.translate_expression(['x', '+', '2'])
print('Generated temp:', t)
print('Intermediate code:')
ic.display()
