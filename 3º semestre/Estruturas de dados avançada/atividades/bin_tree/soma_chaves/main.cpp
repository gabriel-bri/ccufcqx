#include <iostream>
#include <string>
#include "Tree.h"
using namespace std;

int main()
{
	string line;
    getline(cin, line);
    Tree bt(line);
    cout << bt.min_key() << " " << bt.sum_keys() << endl;
    cout << bt.total_internal_nodes() << " " << bt.um_filho() << endl;
	return 0;
}