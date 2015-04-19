class folder:
	
	def __init__(self,name = None):
		self.name = name
		self.parent = None
		self.left = None
		self.right = None
		
	def get_parent(self):
		return self.parent
		
	def get_name(self):
		return self.name
		
	def get_left(self):
		return self.left
		
	def get_right(self):
		return self.right
			
	def set_name(self):
		self.name = raw_input("enter name of folder:")
	
	def set_left(self,ch):
		self.left = ch
	
	def set_right(self,ch):
		self.right = ch
	
	def disp(self):
		print "\n"
		
		print "Name:" + self.name
		
		if not self.parent == None:
			print "Parent:" + self.parent.get_name()
		else:
			print "parent: None"
		
		if not self.left == None:
			print "file nm: " + self.left.get_name()
		else:
			print "file nm: None"
		
		if not self.right == None:
			print "folder nm: " + self.right.get_name()
		else:
			print "folder nm: None"

class file:
	
	def __init__(self,name = None):
		self.name = name
		self.parent = None
		
	def get_name(self):
		return self.name
		
	def set_name(self):
		self.name = raw_input("enter name of file:")
	
	def get_parent(self):
		return self.parent

class file_manager:
	
	def __init__(self):
		self.root = folder()
		self.lfol = [self.root]
		self.lfile = []
	
	def create_fm(self):
		print "THE ROOT NODE !!"
		self.root.set_name()
	def create_file(self):
		temp = file()
		temp.set_name()
		
		flag = 1
		
		dir = raw_input("enter name of folder to be inserted into:")
		
		for i in range(len(self.lfol)):
			if self.lfol[i].get_name() == dir:
				fold = self.lfol[i]
				if not fold.get_left() == None:
					break
				fold.set_left(temp)
				temp.parent = fold
				flag = 0
				self.lfile.append(temp)
				break
		
		if flag:
			print "file not created"
	def create_folder(self):
		temp = folder()
		temp.set_name()
		
		fold = self.lfol[len(self.lfol)-1]
		fold.set_right(temp)
		temp.parent = fold
		self.lfol.append(temp)
	def disp_fm(self):
		print "the list of folders and files "
		for i in range(len(self.lfol)):
			self.lfol[i].disp()
	
	def disp_file(self):
		print "\nthe list of all files"
		for i in range(len(self.lfile)):
			print self.lfile[i].get_name()
