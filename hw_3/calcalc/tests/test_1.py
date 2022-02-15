from CalCalc import calculate

def test_1():
    assert abs(100.0 - calculate('1000/10')) < 0.001
    
def test_2():
    assert calculate('How many ounces are in a gallon', True) == '128 fluid ounces' 
    
def test_3():
    expression = '2 + 3 + 6**2'
    eval_answer = float(calculate(expression))
    wolfram_answer = float(calculate(expression, True))
    assert abs(eval_answer - wolfram_answer) < 0.001
    
def test_4():
    # test that 'numpy' works with inf
    assert calculate('np.inf/100') == float('inf')
    
def test_5():
    # test that 'math' works with unit circle area
    area = 'math.pi*1**2'
    assert abs(3.14159 - calculate(area)) < 0.001
