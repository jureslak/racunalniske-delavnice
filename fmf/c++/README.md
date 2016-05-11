# C++

Tukaj najdete vse potrebno za računalniško delavnico iz C++-a.

## Predpriprava
Potrebovali bomo prevajalnik (npr. `g++` ali `clang`), urejevalnik (npr.
`sublime`, `vim` ali `Notepad++`) in ukazno vrstico.

Običajen C++ program je sestavljen iz ene ali več datotek s končnico `.cpp` ali
`.hpp`, od katerih natanko ena definira funkcijo `main`.

Primer osnovnega programa, ki so ga lahko shranite v `hello_world.cpp` in
poženete.

```
#include <iostream>

int main() {
    std::cout << "Hello world.\n";
    return 0;
}
```

Program prevedete z ukazom
```
g++ -o hello_world hello_world.cpp
```
kar ustvari executable datoteko (na Windowsih `exe`).
Poženete jo lahko z
```
./hello_world
```
ali kar
```
hello_world
```
na Windowsih.

Executable lahko prenesete tudi na drug računalnik (s podobnim OS), pa bo delal
tudi tam brez težav.

### Prevajanje
Bolj pogosto se za prevajanje uporablja ukaz
```
g++ -Wall -pedantic -std=c++11 -o
```
ki vklopi dodatna opozorila in upošteva novejši standard. Ekvivalenten ukaz je
na voljo za `clang`.

Poleg zgoraj naštetega, lahko dodamo tudi zastavice `-O0, -O1, -O2, -O3` ki
vklopijo različne nivoje optimizacije (za ceno daljšega prevajanja), kjer je 3
najvišji nivo.

### Napake
Dobite lahko dve vrsti napak: od prevajanju in ob zagonu.
Napake pri prevajanju se pojavijo ko poskusite prevesti program in pomenijo,
da je nekaj narobe sintaktično ali semantično (npr. kaj z vašimi tipi). Primer:
```
$ g++ -Wall -pedantic -std=c++11 -o hello_world hello_world.cpp
0-hello_world.cpp: In function ‘int main()’:
0-hello_world.cpp:5:5: error: expected ‘;’ before ‘return’
     return 0;
     ^~~~~~
```
Napake ob zagonu se zgodijo, ko zaženete program in pomenijo,
da ste naredili nekaj neveljavnega, npr. šli čez seznam ali delili z nič
(ne pa npr. da ste sešteli `int` in `string`). Taka napaka ponavadi konča z
redkobesednim sporočilom `Segmentation fault` ali okenčkom z napako na Windowsih.

## Osnove
Zanke in if stavki:
```
while (true) {
    for (int i = 0; i < n; ++i) {
        if (i > 5) {
            cout << i << endl;
            break;
        }
    }
}
```

Funkcije:
```
double razdalja(int x, int y) {
    return sqrt(x*x + y*y);
}
```


## Standardna knjižnica
C++ ima (od standarda 11 najprej) spodobno veliko standardno knjižnico. Ne more
se kosati s Pythonom ali Javo, je pa veliko boljša od C-jeve.

Dokumentacija, ki jo bomo veliko uporabljali, je na voljo na
[http://www.cplusplus.com/reference/](http://www.cplusplus.com/reference/).
Alternativa je [http://en.cppreference.com/w/](http://en.cppreference.com/w/).

Pogledali bomo podatkovne strukture, slučajne spremenljivke, algoritme, foreach zanko.

Vprašanja za čast in slavo:
* Kaj je najbolj pogosta beseda z n črkami v skripti Analiza 1, za n = 3, 4, 5, 6, 7, 8, ...
* Koliko je integral `\int_0^\pi \log(1+ \sin x) dx` na 1e-2 relativne napake natančno?
* Koliko permutacij stavka "FMF JE KUL" vsebuje natanko tri besede (strnjene podnize znakov ločene s
  presledkom)?
* Kako dolga je najkrajša pot skozi labirint? Začne se zgoraj levo.


## Classi

Podobno kot v ostalih jezikih. Najenostavnejši primer:
```
struct Junak {
    string ime;
    int ponovitev;
};
```

Uporaba:
```
Junak nino;
nino.ime = "Nino";
nino.ponovitev = 4;
Junak jana = {"Jana", 3};
```

### Metode, konstruktorji, operatorji.
```
class A {
  public:
    int x;
    A(int y) : x(y) { cout << "int constructor" << endl; }
    A() : x(0) { cout << "Default constructor" << endl; }
    A(const A&) : { cout << "Copy constructor" << endl; }
    A& operator=(const A&) { cout << "Copy assignment" << endl; }
    ~A() { cout << "Default destructor" << endl; }
    bool operator<(const A& a) const { return x < a.x; }
};
ostream& operator<<(ostream& os, const A& a) {
    return os << a.x;
}

A a;
A b(5);
A c(a);
A d = c;
A e;
e = a;
if (a < b) {
    e = b;
} else {
    e = c;
}
cout << e << endl;
```

### Memory leaks
```
while (true) {
    int* p = new int(5);
}
```
ali
```
int* p = new int(5);
p = new int(6);
delete p;
```

Dokončaj class Junaki.

## Templates

Velikokrat je treba napisati skoraj enako funkcijo za veliko različnih tipov.
Ali pa narediti generičen container, recimo vector.
Takrat uporabimo template.

Namesto:
```
double skal(const vector<double>& a, const vector<double>& b) {
    double ret = 0;
    for (int i = 0; i < a.size(); ++i) {
        ret += a[i] * b[i];
    }
    return ret;
}
```
napišemo
```
template <typename T>
T skal(const vector<T>& a, const vector<T>& b) {
    T ret = T(0);
    for (int i = 0; i < a.size(); ++i) {
        ret += a[i] * b[i];
    }
    return ret;
}
```

Funkcije poljubno mnogo spremenljivk.
```
template <typename T>
T func(T t) {
    return t;
}

template<typename T, typename... Args>
T func(T t, Args... args) {
    return t + func(args...);
}
```

Napiši funkcijo, ki sprinta poljuben container. Ali pa napiši minimum funkcijo za poljubno mnogo
argumentov.

### Templati so jezik v jeziku
Glej primer 8 in assembly kodo.
```
g++ -o 8 8-templates2.cpp -g -Wa,-alh -O3 | head -40
```

## Prosto
Možne teme:
* Pointerji, reference in iteratorji
* Multithreading
* Dedovanje in virtualne funkcije

<!---
vim: set spell spelllang=sl:
-->
