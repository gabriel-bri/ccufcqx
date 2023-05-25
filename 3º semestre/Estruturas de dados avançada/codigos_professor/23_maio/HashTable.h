#ifndef C7E3A516_DE69_4A35_9845_FCE0DE537053
#define C7E3A516_DE69_4A35_9845_FCE0DE537053
#include <cmath>
#include <string>
#include <iostream>
#include <list>
#include <vector>
#include <utility>
#include <functional>

/**
 * Class that implements a chained hash table.
 * The operations of insertion, deletion and search are executed 
 * with complexity O(1) in the medium case. 
*/
template <typename K, typename V>
class HashTable {
private:
    // attributes
    size_t _n;                                         // number os pairs
    size_t _table_size;                                // number of buckets
    std::vector<std::list<std::pair<K, V>>> *_table;   // buckets
    float _load_factor;                                // 0 < load factor <= _n / _table_size
    float _max_load_factor;                            // load factor <= max_load_lactor
    size_t (*_hashing)(const K& k);                    // pointer to hashing function

    // Returns the smallest prime that is greater than or equal to x.
    // x is required to be such that x > 2
    size_t get_next_prime(size_t x);

    // Returns an integer in the range [0 ... _table_size-1]
    // This function receives a key k and: 
    // (1) computes k's hashing code h(x) by using the function in the 
    //     private attribute _hashing if it is different from nullptr; 
    //     otherwise, it uses the std::hash template defined in the header <functional>;
    // (2) computes an index in the range [0 ... _table_size-1] 
    //     by applying the division method: h(x) % _table_size
    size_t hash_code(const K& k);

public:
    // Deleted functions
    HashTable(const HashTable& t) = delete;
    HashTable& operator=(const HashTable& t) = delete;

    // Constructor: creates a a hash table with a prime number of buckets.
    // tableSize := the number of buckets of the table. Must be a prime number > 2.
    // lf  := load factor (lf > 0)
    // mlf := maximum load factor (mlf > 0 and lf <= mlf)
    // *h  := pointer to a function that receives a key k and returns 
    //        its hash code as an unsigned int
    // If the above conditions are not met, an exception must be thrown
    HashTable(size_t tableSize = 17, float lf = 1.0, float mlf = 1.0, 
              size_t (*h)(const K& k) = nullptr);

    // Destructor
    //~HashTable();

    // Returns the number of buckets in the HashTable.
    // A bucket is a slot in the arrays's internal hash table 
    // to which elements are assigned based on the hash value of their key.
    // The number of buckets influences directly the load factor of the 
    // container's hash table (and thus the probability of collision). 
    size_t bucket_count() const;

    // Returns the number of elements in bucket n.
    // A bucket is a slot in the arrays's internal hash table 
    // to which elements are assigned based on the hash value of their key.
    // The number of elements in a bucket influences the time it takes 
    // to access a particular element in the bucket. 
    size_t bucket_size(size_t n) const;

    // Returns the bucket number where the element with key k is located.
    size_t bucket(const K& k) const;

    // Returns the number of elements in the HashTable.
    size_t size() const;

    // Returns a bool value indicating whether 
    // the HashTable is empty, i.e. whether its size is 0.
    bool empty() const;

    // All the elements in the HashTable are dropped: 
    // their destructors are called, and they are removed from the container, 
    // leaving it with a size of 0.
    void clear();

    // Returns a reference to the mapped value of the 
    // element with key k in the HashTable.
    // If k does not match the key of any element in the container, 
    // the function throws an out_of_range exception.
    V& at(const K& k);

    // Inserts a new element in the HashTable.
    // If _n / _table_size > _load_factor then this functions calls the 
    // function rehash() passing the double of the actual size of the table.
    // The element is inserted only if its key is not equivalent 
    // to the key of any other element already in the hash table 
    // (keys in an HashTable are unique).
    // This effectively increases the hash table size by 1 if the element is inserted.
    // Returns a boolean indicating if an insertion was done.
    bool add(const K& k, const V& v);

    // Removes an element with key k from the hash table if it exists.
    // Returns a boolean indicating if a deletion was done.
    bool remove(const K& k);

