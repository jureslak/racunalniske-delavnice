#include <iostream>

using namespace std;

template <typename T>
T sum(const T& first) { return first; }

template <typename T, typename ...Args>
T sum(const T& first, const Args&... rest) {
    return first + sum(rest...);
}

int main() {
    cout << sum(1) << endl;
    cout << sum(1, 2, 3, 4) << endl;

    return 0;
}
