#ifndef AARRAY_H // AArray.h
#define AARRAY_H
#include <cassert>

template < typename T >
class AArray {
private:
    int m_length;
    T *m_data;
 
public:
    // Construtor 
    AArray(int length) {
        assert(length > 0);
        m_data = new T[length];
        m_length = length;
    }
 
    // Nao queremos permitir que copias 
    // de IntArray sejam criadas
    AArray(const AArray&) = delete;
    AArray& operator=(const AArray&) = delete;
 
    ~AArray() { delete[] m_data; }
 
    void clear() { m_length = 0; }
 
    T& operator[](int index)
    {
        assert(index >= 0 && index < m_length);
        return m_data[index];
    }
 
    int length() const;
};

// Implementacao da funcao length() fora da classe
template < typename T >
int AArray<T>::length() const { 
    return m_length; 
}
 
#endif
