# hw_3 README for CalCalc.py


## CalCalc.py evaluates expressions, passed as strings, with either Python's "eval()" utility or with Wolfram Alpha. 


## Installation
To install, run
```python
pip install -e .
pip install CalCalc
```

## Usage:
Takes an expression (string) an evaluates it with eval() or with Wolfram Alpha.
Required arguments:
    expression: string, the expression to be evaluated. By default, this is evaluated with eval().
Optional arguments:
    wolfram_boolean (default=False): if True, evaluate the expression with Wolfram Alpha. 
    
To evaluate with eval(), 
```bash
    $ python CalCalc.py -s '34*28'
    952
```
To evaluate with Wolfram, 
```bash
    $ python CalCalc.py -w '34*28'
    952
    $ python CalCalc.py -w 'mass of the moon in kg'
    about 7.3459 times 10 to the 22 kilograms
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
    >>> calculate('34*28', True)
    '952'
    >>> calculate('mass of the moon in kg', True)
    'about 7.3459 times 10 to the 22 kilograms'
```
