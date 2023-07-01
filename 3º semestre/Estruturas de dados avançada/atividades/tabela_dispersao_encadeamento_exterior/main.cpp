// Este arquivo ja esta finalizado e foi criado 
// exclusivamente para automatizar o teste da sua HashTable.
// Nao mexa nele. Se precisar fazer testes, durante a sua codificacao, crie
// o seu proprio arquivo main.cpp e va testando as funcoes aos poucos.
// Como este arquivo supoe que todas as funcoes pedidas foram implementadas,
// ele pode nao compilar caso voce ainda nao tenha terminado de programar todas elas.
#include <iostream>
#include <sstream>
#include "HashTable.h"
using namespace std;

int main() 
{
    // cria tabela hash com 7 slots e load_factor 1.0, podendo ser aumentado ate 5.0
    HashTable<int, double> ht (7, 1.0, 5.0);

    while(true) {
        string input, command;
        getline(cin, input);
        stringstream ss {input};
        ss >> command;

        // exit
        if(command == "exit") {
            cout << "$exit" << endl;
            break;
        }
        // bucket_count
        else if(command == "bucket_count") {
            cout << "$bucket_count " << endl;
            cout << "number of buckets = " << ht.bucket_count() << endl;
        }
        // bucket_size n
        else if(command == "bucket_size") {
            cout << "$bucket_size " << endl;
            int n;
            ss >> n;
            cout << "size of bucket " << n << ": " << ht.bucket_size(n) << endl;
        }
        // bucket k
        else if(command == "bucket") {
            int k;
            ss >> k;
            cout << "$bucket " << k << endl;
            cout << ht.bucket(k) << endl;
        }
        // size
        else if(command == "size") {
            cout << "$size " << endl;
            cout << "number of pairs = " << ht.size() << endl;
        }
        // empty
        else if(command == "empty") {
            cout << "$empty" << endl;
            cout << ((ht.empty()) ? "hashtable is empty" : "hashtable is not empty") << endl;
        }
        // clear
        else if(command == "clear") {
            cout << "$clear " << endl;
            ht.clear();
        }
        // at k
        else if(command == "at") {
            int k;
            ss >> k;
            cout << "$at " << k << endl;
            try{
                double v { ht.at(k) };
                cout << v << endl;
            }
            catch(const out_of_range& e) {
                cout << e.what() << endl;
            }
        }
        // add n k1 v1 k2 v2 ... kn vn
        else if(command == "add") {
            int n;
            ss >> n;
            cout << "$add " << n << " pairs" << endl;
            for(int i = 1; i <= n; ++i) {
                int k;
                double v;
                ss >> k;
                ss >> v;
                ht.add(k, v);
            } 
        }
        // remove k
        else if(command == "remove") {
            int k;
            ss >> k;
            cout << "$remove " << k << endl;
            cout << (ht.remove(k) ? "deleted" : "no key with this value") << endl;
        }
        // loadfactor
        else if(command == "loadfactor") {
            cout << "$loadfactor" << endl;
            cout << ht.load_factor() << endl;
        }
        // change_loadfactor l
        else if(command == "change_loadfactor") {
            double l;
            ss >> l;
            cout << "$change_loadfactor " << l << endl;
            ht.load_factor(l);
        }
        // maxloadfactor
        else if(command == "maxloadfactor") {
            cout << "$maxloadfactor" << endl;
            cout << ht.max_load_factor() << endl;
        }
        // reserve n
        else if(command == "reserve") {
            int n;
            ss >> n;
            cout << "$reserve " << n << endl;
            ht.reserve(n);
        }
        // rehash m
        else if(command == "rehash") {
            int m;
            ss >> m;
            cout << "$rehash " << m << endl;
            ht.rehash(m);
        }
        // print_estatistics
        else if(command == "print_statistics") {
            cout << "$print_statistics" << endl;            
            ht.print_statistics();
        }
        // count k
        else if(command == "count") {
            int k;
            ss >> k;
            cout << "$count " << k << endl;
            cout << ht.count(k) << endl;
        }
        // copy_constructor
        else if(command == "copy_constructor") {
            HashTable<int,double> newtable (ht);
            newtable.print_statistics();
            ht.print_statistics();
            newtable.load_factor(0.5);
            newtable.print_statistics();
            ht.print_statistics();
        }
        else {
            cout << "$invalid command" << endl;
        }
    }

    return 0;
}