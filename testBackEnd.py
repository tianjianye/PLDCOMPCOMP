import subprocess
import os
import filecmp
from os.path import basename

def generate_tr(filename,result,error):
	if result=="failed":
		return'<tr><td>%s</td><td style="color:red">%s</td><td style="color:red">%s</td></tr>'%(filename,result,error)
	return'<tr><td>%s</td><td style="color:green">%s</td><td style="color:green">%s</td></tr>'%(filename,result,error)

def writeIn(filename,contents):
	f=open(filename,"w+")
	f.write(str(contents))
	f.close()
	pass
def writeTexte(file,nomOut,nomOutTexte,nomReturnTexte):
	#output
	cheminOut="./tests/testsBackEnd/results/"+str(file)
	cheminOutput=cheminOut+"/out/"
	cmdOut=cheminOut+"/"+str(file)+"."+nomOut
	fileOutput=cheminOutput+str(file)+"_"+nomOutTexte+".txt"
	try:
		subprocess.call([cmdOut+" >"+fileOutput],shell=True)
	except subprocess.CalledProcessError as e:
		pass
	except OSError as e:
		pass
	#return
	try:
		print(str(file)+"."+nomOut)
		ret=subprocess.call(cmdOut)
		print("")
		fileReturn=cheminOutput+str(file)+"_"+nomReturnTexte+".txt"
		writeIn(fileReturn,ret)
	except subprocess.CalledProcessError as e:
		pass
	except OSError as e:
		pass	
def execution1(file,filename):
	os.system("mkdir -p ./tests/testsBackEnd/results/"+str(file)+"/out")
	obj=subprocess.Popen(["gcc","-w","./tests/testsBackEnd/"+str(filename), "-o","./tests/testsBackEnd/results/"+str(file)+"/"+str(file)+".out1"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
	out_error_list=obj.communicate()[0]
	writeTexte(file,"out1","output1","return1")
	return out_error_list
	pass
def execution2(file,filename):
	folderC="./tests/testsBackEnd"
	folderO="./tests/testsBackEnd/results/"+str(file)
	folderOutput="./tests/testsBackEnd/results/"+str(file)+"/out"
	obj=subprocess.Popen(["make","BackEnd","file="+str(file),"folderC="+str(folderC),"folderO="+str(folderO),"folderOutput="+str(folderOutput)],
stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
	out_error_list=obj.communicate()[0]
	writeTexte(file,"out2","output2","return2")
	return out_error_list
	pass
def compare(file):
	chemin="./tests/testsBackEnd/results/"+str(file)+"/out/"
	texteOutput1=chemin+str(file)+"_output1.txt"
	texteOutput2=chemin+str(file)+"_output2.txt"
	texteReturn1=chemin+str(file)+"_return1.txt"
	texteReturn2=chemin+str(file)+"_return2.txt"
	try:
		result1=filecmp.cmp(texteOutput1,texteOutput2)
		result2=filecmp.cmp(texteReturn1,texteReturn2)
		if(result1 and result2):
			return "success"
		else:
			return "failed"
	except:
		return "failed"
def printDict(list1,list2,list3):
	tab='<table border="1">'
	tab=tab+'<tr><th>File</th><th>Result</th><th>Error</th><tr>'
	length=len(list1)
	i=0
	while i<length:
		tab=tab+generate_tr(list1[i],list2[i],list3[i])
		i+=1
	tab=tab+'</table>'
	return tab
#delete exist folder
os.system("make BackClean")
list_in_tests = os.listdir("./tests/testsBackEnd/")
listFile=[]
listResult=[]
listError=[]
for name in sorted(list_in_tests):
	if name[-2:] == '.c':
		base=os.path.basename(name)
		file=os.path.splitext(base)[0]
		out_error_list1=execution1(file,name)
		out_error_list2=execution2(file,name)
		result=compare(file)
		listFile.append(file)
		listResult.append(result)
		if(result=="failed"):
			listError.append(out_error_list1+out_error_list2)
		else:
			listError.append("")
	else:
		pass
tab=printDict(listFile,listResult,listError)
writeIn("./testBackEnd.html",tab)
