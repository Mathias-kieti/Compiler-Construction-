from optimizer import Optimizer

code = [
    "t1 = 2 + 3",
    "t2 = x - 1",
    "x = t2"
]

opt = Optimizer(code)
opt.constant_folding()
opt.dead_code_elimination()
opt.display()
