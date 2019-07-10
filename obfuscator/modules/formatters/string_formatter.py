from pygments.formatter import Formatter
from pygments.token import Token


class StringFormatter(Formatter):
    def __init__(self, **options):
        super().__init__(**options)
        self.string_carrier = ""
        self.previous_type = ""

    def _run_on_string(self, s: str) -> str:
        raise NotImplementedError()

    def format(self, tokensource, outfile):
        for ttype, value in tokensource:
            if ttype == Token.Literal.String and value != "\"":
                substrings = [value[i:i+15] for i in range(0, len(value), 15)]
                for i in range(len(substrings)):
                    outfile.write(self._run_on_string(substrings[i]))
                    if i < (len(substrings) - 1):
                        outfile.write(" & _\r\n")
            elif value != "\"":
                outfile.write(value)
            if self.string_carrier == "\"" and ttype != Token.Literal.String:
                outfile.write(self.string_carrier)
                self.string_carrier = ""
            self.string_carrier = value if value == "\"" and self.previous_type != Token.Literal.String else ""
            self.previous_type = ttype
