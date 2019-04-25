#include <iostream>

// Lastna tabela
template <typename T>
class Tabela {
    int size_;
    int capacity_;
    T* t;
  public:
    Tabela() : size_(0), capacity_(20), t(new T[capacity_]) {}
    // copy constructor (za kopiranje tabele)
    Tabela(const Tabela& v) : size_(v.size_), capacity_(v.capacity_) {
        t = new T[capacity_];
        for (int i = 0; i < size_; ++i) {
            t[i] = v[i];
        }
    }
    // copy assignment (za kopiranje tabele)
    Tabela& operator=(const Tabela& v) {
        size_ = v.size_;
        capacity_ = v.capacity_;
        delete[] t;
        t = new T[capacity_];
        for (int i = 0; i < size_; ++i) {
            t[i] = v[i];
        }
        return *this;
    }
    ~Tabela() { delete[] t; }
    const T& operator[](int i) const { return t[i]; }
    T& operator[](int i) { return t[i]; }
    void push_back(const T& v) {
        if (size_ == capacity_) {
            capacity_ *= 2;
            T* nt = new T[capacity_];
            for (int i = 0; i < size_; ++i) {
                nt[i] = t[i];  // skopiramo elemente
            }
            delete[] t;
            t = nt;
        }
        t[size_++] = v;
    }
    int size() const { return size_; }
};

// Dodamo možnost printanja tabele.
template <typename T>
std::ostream& operator<<(std::ostream& os, const Tabela<T>& v) {
    if (v.size() == 0) {
        return os << "[]";
    }
    os << "[" << v[0];
    for (int i = 1; i < v.size(); ++i) {
        os << ", " << v[i];
    }
    return os << "]";
}

using namespace std;

int main() {
    Tabela<char> a;

    for (int i = 0; i < 26; ++i) {
        a.push_back('a' + i);
    }

    cout << a << endl;

    return 0;
}
