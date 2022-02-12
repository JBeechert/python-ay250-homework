from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = "Evaluate an expression with either eval() or Wolfram Alpha"
with open("README.md", "r") as readme:
    LONG_DESCRIPTION = readme.read()

setup(name='CalCalc',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",      
      classifiers=['License :: MIT License', 'Programming Language :: Python :: 3.9.10'],       
      author="Jacqueline Beechert",
      author_email="jbeechert56@gmail.com",   
      python_requires=">=3",
      license="MIT",
      py_modules = ["CalCalc"],
      package_dir = {'':'CalCalc'},      
      install_requires = ['argparse', 'pytest', 'numpy']
)
