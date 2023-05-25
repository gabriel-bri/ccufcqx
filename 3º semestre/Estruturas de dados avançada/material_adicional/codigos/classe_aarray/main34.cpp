#include <iostream>
#include <string>
#include "AArray.h"
using namespace std;

int main() {
    AArray<double> b(20);
    AArray<string> str(10);

    for(int i = 0; i < 15; i++)
        b[i] = i * 3.4;

    for(int i = 0; i < b.length(); i++)
        cout << b[i] << " ";
    
    str[0] = "Amanda";
    str[1] = "Carla";

    for(int i = 0; i < str.length(); i++)
        cout << str[i] << " ";

    cout << endl;
    return 0;
}