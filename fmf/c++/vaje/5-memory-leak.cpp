#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n = 100000000;
    int p = 0;
    for (int i = 0; i < n; ++i) {
        p += i;
    }
    cout << p << endl;

    int* q;
    for (int i = 0; i < n; ++i) {
        q = new int(4 + p);
//          q = new int(4 + p);
//          delete q;
    }
    cout << *q << endl;

    return 0;
}

