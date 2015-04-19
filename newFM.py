class folder:
	
	def __init__(self,name = None):
		self.name = name
		self.parent = None
		self.child = []
		
	def get_parent(self):
		return self.parent
	
	def get_nth_child(self,n):
		if (n-1) > len(self.child):
			raise "invalid n !!"
		else:
			return self.child[n-1]
	
	def get_name(self):
		return self.name
		
	def get_all_childs(self):
		return self.child
		
	def set_name(self):
		self.name = raw_input("enter name of folder:")
	
	def add_child(self,ch):
		self.child.append(ch)
		
	def disp(self):
		print "\n"
		
		print "Name:" + self.name
		if not self.parent == None:
			print "Parent:" + self.parent.get_name()
		else:
			print "parent: None"
		for i in range(len(self.child)):
			print "child: " + str(i+1) + " "+ self.child[i].get_name()

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
	def disp_fm(self):
		print "the list of folders and files "
		for i in range(len(self.lfol)-1,-1,-1):
			self.lfol[i].disp()
	
	def disp_file(self):
		print "\nthe list of all files"
		for i in range(len(self.lfile)):
			print self.lfile[i].get_name()
	
