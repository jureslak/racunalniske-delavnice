#include <iostream>
#include <string>

using namespace std;

int main() {
    string ime;
    while (true) {
        cout << "Kako ti je ime: ";
        cin >> ime;
        bool ok = true;
        for (char c : ime) {
            if (!('A' <= c && c <= 'Z') && !('a' <= c && c <= 'z') && c != ' ') {
                ok = false;
            }
        }
        if (ok) {
            break;
        }
        cout << "To pa ni lepo ime. A me zafrkavas?\n";
    }
    cout << "Tvoje ime ima " << ime.size() << " crk." << endl;
    return 0;
}

