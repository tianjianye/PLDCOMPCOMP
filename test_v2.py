import subprocess
import os
import filecmp
from os.path import basename

def createFolder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	pass
def writeIn(filename,contents):
	f=open(filename,"w+")
	f.write(str(contents))
	f.close()
	pass
def writeTexte(file,nomOut,nomOutTexte,nomReturnTexte):
	#output
	cheminOut="./tests/results/"+str(file)
	cheminOutput=cheminOut+"/out/"
	cmdOut=cheminOut+"/"+str(file)+"."+nomOut
	fileOutput=cheminOutput+str(file)+"_"+nomOutTexte+".txt"
	subprocess.call([cmdOut+" >"+fileOutput],shell=True)
	#return
	ret=subprocess.call(cmdOut)
	fileReturn=cheminOutput+str(file)+"_"+nomReturnTexte+".txt"
	writeIn(fileReturn,ret)

def execution1(file,filename):
	os.system("mkdir -p ./tests/results/"+str(file)+"/out")
	subprocess.call(["gcc", "./tests/"+str(filename), "-o","./tests/results/"+str(file)+"/"+str(file)+".out1"])
	writeTexte(file,"out1","output1","return1")
	pass
def execution2(file,filename):
	os.system("make test file="+str(file))
	writeTexte(file,"out2","output2","return2")
	pass
def compare(file):
	chemin="./tests/results/"+str(file)+"/out/"
	texteOutput1=chemin+str(file)+"_output1.txt"
	texteOutput2=chemin+str(file)+"_output2.txt"
	texteReturn1=chemin+str(file)+"_return1.txt"
	texteReturn2=chemin+str(file)+"_return2.txt"
	result1=filecmp.cmp(texteOutput1,texteOutput2)
	result2=filecmp.cmp(texteReturn1,texteReturn2)
	return(result1 and result2)
#delete exist folder
os.system("rm -rf ./tests/results")
os.system("mkdir -p ./tests/results")
list_in_tests = os.listdir("./tests/")
#makefile	
os.system("make clean")
os.system("make")
for name in list_in_tests:
	if name[-2:] == '.c':
		#file=test
		base=os.path.basename(name)
		file=os.path.splitext(base)[0]
		execution1(file,name)
		execution2(file,name)
		coherence=compare(file)
		print(str(file)+".c: "+str(coherence))
	else:
		pass

