from symbol_table import SymbolTable

st = SymbolTable()

st.add_symbol("x", "int", "global", 10)
st.add_symbol("price", "float", "global", 99.5)
st.add_symbol("name", "string", "global", "ZaraLang")
st.add_symbol("nums", "array", "global")
st.add_symbol("stack1", "stack", "global")

st.display()
