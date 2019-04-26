#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct A {
    int& a;
    A(int& b) : a(b) {}
};



int main() {
    int b = 7;
    A a(b);
    A c(a);
    
    
    
//     {
//     int b = 7;
//     a.a = &b;
//     }
    
//     A a2 = a;
    
//     b = 8;
    
//     cout << *a2.a << endl;
    
    b = 8;
    cout << a.a << endl;
    
    return 0;
}
