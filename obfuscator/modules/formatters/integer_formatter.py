import random
from pygments.formatter import Formatter
from pygments.token import Token


class IntegerFormatter(Formatter):
    XOR_RATE = 0.7
    ADD_RATE = 0.7
    SUB_RATE = 0.7

    def format(self, tokensource, outfile):
        for ttype, value in tokensource:
            if ttype == Token.Literal.Number.Integer:
                outfile.write(self.xor_transformation(value))
            else:
                outfile.write(value)

    def xor_transformation(self, value):
        if random.random() > self.XOR_RATE:
            int_val = int(value)
            op_1 = random.randint(0, int_val)
            op_2 = int_val ^ op_1
            op_1 = self.add_transformation(op_1)
            op_2 = self.add_transformation(op_2)
            return "({} XOR {})".format(op_1, op_2)
        else:
            return self.add_transformation(value)

    def add_transformation(self, value):
        if random.random() > self.ADD_RATE:
            int_val = int(value)
            op_1 = random.randint(0, int_val)
            op_2 = int_val - op_1
            op_1 = self.sub_transformation(op_1)
            op_2 = self.sub_transformation(op_2)
            return "({} + {})".format(op_1, op_2)
        else:
            return self.sub_transformation(value)

    def sub_transformation(self, value):
        if random.random() > self.SUB_RATE:
            int_val = int(value)
            op_1 = random.randint(0, int_val)
            op_2 = int_val + op_1
            return "({} - {})".format(op_2, op_1)
        else:
            return value


