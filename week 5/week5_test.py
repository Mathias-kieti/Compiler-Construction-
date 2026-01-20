# Simple test for week 5 semantic analyzer
from importlib import util

# load symbol_table
spec_st = util.spec_from_file_location('symbol_table', 'week 1/symbol_table.py')
st_mod = util.module_from_spec(spec_st)
spec_st.loader.exec_module(st_mod)

# load semantic_analyzer
spec_sa = util.spec_from_file_location('semantic_analyzer', 'week 5/semantic_analyzer.py')
sa_mod = util.module_from_spec(spec_sa)
spec_sa.loader.exec_module(sa_mod)

st = st_mod.SymbolTable()
st.add_symbol('x', 'int', 'global', 10)

sa = sa_mod.SemanticAnalyzer(st)
print('Check valid assignment (should pass)')
sa.check_assignment('x', 'int', 'global')
print('OK')

print('Check invalid assignment (should raise Exception)')
try:
    sa.check_assignment('x', 'string', 'global')
except Exception as e:
    print('Caught expected error:', e)
