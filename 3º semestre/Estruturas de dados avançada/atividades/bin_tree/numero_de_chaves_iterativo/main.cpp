#include <iostream>
#include <string>
#include "Tree.h"
using namespace std;

int main()
{
	string line;
    getline(cin, line);
    Tree bt(line);
    cout << bt.size() << endl;
	return 0;
}