    // gets the load factor
    float load_factor() const;

    // sets the load factor
    // lf must be a positive number, lf > 0
    void load_factor(float lf);

    // gets the max load factor
    float max_load_factor();

    // Sets the number of buckets in the container (bucket_count) to 
    // the most appropriate to contain at least n elements.
    // If n is greater than the current bucket_count multiplied by 
    // the load_factor, the container's bucket_count is increased 
    // and a rehash is forced.
    // If n is lower than that, the function may have no effect.
    void reserve(size_t n);

    // Sets the number of buckets in the container to m or more.
    // If m is greater than the current number of buckets in the 
    // container (bucket_count), a rehash is forced. 
    // The new bucket count can either be equal or greater than m.
    // If m is lower than the current number of buckets in the 
    // container (bucket_count), the function may have no effect 
    // on the bucket count and may not force a rehash. 
    // A rehash is the reconstruction of the hash table: 
    // All the elements in the container are rearranged according 
    // to their hash value into the new set of buckets. 
    // This may alter the order of iteration of elements within the container.
    // Rehashes are automatically performed by the container whenever 
    // its load factor is going to surpass its max_load_factor in an operation.
    void rehash(size_t m);

    // This function prints the following data in the terminal:
    // bucket_count()
    // load_factor()
    // max_load_factor()
    // the size of the largest bucket in the table
    // size()
    void print_estatistics();

    // If k matches the key of an element in the container, the function 
    // returns a reference to its mapped value.
    // If k does not match the key of any element in the container, 
    // the function inserts a new element with that key and returns a 
    // reference to its mapped value. Notice that this always increases 
    // the container size by one, even if no mapped value is assigned to 
    // the element (the element is constructed using its default constructor).
    V& operator[](const K& k);

    // Searches the container for elements whose key is k and returns 
    // the number of elements found. Because HashTable do not allow for 
    // duplicate keys, this means that the function actually returns 1 if 
    // an element with that key exists in the container, and zero otherwise.
    size_t count(const K& k);
};


template <typename K, typename V>
size_t HashTable<K,V>::get_next_prime(size_t x) {
    if(x <= 2) return 3;
    if(x % 2 == 0) x = x + 1;
    while(true) {
        int d {0};
        for(d = 2; d <= sqrt(x); d++) {
            if(x % d == 0) {
                break;
            }
        }
        if(d > sqrt(x)) {
            break;
        }
        x = x + 2;
    }
    return x;
}

template <typename K, typename V>
size_t HashTable<K,V>::hash_code(const K& k) {
    size_t code;
    if(_hashing != nullptr) {
        code = _hashing(k);
    }
    else {
        code = std::hash<K>()(k);
    }
    return code % _table_size;
}

template <typename K, typename V>
HashTable<K,V>::HashTable(size_t tableSize, float lf, float mlf, size_t (*h)(const K& k)) 
{
    if(lf > mlf || lf <= 0 || mlf <= 0) {
        throw std::runtime_error("lf > mlf");
    }
    _n = 0;
    _table_size = get_next_prime(tableSize);
    _table = new std::vector<std::list<std::pair<K,V>>>;
    _table->resize(_table_size);
    _load_factor = lf;
    _max_load_factor = mlf;
    _hashing = h;
}

template <typename K, typename V>
V& HashTable<K,V>::at(const K& k) {
    size_t bucket = hash_code(k);
    for(auto& par : (*_table)[bucket]) {
        if(par.first == k) {
            return par.second;
        }
    }
    throw std::out_of_range("nao existe essa chave na tabela!!");
}

template <typename K, typename V>
bool HashTable<K,V>::add(const K& k, const V& v) {
    //if(_n /_table > _load_factor ) {
    //    rehash(2 * _table_size);
    //}

    size_t bucket = hash_code(k); // achei o slot
    for(auto& par : (*_table)[bucket]) {
        if(par.first == k) {
            return false;
        }
    }
    (*_table)[bucket].push_back(std::make_pair(k,v));
    _n++;
    return true;
}

#endif /* C7E3A516_DE69_4A35_9845_FCE0DE537053 */
