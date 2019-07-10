from pygments.formatter import Formatter
from pygments.token import Token


class CommentFormatter(Formatter):
    def format(self, tokensource, outfile):
        for ttype, value in tokensource:
            if ttype != Token.Comment:
                outfile.write(value)
