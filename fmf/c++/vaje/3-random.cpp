#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <chrono>

using namespace std;

double f(double x) { return log(1+sin(x)); }

int main() {

    int n = 10000000;
    std::mt19937 gen(std::chrono::system_clock::now().time_since_epoch().count());
    std::uniform_real_distribution<double> X(0, 3);
    std::uniform_real_distribution<double> Y(0, M_PI);
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        double x = X(gen);
        double y = Y(gen);
        if (f(x) >= y) {
            sum += 1;
        }
    }
    cout << sum * M_PI * 3  / n << endl;

    return 0;
}

