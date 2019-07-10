from pygments import highlight
from pygments.lexers.dotnet import VbNetLexer

from obfuscator.modules.formatters.encryption_formatter import EncryptionFormatter
from obfuscator.modules.formatters.integer_formatter import IntegerFormatter


class StringObfuscator():
    def __init__(self, script):
        self.script = script

    def run(self):
        self.encrypt()
        self.hide_integers()

    def encrypt(self):
        formatter = EncryptionFormatter()
        self.script.code = EncryptionFormatter.DECRYPT_VBA + highlight(self.script.code, VbNetLexer(), formatter)

    def hide_integers(self):
        formatter = IntegerFormatter()
        self.script.code = highlight(self.script.code, VbNetLexer(), formatter)

