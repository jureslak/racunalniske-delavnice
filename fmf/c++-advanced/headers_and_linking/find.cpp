#include <vector>
#include "find.hpp"

bool find(const std::vector<int>& a, int x) {
    for (int v : a) {
        if (v == x) return true;
    }
    return false;
}
