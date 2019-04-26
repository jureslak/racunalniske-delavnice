#include <iostream>
#include <string>
#include <vector>

using namespace std;

template <typename T>
class Tabela {
    T* t;
    int size_;
    int capacity;

public:  
    Tabela() : t(new T[5]), size_(0), capacity(5) {}
    ~Tabela() { delete[] t; }
     Tabela(const Tabela& v) : size_(v.size_), capacity(v.capacity) {
        t = new T[capacity];
        for (int i = 0; i < size_; ++i) {
            t[i] = v[i];
        }
    }
    // copy assignment (za kopiranje tabele)
    
    Tabela& operator=(Tabela&& v) {
        delete[] t;
        t = v.t;
        capacity = v.capacity;
        size_ = v.size_;
        v.t = new T[5];
        v.capacity = 5;
        v.size_ = 0;
        return *this;
    }
    
    Tabela& operator=(const Tabela& v) {
        size_ = v.size_;
        capacity = v.capacity;
        delete[] t;
        t = new T[capacity];
        for (int i = 0; i < size_; ++i) {
            t[i] = v[i];
        }
        return *this;
    }
    
    void push_back(const T& a) {
        if (size_ >= capacity) {
            capacity = 2*capacity;
            T* nt = new T[capacity];
            for (int i = 0; i < size_; ++i) {
                nt[i] = std::move(t[i]);
            }
            delete[] t;
            t = nt;
        }
        t[size_] = a;
        ++size_;
    }
    const T& operator[](int i) const { return t[i]; }
    T& operator[](int i) { return t[i]; }
    int size() const { return size_; }
};

template <typename T>
std::ostream& operator<<(std::ostream& os, const Tabela<T>& t) {
    if (t.size() == 0) return os << "[]";
    os << "[" << t[0];
    for (int i = 1; i < t.size(); ++i) {
        os << ", " << t[i];
    }
    os << "]";
    return os;
}

struct A {
    int a;
//     A() { cout << "C-d" << endl; }
//     A(int a) : a(a) { cout << "C-i" << endl; };
//     A(const A& a) : a(a.a) { cout << "C-c" << endl; };
//     ~A() { cout << "D" << endl; }
};
std::ostream& operator<<(std::ostream& os, const A& a) {
    return os << a.a;
}


int main() {
    
    Tabela<Tabela<A>> b;
    
    for (int j = 0; j < 10; ++j) {
        Tabela<A> a;
        for (int i = 0; i < 10; ++i) {
            a.push_back({i*j});
        }
        b.push_back(a);
    }
    
    cout << b << endl;
    
    return 0;
}
