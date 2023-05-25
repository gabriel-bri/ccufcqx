#include <iostream>
#include <string>
#include <stdexcept>
#include <vector>
#include "Codification.h"
#include "HashTable.h"
using namespace std;

int main() 
{
    HashTable<std::string, float> ht (14, 1.0, 2.0, code_std_string);

    ht.add("atilio", 13);
    ht.add("erick", 14);
    ht.add("joana", 15);

    cout << ht.at("atilio") << endl;
    cout << ht.at("joana") << endl;
    cout << ht.at("erick") << endl;

}
