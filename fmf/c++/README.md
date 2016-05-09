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

## Standardna knjižnica
C++ ima (od standarda 11 najprej) spodobno veliko standardno knjižnico. Ne more
se kosati s Pythonom ali Javo, je pa veliko boljša od C-jeve.

Dokumentacija, ki jo bomo veliko uporabljali je na voljo na
[http://www.cplusplus.com/reference/](http://www.cplusplus.com/reference/).
Alternativa je [http://en.cppreference.com/w/](http://en.cppreference.com/w/).

<!---
vim: set spell spelllang=sl:
-->
