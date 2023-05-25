// file dynamic_set.h
#ifndef DYNAMIC_SET_H
#define DYNAMIC_SET_H
#include <vector>

/**
 * Abstract class 'dynamic_set'. 
 * This class declares pure virtual functions that 
 * express the basic functionalities of a dynamic set data structure. 
 * A dynamic set is a set that can increase and decrease in size. 
*/
class dynamic_set {
public:
    virtual void add(int key) = 0;                               // O(lg n)
    virtual void remove(int key) = 0;                            // O(lg n)
    virtual void access_keys_inorder(void (*f)(int& key)) = 0;   // O(n)
    virtual void keys_as_vector(std::vector<int>& v) const = 0;  // O(n)
    virtual void clear() = 0;                                    // O(n)

    //------------------------------------------------------------------------
    // Descomente as funcoes abaixo a medida que voce as implementar nas classes filhas
    //virtual bool contains(int key) const = 0;                    // O(lg n)
    //virtual int minimum() const = 0;                             // O(lg n)
    //virtual int maximum() const = 0;                             // O(lg n)
    //virtual int successor(int key) const = 0;                    // O(lg n)
    //virtual int predecessor(int key) const = 0;                  // O(lg n)
    //virtual bool empty() const = 0;                              // O(1)
    //virtual int size() const = 0;                                // O(n) ou O(1)
    //-----------------------------------------------------------------------

    virtual ~dynamic_set() = default;
};

#endif 
