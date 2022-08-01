#include <iostream>

using namespace std;

struct Vector {
    int _size;
    int _capacity;
    int* _data;

    Vector(int _capacity) {
        this->_size = 0;
        this->_capacity = _capacity;
        this->_data = new int [_capacity];
    }

    ~Vector() {
        delete [] this->_data;
    }

    void show() {
        cout << "[ ";
        for(int i = 0; i < this->_size; i++) {
            cout << this->_data[i] << " ";
        }
        cout << "] " << this->_size << "/" << this->_capacity << endl;
    }

    void push_back(int value) {
        if(this->_size == this->_capacity) {
            this->reserve(this->_capacity * 2);
        }

        this->_data[this->_size] = value;
        this->_size += 1;
    }

    void pop_back() {
        if(this->_size > 0) {
            this->_size -= 1;
        }
    }

    int& front() {
        return this->_data[0];
    }

    int& back() {
        return this->_data[this->_size - 1];
    }

    int& operator[](int index) {
        return this->_data[index];
    }

    int size() {
        return _size;
    }

    int capacity() {
        return this->_capacity;
    }

    int * begin() {
        return &this->_data[0];
    }

    int * end() {
        return &this->_data[this->_size];
    }

    void reserve(int capacity) {
        int * novo = new int[capacity];
        if(capacity < this->_size){
            this->_size = capacity;
        }

        for(int i = 0; i < this->_size; i++) {
            novo[i] = this->_data[i];
        }

        delete [] this->_data;
        this->_data = novo;
        this->_capacity = capacity;
    }
};

int main() {
    Vector vet(3);
    vet.push_back(5);
    vet.push_back(6);
    vet.push_back(7);
    vet.show();
}
