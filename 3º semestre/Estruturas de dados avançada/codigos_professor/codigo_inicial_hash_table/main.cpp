#include <iostream>
#include <functional>
#include <string>
#include <stdexcept>
#include "Codification.h"
#include "HashTable.h"
using namespace std;

int main() 
{
    HashTable<std::string, float> ht;
    
    ht["atilio"] = 12.34;
    ht["ana"] = 76.54;
    ht["luiz maria"] = 78.9;

    cout << ht["atilio"] << endl;
    cout << ht["ana"] << endl;
    cout << ht["luiz maria"] << endl;

    cout << ht.count("ana") << endl;
    cout << ht.count("karla") << endl;
}
