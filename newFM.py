class file_manager:
	
	def __init__(self):
		self.root = folder()
		self.lfol = [self.root]
		self.lfile = []
	
	def create_fm(self):
		print "THE ROOT NODE !!"
		self.root.set_name()
	def create_folder(self):
		temp = folder()
		temp.set_name()
		
		ind = 0
		flag = 1
		dir = raw_input("enter name of folder to be inserted into:")
		for i in range(len(self.lfol)):
			if self.lfol[i].get_name() == dir:
				fold = self.lfol[i]
				fold.add_child(temp)
				temp.parent = fold
				ind = i
				flag = 0
				self.lfol.insert(i,temp)
				break
		
		if flag:
			print "folder not created invalid directory"
	def create_file(self):
		temp = file()
		temp.set_name()
		
		flag = 1

		dir = raw_input("enter name of folder to be inserted into:")

		for i in range(len(self.lfol)):
			if self.lfol[i].get_name() == dir:
				fold = self.lfol[i]
				fold.add_child(temp)
				temp.parent = fold
				flag = 0
				self.lfile.append(temp)
				break
		
		if flag:
			print "file not created"
	