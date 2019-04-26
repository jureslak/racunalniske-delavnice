#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct A {
    string s_;
    A() : s_("default") { cout << "Default C " << s_ << endl; }
    A(const A& a) : s_(a.s_) { cout << "Copy C " << s_ << endl; }
    A(A&& a) : s_(std::move(a.s_)) { cout << "Move C " << s_ << endl; }

    explicit A(string s) : s_(s) { cout << "User C " << s_ << endl; }
    A(string s, int) : s_(s) { cout << "User C2 " << s_ << endl; }

    ~A() { cout << "Default D " << s_ << endl; }
    
    A& operator=(const A& a) { s_ = a.s_; cout << "Copy A " << s_ << endl; return *this; }
    A& operator=(A&& a) { s_ = std::move(a.s_); cout << "Move A " << s_ << endl; return *this; }
};



int main() {
    
    A a;
    A b{"234"};
    b = std::move(a);
    A c(a);
    A d = b;

    vector<A> v;
//     v.push_back(A("b"));
    v.emplace_back("b", 3);
    
    for (const A& a : v) {
                
    }
        cout << " ------ " << endl;

    
    
    
    return 0;
}
