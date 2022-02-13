import argparse
import urllib.parse, urllib.request
import numpy as np
import math

def calculate(expression, wolfram_boolean=False, return_float=True):
    """
    Takes an expression (string) an evaluates it with eval() or with Wolfram Alpha.
    Required arguments:
        expression: string, the expression to be evaluated. By default, this is evaluated with eval().
    Optional arguments:
        wolfram_boolean (default=False): if True, evaluate the expression with Wolfram Alpha. 
        return_float (default=True): if True, convert the output from Wolfram Alpha to a float.
    
    Example usage:
    To evaluate with eval(), 
        $ python CalCalc.py -s '34*28'
        952
    To evaluate with Wolfram, 
        $ python CalCalc.py -w '34*28'
        952.0
        $ python CalCalc.py -w 'mass of the moon in kg'
        7.3459e+22
    
    or
    
    To evaluate with eval(),
        $ python
        >>> from CalCalc import calculate
        >>> calculate('34*28')
        952
    To evaluate with Wolfram,
        $ python
        >>> from CalCalc import calculate
        >>> calculate('34*28', wolfram_boolean=True)
        952.0
        >>> calculate('mass of the moon in kg', wolfram_boolean=True, return_float=False)
        'about 7.3459 times 10 to the 22 kilograms'
    """
    
    if wolfram_boolean:
        query = urllib.parse.quote_plus(expression)
        
        # My own Wolfram API
        url = f'http://api.wolframalpha.com/v1/result?appid=HLLE7E-Y7AW7JUR8G&i={query}%3F'

        answer = urllib.request.urlopen(url).read()
        answer = str(answer, 'utf-8')
        
        if return_float:
            if 'times 10 to the' in answer:
                answer = answer.replace(' times 10 to the ', ' e ')
            answer = answer.split(' ')
            new = []
            for x in answer:
                if x.replace('.','',1).isdigit() or x=='e':
                    new.append(x)
            answer = ''.join(str(elem) for elem in new)
            answer = float(answer)
        
    else:
        answer = eval(expression)
        
    return answer   
    

parser = argparse.ArgumentParser(description=
                                 'Evaluate an expression, passed as a string, with eval or Wolfram alpha')

exc = parser.add_mutually_exclusive_group()
exc.add_argument('-s', action='store', dest='expression', 
                    help="Provide an expression ('string') to evaluate. \
                    DON\'T PASS ANYTHING STUPID LIKE rm -r.")

exc.add_argument('-w', action='store', dest='wolfram_input', 
                     help="Provide a query ('string') for Wolfram Alpha to evaluate")

results = parser.parse_args()

if __name__ == '__main__':
    
    if results.expression:
        answer = calculate(results.expression)
        
    elif results.wolfram_input:
        answer = calculate(results.wolfram_input, True)
        
    print(answer)
