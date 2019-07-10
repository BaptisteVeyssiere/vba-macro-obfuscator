from obfuscator.modules.randomizer import Randomizer
from obfuscator.modules.string_obfuscator import StringObfuscator
from obfuscator.modules.trimmer import Trimmer
from .document import Document


class Obfuscator:
    def __init__(self, script: Document):
        self.script = script

    def obfuscate(self):
        self.obfuscate_strings()
        self.trim_document()
        self.randomise_names()
        print(self.script.code)

    def obfuscate_strings(self):
        obfuscator = StringObfuscator(self.script)
        obfuscator.run()

    def trim_document(self):
        trimmer = Trimmer(self.script)
        trimmer.run()
        
    def randomise_names(self):
        randomizer = Randomizer(self.script)
        randomizer.run()
