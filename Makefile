ANTLR=./antlr4
ANTLRRUNTIME=./ANTLR4-CPP

default:
	$(ANTLR) -visitor -no-listener -Dlanguage=Cpp  Main.g4
	clang++ -DTRACE -g -std=c++11  -I $(ANTLRRUNTIME)/antlr4-runtime/ *.cpp ./gen-assembly/*.cpp ./ast-nodes/*.cpp  -o Main.exe $(ANTLRRUNTIME)/lib/libantlr4-runtime.a
clean:
	rm -rf MainBaseVisitor.* MainLexer.* MainParser.* MainVisitor.* *.dot *.pdf *.interp *.tokens *.exe *.s *.o *.out

build:
	./Main.exe ./tests/test.c
	as -o ./tests/results/test/test.o ./tests/results/test/test.s
	gcc ./tests/results/test/test.o
testsBackEnd:
	mkdir -p ./tests/testsBackEnd/results/$(file)/out
	./Main.exe ./tests/testsBackEnd/$(file).c
	as -o ./tests/testsBackEnd/results/$(file)/$(file).o ./tests/testsBackEnd/results/$(file)/$(file).s
	gcc -std=c99 -w ./tests/testsBackEnd/results/$(file)/$(file).o -o ./tests/testsBackEnd/results/$(file)/$(file).out2

testsFrontEnd:
	mkdir -p ./tests/testsFrontEnd/results/$(file)
	./Main.exe ./tests/testsFrontEnd/$(file).c .
	as -o ./tests/testsFrontEnd/results/$(file)/$(file).o ./tests/testsFrontEnd/results/$(file)/$(file).s
	gcc -std=c99 -w ./tests/testsFrontEnd/results/$(file)/$(file).o -o ./tests/testsFrontEnd/results/$(file)/$(file).out
