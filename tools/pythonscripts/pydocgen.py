class DocGen:

	def __init__(self, mod_name):
		self.mod_name = mod_name

        def grab_doc(self):
		from subprocess import Popen, PIPE
                
