#include <iostream>
#include <vector>

using namespace std;

class A {
  public:
    int x;
    A(int y) : x(y) { cout << "int constructor" << endl; }
    A() : x(0) { cout << "Default constructor" << endl; }
    A(const A&) { cout << "Copy constructor" << endl; }
    A& operator=(const A&) { cout << "Copy assignment" << endl; return *this; }
    ~A() { cout << "Default destructor" << endl; }
    bool operator<(const A& a) const { return x < a.x; }
};
ostream& operator<<(ostream& os, const A& a) {
    return os << a.x;
}


int main() {
    A a;
    A b(5);
    A c(a);
    A d = c;
    A e;
    e = a;
    if (a < b) {
        e = b;
    } else {
        e = c;
    }
    cout << e << endl;

    return 0;
}

