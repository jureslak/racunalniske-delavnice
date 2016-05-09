#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main() {
    ifstream ifs("data/anailza1.txt");
    if (!ifs) {
        cout << "Napaka pri odpiranju datoteke." << endl;
    }
    map<string, int> count;
    string s;
    while (ifs) {
        ifs >> s;
        count[s]++;
    }
    int cnt;
    vector<pair<int, string>> besede;
    besede.reserve(count.size());
    for (const auto& p : count) {
        tie(s, cnt) = p;
        besede.push_back({cnt, s});
    }
    sort(besede.begin(), besede.end());
    reverse(besede.begin(), besede.end());

    int n = 100;
    for (int i = 0; i < n; ++i) {
        cout << besede[i].first << ' ' << besede[i].second << endl;
    }

    return 0;
}

