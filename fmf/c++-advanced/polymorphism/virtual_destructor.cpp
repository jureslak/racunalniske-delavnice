#include <iostream>
#include <vector>

using namespace std;

struct A {
    A() { cout << "CA" << endl; }
    virtual ~A() { cout << "DA" << endl; }  // !!!!!
    virtual void f() { cout << "f" << endl; };
    int a;
};

struct B : public A {
    B() { cout << "CB" << endl; }
    ~B() { cout << "DB" << endl; }
};

struct C : public B {
    C() { cout << "CC" << endl; }
    ~C() { cout << "DC" << endl; }
};

struct D : public C{
    D() { cout << "CD" << endl; }
    ~D() { cout << "DD" << endl; }
    int h;
    void f() override { cout << "df" << endl; }
};

int main() {
    D* d = new D();
    A* a = d;
    delete a;
}
