# Simple test for week 9 class table and inheritance
from importlib import util

spec = util.spec_from_file_location('class_table', 'week 9/class_table.py')
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

ct = mod.ClassTable()
ct.add_class('Animal')
ct.add_class('Dog', parent='Animal')

print('Classes in table:', list(ct.classes.keys()))
print('Dog inherits from Animal?', ct.check_inheritance('Dog', 'Animal'))

# add methods and fields
ct.get_class('Animal').add_method('speak', 'void')
ct.get_class('Dog').add_field('breed', 'string')
print('Animal methods:', ct.get_class('Animal').methods)
print('Dog fields:', ct.get_class('Dog').fields)
