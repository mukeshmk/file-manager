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
