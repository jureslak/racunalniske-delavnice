#include <iostream>
#include <vector>
#include <regex>
#include <thread>
#include <random>
#include <chrono>
#include <tuple>

using namespace std;

template <typename T>
T func(T t) {
    return t;
}
template<typename T, typename... Args>
T func(T t, Args... args) {
    return t + func(args...);
}

int main() {
    string pattern = "^.*$";

    regex first;                                        // default
    regex second = first;                               // copy
    regex third (pattern);                              // string object initialization
    regex fourth ("<[^>]>");                            // string literal initialization
    regex fifth (pattern.begin(),pattern.end());        // range initialization
    regex sixth {'.','+'};                              // initializer_list initialization

    regex seventh ("[0-9A-Z]+", regex::ECMAScript);     // with syntax option

    using namespace regex_constants;                    // introducing constants namespace
    regex eighth ("[0-9A-Z]+", ECMAScript);             // same as seventh

    regex ninth ("\\bd\\w+", ECMAScript | icase );      // multiple flags

    string subject = "Duddy the duck";
    string replacement = "yup";

    cout << regex_replace (subject, ninth, replacement);
    cout << endl;

    cout << func(1, 2, 3, func(1, 2, 3)) << endl;


    thread t([] {cout << "thread 1" << endl; });
    thread u([] {cout << "thread 2" << endl; });

    t.join();
    u.join();

    std::mt19937 gen(std::chrono::system_clock::now().time_since_epoch().count());
    std::gamma_distribution<double> g(2.4, 3.2);
    cout << g(gen) << endl;

    int a, b, c;
    tuple<int, int, int> tt = make_tuple(3, 4, 2);
    tie(a, b, c) = tt;

    cout << "All is good.\n";
    return 0;
}

