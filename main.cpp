#include <iostream>
#include "antlr4-runtime.h"
#include "MainLexer.h"
#include "MainParser.h"
#include "Comp.h"
#include "MainBaseVisitor.h"
#include "dotexport.h"
#include <string>

using namespace antlr4;
using namespace std;

/*Main file which lauchs the compilation*/

int main(int argc, const char ** argv) 
{
    ifstream is (argv[1]);

    if (!is) 
    {
        cout << "erreur ouverture fichier" << endl;
        return -1;
    }

	string s(argv[1]);
	size_t pos1=s.find_last_of("/");
	string folderC=s.substr(0,pos1);
	string fileC=s.substr(pos1);
	size_t pos2=fileC.find(".c");
	string file=fileC.substr(0,pos2);

    ANTLRInputStream input(is);

    MainLexer lexer(&input);

    CommonTokenStream tokens(&lexer);

    MainParser parser(&tokens);

    tree::ParseTree* tree = parser.prog();

    DotExport dotexport(&parser);
    tree::ParseTreeWalker::DEFAULT.walk(&dotexport,tree);
    ofstream out;
    out.open(folderC+"/results/"+file+"/tmp.dot");
    out<<dotexport.getDotFile();
    out.close();
	string outPDF=folderC+"/results/"+file+"/out.pdf ";
	string tmpDOT=folderC+"/results/"+file+"/tmp.dot";
	string cmd="dot -Tpdf -o "+outPDF+tmpDOT;
    system(cmd.c_str());

   
    Comp visitor;


    Program* prog = (Program*)visitor.visit(tree);
    prog->buildIR();

	
	ofstream o;
    o.open(folderC+"/results/"+file+"/"+file+".s");

    prog->generateCode(o);
	cout << "PLD COMP Success" << endl;
    

    return 0;
}
