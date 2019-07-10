import re

from pygments import highlight
from pygments.lexers.dotnet import VbNetLexer

from obfuscator.modules.formatters.comment_formatter import CommentFormatter


class Trimmer:
    def __init__(self, script):
        self.script = script

    def run(self):
        self.remove_indentation()
        self.remove_empty_lines()
        self.remove_comments()

    def remove_indentation(self):
        self.script.code = re.sub(r'^\s*', '', self.script.code, flags=re.MULTILINE)

    def remove_empty_lines(self):
        self.script.code = re.sub(r'^\n', '', self.script.code, flags=re.MULTILINE)

    def remove_comments(self):
        formatter = CommentFormatter()
        self.script.code = highlight(self.script.code, VbNetLexer(), formatter)
