import subprocess
import os
import filecmp
import traceback
from os.path import basename
def execution(file,filename):
	output="./tests/testsFrontEnd/results/"+str(file)+"/"+str(file)+"_output.txt"
	os.system("make testsFrontEnd file="+str(file)+" > "+output)
	out="./tests/testsFrontEnd/results/"+str(file)+"/"+str(file)+".out"
	os.system(out+" >"+output)
	pass
#delete exist folder
os.system("rm -rf ./tests/testsFrontEnd/results")
os.system("mkdir -p ./tests/testsFrontEnd/results")
list_in_tests = os.listdir("./tests/testsFrontEnd/")	
for name in list_in_tests:
	if name[-2:] == '.c':
		#file=test
		base=os.path.basename(name)
		file=os.path.splitext(base)[0]
		print(str(file)+".c:")
		execution(file,name)
		print()
		print()
	else:
		pass

