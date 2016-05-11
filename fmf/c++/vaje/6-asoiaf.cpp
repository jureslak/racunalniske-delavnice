#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

class Junaki {
  private:
    map<string, vector<int>> junaki;
  public:
    bool dodaj_junaka(const string& ime) {
        if (je_junak(ime)) return false;
        junaki[ime] = {};
        return true;
    }
    bool je_junak(const string& ime) const {
        return junaki.find(ime) != junaki.end();
    }
    void dodaj_pojavitev(const string& ime, int word_number) {
        junaki[ime].push_back(word_number);
    }
    int size() const { return junaki.size(); }
};

// TODO dodaj cout

int main() {
    ifstream cf("data/characters.txt");
    if (!cf) {
        cout << "Error opening character list." << endl;
    }

    Junaki junaki;

    string ime;
    cf >> ime;
    while (cf) {
        junaki.dodaj_junaka(ime);
        cf >> ime;
    }

    int wordcnt;
    string word;
    for (int k = 1; k <= 5; ++k) {
        wordcnt = 10000000*k;
        stringstream ss;
        ss << "data/asoiaf" << k << ".txt";
        string name = ss.str();
        ifstream kf(name);
        if (!kf) {
            cout << "Error opening " << k << endl;
        }
        cf >> word;
        while (cf) {
            wordcnt++;
            if (junaki.je_junak(word)) {
                junaki.dodaj_pojavitev(word, wordcnt);
            }
            cf >> word;
        }
    }

// TODO dodaj graf povezanosti z utežmi
    cout << junaki.size() << endl;

    return 0;
}

