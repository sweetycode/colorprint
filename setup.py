import re
import ast
from setuptools import setup

pkg_name = 'colorprint'

with open(pkg_name + '/__init__.py') as f:
    ver = re.search('__version__\s*=\s*(.*)', f.read().decode('utf8')).group(1)
    version = str(ast.literal_eval(ver))

setup(
    name=pkg_name,
    version=version,
    packages=[pkg_name, ]
)
