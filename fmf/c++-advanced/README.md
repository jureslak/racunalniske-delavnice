# Linkanje in compilanje

```
g++ -c a.cpp
g++ -c find.cpp
ar rcs mylib.a a.o find.o
g++ -o main main.cpp -lmy -L.
./main
```
