class file_manager:
	
	def __init__(self):
		self.root = folder()
		self.lfol = [self.root]
		self.lfile = []
	
	def create_fm(self):
		print "THE ROOT NODE !!"
		self.root.set_name()
