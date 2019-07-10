import random
import re
import string
from pygments import highlight
from pygments.lexers.dotnet import VbNetLexer

from obfuscator.modules.formatters.variable_names_formatter import VariableNamesFormatter


class Randomizer:
    def __init__(self, script):
        self.script = script
        self.rand = {}

    def run(self):
        self.map_variable_names_to_random_names()
        formatter = VariableNamesFormatter(self.rand)
        self.script.code = highlight(self.script.code, VbNetLexer(), formatter)

    def map_variable_names_to_random_names(self):
        functions = re.finditer("(Function|Sub)[ ]+(\w+)\(", self.script.code)
        for function_name in functions:
            self.rand[function_name.group(2)] = ''.join(
                random.choice(string.ascii_letters) for _ in range(random.randint(12, 15)))
        parameters = re.finditer("(?:Function|Sub)[ ]+\w+\(((?:\w+[ ]+As[ ]+\w+(?:, )*)*)\)", self.script.code)
        for parameter in parameters:
            parameter_names = re.finditer("(?:(\w+)[ ]+As[ ]+\w+(?:, )*)", self.script.code)
            for parameter_name in parameter_names:
                print("parameter found: " + parameter_name.group(1))
                self.rand[parameter_name.group(1)] = ''.join(
                    random.choice(string.ascii_letters) for _ in range(random.randint(12, 15)))
        variables = re.finditer("^\s*(Dim|Set)[ ]+(\w+)", self.script.code, flags=re.MULTILINE)
        for variable_name in variables:
            self.rand[variable_name.group(2)] = ''.join(
                random.choice(string.ascii_letters) for _ in range(random.randint(12, 15)))
