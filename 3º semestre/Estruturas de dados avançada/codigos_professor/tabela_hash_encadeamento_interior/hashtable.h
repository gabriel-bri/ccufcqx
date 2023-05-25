#ifndef hashtable_h
#define hashtable_h
#include <iostream>
#include <utility> 
#include <functional>
#include <stdexcept>
#include <vector>

template <typename K, typename V>
class HashTable {
public:
    // construtor: recebe tamanho da tabela e uma funcao de hash (opcional)
    HashTable(size_t tableSize = 101, size_t (*h)(const K& key) = nullptr);

    // insere o par (key,value) na tabela se e somente se ela nao estiver cheia
    bool insert(const K &key, const V &value);

    // retorna o valor associado a chave se ela existir
    V& search(const K &key);

    // remove chave key se e somente se estiver na tabela e retorna 
    // um booleano indicando se remocao foi bem sucedida
    bool remove(const K &key);

    // retorna true se e somente se a tabela contem a chave key
    bool contains(const K &key) const;
    
    // retorna o numero de elementos (pares) na tabela
    size_t size() const;

    // destrutor
    //~HashTable();

private:
    const char ACTIVE = 'A';
    const char EMPTY = 'E';
    const char DELETED = 'D';

    struct HashEntry 
    {
        std::pair<K,V> element;
        char status;

        HashEntry(const K &key = K{}, const V &value = V{}, char st = EMPTY )
            : element( make_pair(key,value) ), status( st ) { }
    };

    std::vector<HashEntry> *_table;     // ponteiro para array (tabela)
    size_t _n;                          // numero de pares armazenados
    size_t (*_hashing)(const K& key);   // ponteiro para funcao de hashing

    // funcao que retorna um slot na tabela, cujo valor esta vinculado
    // a funcao de codificacao _hashing e a um inteiro i (0 <= i <= _table.size())
    // que, juntos, determinam a sequencia de sondagem
    // o calculo do slot eh dado por: (_hashing(key) + i) % _table.size()
    size_t hash_code(const K &key, size_t i) const; 

    // retorna um primo maior ou igual a x
    // espera-se que x > 2
    size_t get_next_prime(size_t x) const; 
};

#endif