# hw_3 README for CalCalc.py


## CalCalc.py evaluates expressions, passed as strings, with either Python's "eval()" utility or with Wolfram Alpha. 


## Usage:
Takes an expression (string) an evaluates it with eval() or with Wolfram Alpha.
Required arguments:
    expression: string, the expression to be evaluated. By default, this is evaluated with eval().
Optional arguments:
    wolfram_boolean (default=False): if True, evaluate the expression with Wolfram Alpha. 
    return_float (default=True): if True, convert the output from Wolfram Alpha to a float.
    
Example usage:
To evaluate with eval(), 
```bash
    $ python CalCalc.py -s '34*28'
    952
```
To evaluate with Wolfram, 
```bash
    $ python CalCalc.py -w '34*28'
    952.0
    $ python CalCalc.py -w 'mass of the moon in kg'
    7.3459e+22
```
    
or
    
To evaluate with eval(),
```bash
    $ python
```
```python
    >>> from CalCalc import calculate
    >>> calculate('34*28')
    952
```
To evaluate with Wolfram,
```bash
    $ python
```
```python
    >>> from CalCalc import calculate
    >>> calculate('34*28', wolfram_boolean=True)
    952.0
    >>> calculate('mass of the moon in kg', wolfram_boolean=True, return_float=False)
    'about 7.3459 times 10 to the 22 kilograms'
```
