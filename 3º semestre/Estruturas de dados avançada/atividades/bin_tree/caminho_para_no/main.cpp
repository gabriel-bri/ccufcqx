#include <iostream>
#include <string>
#include "Tree.h"
using namespace std;

int main()
{
	string line;
    getline(cin, line);
    Tree bt(line);
    int value;
    cin >> value;
    string path = bt.find_path(value);
    cout << path << endl;
	return 0;
}