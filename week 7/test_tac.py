from tac_generator import TACGenerator

tac = TACGenerator()

t1 = tac.generate_expression("x", "-", "1")
tac.generate_assignment("x", t1)

tac.display()
