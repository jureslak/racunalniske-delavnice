#include <iostream>
#include <memory>

using namespace std;

void f(unique_ptr<int>& a) {
    *a = 6;
    cout << *a << endl;
}


void g(unique_ptr<int> a) {
    cout << *a << endl;
}

int main() {
    unique_ptr<int> a = make_unique<int>(4);
    cout << *a << endl;
    
    unique_ptr<int> b = std::move(a);
    
    f(b);
    
    g(std::move(b));
    
    return 0;
}
