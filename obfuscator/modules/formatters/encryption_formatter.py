import random

from obfuscator.modules.formatters.string_formatter import StringFormatter


class EncryptionFormatter(StringFormatter):
    DECRYPT_VBA = """
Private Function decrypt(ciphertext As Variant, key As Variant)
    Dim plaintext As String
    plaintext = ""
    
    For i = LBound(ciphertext) To UBound(ciphertext)
        plaintext = plaintext & Chr(key(i) Xor ciphertext(i))
    Next
    decrypt = plaintext
End Function
"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def _obfuscate_string(self, value: str) -> str:
        key = [random.randint(0, 255) for _ in range(len(value))]
        cipher_values = ','.join("{0}".format(ord(value[i]) ^ key[i]) for i in range(len(key)))
        self.keys += key
        key_values = ','.join("{0}".format(key[i]) for i in range(len(key)))
        return "decrypt(Array({}),Array({}))".format(cipher_values, key_values)

    def _run_on_string(self, s: str):
        return self._obfuscate_string(s)
