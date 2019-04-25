#include <vector>
#include <string>
#include <iostream>
#include <set>

using namespace std;

template <typename T>
bool find(const std::vector<T>& a, const T& x) {
    for (const T& v : a) {
        if (v == x) return true;
    }
    return false;
}

template <typename C>
bool find(const C& a, const typename C::value_type& x) {
    for (const typename C::value_type& v : a) {
        if (v == x) return true;
    }
    return false;
}

template <>
bool find(const std::vector<int>& a, const int& x) {
    return true;
}

bool find(const std::vector<int>& a, const int& x) {
    return false;
}

template bool find(const std::vector<int>& a, const int& x);

template <typename T>
class A {
public:
    typedef T value_type;
    
    template <typename U>
    U f(U x) { return -x; } 
};

template <typename U>
int m(U x) {
    return x.template f(5);
}


int main() {
    
    vector<string> v = {"ab", "b", "c"};
    cout << find<string>(v, "c") << endl;
    
    vector<int> a = {1, 3, 4, 6};
    cout << find(a, 7) << endl;
    
    set<int> s = {1, 2, 3};
    cout << find(s, 7) << endl;

    
    A<int> g;
    cout << g.f(6) << endl;
    
    cout << m(g) << endl;
    
    return 0;
}
