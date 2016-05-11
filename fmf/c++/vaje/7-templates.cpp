#include <iostream>
#include <vector>

using namespace std;
template <typename T>
T skal(const vector<T>& a, const vector<T>& b) {
    T ret = T(0);
    int n = a.size();
    for (int i = 0; i < n; ++i) {
        ret += a[i] * b[i];
    }
    return ret;
}
template <typename T>
T func(T t) {
    return t;
}

template<typename T, typename... Args>
T func(T t, Args... args) {
    return t + func(args...);
}

int main() {

    cout << skal(vector<int>{2, 3, 4}, {5, 6, 7}) << endl;
    cout << skal(vector<double>{3.2, 4.5, 7.8}, {1.2, 3.5, .17}) << endl;
    cout << func(1, 6, func(3, 7)) << endl;

    return 0;
}

