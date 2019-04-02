import subprocess
import os
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
def execution1(file,filename):
	os.chdir("./tests/")
	subprocess.call(["gcc", str(filename), "-o","./results/"+str(file)+"/"+str(file)+".out1"])
	os.chdir("./results/")
	#output
	cmdOut="./"+str(file)+"/"+str(file)+".out1"
	fileOutput1="./"+str(file)+"/out/"+str(file)+"_output1.txt"
	subprocess.call([cmdOut+" >"+fileOutput1],shell=True)
	#return
	ret=subprocess.call(cmdOut)
	fileReturn1="./"+str(file)+"/out/"+str(file)+"_return1.txt"
	writeIn(fileReturn1,ret)
	os.chdir("./../..")
	pass
def execution2(file,filename):
	subprocess.call(["./Main.exe", "./tests/"+str(filename)])
	os.chdir("./tests/results/"+str(file))
	subprocess.call(["as","-o",str(file)+".o",str(file)+".s"])
	subprocess.call(["gcc",str(file)+".o","-o",str(file)+".out2"])
	#output
	cmdOut2="./"+str(file)+".out2"
	fileOutput2="./out/"+str(file)+"_output2.txt"
	subprocess.call([cmdOut2+" >"+fileOutput2],shell=True)
	#return
	ret2=subprocess.call(cmdOut2)
	fileReturn2="./out/"+str(file)+"_return2.txt"
	writeIn(fileReturn2,ret2)
	os.chdir("./../..")
	pass
def comparaison(texte1,texte2):
	f1=open(texte1,"r")
	f2=open(texte2,"r")
	for line1 in f1:
		for line2 in f2:
			if line1!=line2:
				f1.close()
				f2.close()
				return "false"
			else:
				pass
	f1.close()
	f2.close()
	return "true"

def compare(file):
	texteOutput1=str(file)+"_output1.txt"
	texteOutput2=str(file)+"_output2.txt"
	texteReturn1=str(file)+"_return1.txt"
	texteReturn2=str(file)+"_return2.txt"
	result1=comparaison(texteOutput1,texteOutput2)
	result2=comparaison(texteReturn1,texteReturn2)
	if str(result1)=="true" and str(result2)=="true":
		flag="true"
	else:
		flag="false"
	return flag
#delete exist folder
os.system("rm -rf ./tests/results")
#create folder
createFolder("tests/results")
list_in_tests = os.listdir("./tests/")
#makefile	
os.system("make clean")
os.system("make")
for name in list_in_tests:
	if name[-2:] == '.c':
		#file=test
		base=os.path.basename(name)
		file=os.path.splitext(base)[0]
		#creer sous-folder "test" et "out"
		createFolder("tests/results/"+str(file))
		createFolder("tests/results/"+str(file)+"/out")
		execution1(file,name)
		execution2(file,name)
		os.chdir("./results/"+str(file)+"/out")
		coherence=compare(file)
		print(str(file)+".c: "+str(coherence))
		os.chdir("./../../../..")
	else:
		pass

