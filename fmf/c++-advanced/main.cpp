#include <iostream>
#include <vector>
#include "find.hpp"
#include "find2.hpp"
#include "a.hpp"

using namespace std;

int main() {
    vector<int> a = {2, 3, 4, -4, 6};
    cout << find(a, 5) << endl;
    cout << find(a, -4) << endl;
    cout << find2(a) << endl;
    
    f();
    
    return 0;
}
