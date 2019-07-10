class Document:
	def __init__(self, path: str):
		with open(path, 'r') as f:
			self.code = f.read()

	def store(self, path: str):
		with open(path, 'w') as f:
			f.write(self.code)