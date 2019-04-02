#include <iostream>
#include <vector>

using namespace std;

class A {
public:
    int b;
//     virtual void h() = 0;
    virtual void f() { cout << "f" << endl; }
    void g() { cout << "g" << endl; }
    int f(int a) { return a; }
};

class B : public A {
    string s;
public:
    void g() { cout << "bg" << endl; }
    using A::f;
    void f() override { cout << "bf" << endl; }
//     void h() override { cout << "h" << endl; };
};

int main() {
    {
        A a;
        a.f();
        a.g();
        
        B b;
        b.f();
        b.g();
        
        A ba = b;
        ba.f();
        ba.g();
    }
    cout << "-------" << endl;
    {
        A* a = new A();
        a->f();
        a->g();
        
        B* b = new B();
        b->f();
        b->g();
        
        A* ba = b;
        ba->f();
        ba->g();
        
        B* bb = dynamic_cast<B*>(ba);
    }  
    cout << "-------" << endl;
    {
        A a;
        a.f();
        a.g();
        
        B b;
        b.f();
        b.g();
        
        A& ba = b;
        ba.f();
        ba.g();
        
        B& bb = dynamic_cast<B&>(ba);
        
        try {
            B& bbb = dynamic_cast<B&>(a);
        } catch (const std::exception& b) {
            cout << "ups" << endl;
        }
    }   
    vector<A*> v;
    v.push_back(new A());
    v.push_back(new B());
    v.push_back(new A());
    v.push_back(new B());
    v.push_back(new A());
    
    for (A* a : v) {
        a->f();
        if (dynamic_cast<B*>(a) != nullptr) {
            cout << "jaz sem b" << endl;
        }
    }
    
    
    
    
    return 0;
}
