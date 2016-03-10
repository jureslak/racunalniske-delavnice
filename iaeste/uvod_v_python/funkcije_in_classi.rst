.. _funkcijepython:

Funkcije in razredi
===================

Funkcije in razredi so zelo uporabljene strukture v programiranju. Zaradi
splošnosti in lepih načinov za dodajanje novih funkcionalnosti in zato, ker
naredijo kodo mnogo bolj berljivo in uporabno so eden najpomembnejših konceptov,
ki se je zelo razvit in zelo pomemben v resnem programiranju.

Funkcije
--------

Velikokrat se nam zgodi, da imamo v programu zelo podobno kodo, ki dela zelo
podobno reč, napisano večkrat. Recimo, da želimo izračunati produkt elementov v
seznamu, v našem programu pa imamo 3 sezname, ali pa še huje, imamo zelo veliko
seznamov, ki nam jih je podal uporabnik. Lahko pa koda postane tudi zelo
zapletena, saj znotraj ene zanke preverjamo, kaj drugega z drugo zanko in tako
naprej...

Primera takih programov:

.. code-block:: python

  a = [1, 2, 3, 4, 5]
  b = [14, 15, 0, 2]
  c = [-1, -1, -1, -1]
  pa = 1
  for i in a:
      pa *= i
  for i in b:
      pb *= i
  for i in c:
      pc *= i
  print(pa)
  print(pb)
  print(pc)

.. code-block:: python

  """Program preveri ali je število, ki ga vnese uporabnik popolno."""
  while True:
      a = int(input("Vpisi stevilo: "))
      if a == 0:
          break
      vsota_deliteljev = 0
      for i in range(1, a):
          if a % i == 0:
              vsota_deliteljev += i
      if vsota_deliteljev == a:
          print("Stevilo", a, "je popolno.")
      else:
          print("Stevilo", a, "ni popolno.")

V prvem primeru je problem zelo ponavljajoča koda, v drugem pa je težko
berljiva in zelo gnezdena. V tem primeru pridejo na pomoč funkcije, ki so
primerne ravno za take probleme: določene pomensko neodvisne izseke kode ločijo
in jih naredijo primerne za večkratno uporabo.

Funkcijo si lahko predstavljamo kot neko črno škatlo, ki ji nekaj damo, funkcija
pa potem s tem nekaj naredi in/ali nam nekaj vrne. Velika prednost funkcij je
to, da ni potrebno vedeti, kako točno deluje (lahko nam kakšno funkcijo npr.
napiše kdo drug, jo skopiramo iz interneta itd.). Poleg tega funkcije naredijo
kodo lažje za vzdrževanje, saj omogočajo preprosto popravljanje in spreminjanje.
Če namreč v funkciji pride do kakšne napake, lahko napako popravimo le v
definiciji, namesto da bi jo morali popraviti povsod, kjer funkcijo uporabimo.

Sintaksa
~~~~~~~~
Funkcijo vedno začnemo z besedo ``def``, nato pride ime funkcije (kot ime
spremenljivke mora biti nujno iz ene besede) in v oklepaju poljubno število
parametrov. Telo funkcije je potrebno zamakniti.

.. code-block:: python

  def imeFunkcije(parameter1, parameter2):
      Koda, ki se izvede, ko pokličemo funkcijo


Vračanje rezultatov
~~~~~~~~~~~~~~~~~~~

Če hočemo, da funkcija kaj vrne, to povemo z ukazom ``return``. Ko funkcija nekaj
vrne, lahko to ujamemo in s tem nekaj naredimo (npr. shranimo v spremenljivko,
izpišemo itd.) ali pa ne naredimo ničesar -- s tem bo stvar, ki jo je funkcija
vrnila, izgubljena. Poglejmo si primer, ki preveri, ali je dano število popolno,
in vrne ``True`` če je, sicer pa ``False``.

.. code-block:: python

  def popolno(n):
      vsota_deliteljev = 0
      for i in range(1, n):
          if n % i == 0:
              vsota_deliteljev += i
      if vsota_deliteljev == n:
          return True
      else:
          return False

.. warning::

  Ko se v funkciji izvede ``return`` ukaz, se funkcija konča, tudi če je
  pod stavkom še kaj kode. Če ukaza ``return`` ni, potem funkcija na koncu vrne
  ``None``.

Klicanje funkcij
~~~~~~~~~~~~~~~~

Ko izvedemo program, ki vsebuje samo definicije funkcij, se ne zgodi nič.
Funkcijo je treba namreč še poklicati. Naše funkcije kličemo popolnoma enako kot
že vdelane funkcije (npr. print(), range(), ...)

Oglejmo si primer programov iz uvoda, samo da tokrat uporabljata definirane
funkcije. Za vsakim programom je tudi njegov možen izpis.

.. code-block:: python

  def zmnozi(seznam):
      prod = 1
      for i in seznam:
          prod *= i
      return prod

  a = [1, 2, 3, 4, 5]
  b = [14, 15, 0, 2]
  c = [-1, -1, -1, -1]
  print(zmnozi(a))
  print(zmnozi(b))
  print(zmnozi(c))

::

  120
  0
  1

.. code-block:: python

  """Program preveri ali je število, ki ga vnese uporabnik popolno."""
  while True:
      a = int(input("Vpisi stevilo: "))
      if a == 0:
          break
      if popolno(a):
          print("Stevilo", a, "je popolno.")
      else:
          print("Stevilo", a, "ni popolno.")

::

  Vpisi stevilo: 13
  Stevilo 13 ni popolno.
  Vpisi stevilo: 6
  Stevilo 6 je popolno.
  Vpisi stevilo: 2
  Stevilo 2 ni popolno.
  Vpisi stevilo: 28
  Stevilo 28 je popolno.
  Vpisi stevilo: 0

Scoping
~~~~~~~
*Scoping* je angleški izraz, ki obravnava vidljivost spremenljivk po kodi.
*Scope* je območje v kodi, z določenim naborom spremenljivk, ki so vidne samo
znotraj tega območja. Območja se lahko gnezdijo in vsa novo ustvarjena so
znotraj globalnega scopa. V Pythonu se novi scopi ustvarijo znotraj funkcij.
Spremenljivke iz bolj zunanjih scopov lahko samo beremo, nastavljati jih pa ne
moremo.  Enostavno: spremenljivke, definirane znotraj funkcije, so vidne samo
znotraj funkcije. Primer:

.. code-block:: python

  def f():
      c = 8
      print(c)

  >>> f()
  8
  >>> print(c)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'c' is not defined

Bolj napreden primer:

.. code-block:: python

  def f():
      a = 1
      c = 2
      print(a, b, c)

  >>> a = 8
  >>> b = 7
  >>> print(a)
  8
  >>> print(b)
  7
  >>> print(c)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'c' is not defined
  >>> f()  # a v funkciji je lokalen, in nima povezave z zunanjim
  1 7 2
  >>> print(a)
  8
  >>> print(b)
  7
  >>> print(c)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'c' is not defined

Zaključek: stvari, ki jih počenemo v funkciji ne spreminjajo zunanjega sveta,
kot se od funkcij tudi pričakuje.

Za zelo podrobno razlago scopinga v Pythonu kliknite
`tukaj <http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/scope_resolution_legb_rule.ipynb>`_.

Razredi
-------

Kdaj se zgodi, da bi radi v programu imeli na primer seznam avtomobilov. Kako
si predstavimo avto? Za začetek mogoče kot seznam vrednosti, npr. ``["Yugo",
1977, 234564]``, kjer nam prvi element pove ime, drugi letnico, tretji pa
prevožene kilometre. Problemi nastanejo, ker bi radi dodajali nove podatke.
A vrstnega reda podatkov ne smemo spremeniti, saj bi to podrlo že vso obstoječo
kodo. Na vrsti red bomo odporni, če podatke poimenujemo, in seznam spremenimo v
slovar: ``{'ime': "Yugo", 'leto': 1997, 'razdalja': 234564}``. Sedaj laže
dodajamo nove podatke in smo odporni na vrstni red. Funkcije za delo z
avtomobili sedaj izgledajo nekako tako:

.. code-block:: python

  def prevozi(avto, km):
      avto['razdalja'] += km

Vsaka funkcija mora poleg dodatnih parametrov sprejeti še avto, ki ga želi
spremeniti. Take funkcije v resnici spadajo k avtu, saj so namenjene samo za
delo z avtom. Rešitev vseh teh problemov so *razredi* (class-i). S pomočjo
razredov definiramo svoje tipe, ki imajo lahko popolnoma enako obnašanje kot že
vgrajeni tipi. Vedno, ko se nam pojavijo problemi kot so opisani zgoraj, je
verjetno čas, da definirate svoj tip. Imena novih tipov se po tihem dogovoru vedno
začnejo z veliko začetnico, če pa je ime tipa iz več besed, te kar pritaknemo
zraven, zopet z veliko začetnico (taka imena se imenujejo *Camel Case*).

Sintaksa definicije novih razredov gre takole:

.. code-block:: python

  class ImeTipa(object):

      def __init__(self, arg1, arg2, ...):
          selg.arg1 = arg1
          # code

      def metoda(self, arg, ...):
          # code


Spremenljivka tega tipa, ki jo naredimo, se imenuje *objekt* tega razreda ali
*instanca* tega razreda. *Tip* in *razred* se nanašata na abstraktno
definicijo, *objekt* ali *instanca* pa na konkretno spremenljivko.
Funkcije, ki so vsebovane v tem objektu se imenujejo *metode*, spremenljivke
tega objekta pa *atributi*. Primer ustvarjanja objekta in klicanja metod:

.. code-block:: python

  a = ImeTipa(arg1, arg2, ...)
  a.metoda()

.. _konstruktorji:

Konstruktorji in destruktorji
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objekt ustvarimo tako, da napišemo ime razreda in podamo vse potrebne argumente.
V tem primeru Python pokliče *konstruktor* objekta, ki objekt zgradi.
Konstruktor objekta je metoda ``__init__``, ki jo napišemo v definicijo
razreda. Metoda kot prvi argument sprejme ``self``, to je objekt na katerem
trenutno delamo, torej na novo narejen, prazen objekt našega tipa. Metoda ima
lahko še dodatne parametre, ki jih je potrebno podati ob klicu konstruktorja.

V ``self`` lahko sedaj nastavimo atribute, ``self.ime = vrednost``. Do tako
nastavljenih atributov lahko dostopamo na instancah objekta s klicem ``a.ime``.
Elemente lahko tudi spreminjamo ali pa dodajamo nove. Seveda se take spremembe
poznajo samo na trenutni instanci, in ne na vseh objektih.
Primer:

.. code-block:: python

  class Avto(object):

      def __init__(self, ime, leto, razdalja):
          self.ime = ime
          self.razdalja = razdalja
          self.leto = leto

  >>> a = Avto("Yugo", 1978, 76234)  # self je a
  >>> print(a.leto)                   # branje atributov
  1978
  >>> b = Avto("Golf", 2000, 31243)  # self je tukaj b
  >>> b.razdalja = 312445             # nastavljanje atributov
  >>> print(b.razdalja)               # atribut se spremeni
  312445
  >>> print(a.razdalja)               # druga instanca se ni spremenila
  762134
  >>> a.solata = "7"                  # dodamo nov atribut, sam smo to dodali
  >>> print(b.solata)                 # b tega atributa nima, saj smo dodali samo k a-ju
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: 'Avto' object has no attribute 'solata'

Destruktor je funkcija, ki se pokliče, ko objekt izbrišemo. Objekt se
avtomatsko izbriše, ko na se na primer zaključi funkcija, ali pa če ga
eksplicitno izbrišemo z ``del``. Destuktorja ponavadi ni potrebno posebej
spreminjati, če pa to kdaj potrebujete, se naredi z definicijo metode
``__del__``.

Metode
~~~~~~

Znotraj objekta lahko definiramo funkcije za delo s tem objektom. Te metode se
definira enako kot navadne funkcije, vendar moramo tako kot pri konstruktorju
za prvi parameter sprejeti ``self``, ki vsebuje vse atribute, ki smo jih
definirali. S pomočjo metod lahko sedaj spreminjamo objekt ali pa nudimo
podatke o tem objektu. Metode se ponavadi imenuje z malimi začetnicami s
podčrtaji, ali pa ``mixedCase``, torej *Camel case* z malo začetnico na začetku.

Dodajmo ``Avtu`` od zgoraj metodo, ki zabeleži prevožene kilometre in metodo,
ki preveri, ali mora avto na servis.

.. code-block:: python

  class Avto(object):

      def __init__(self, ime, leto, razdalja):
          self.ime = ime
          self.razdalja = razdalja
          self.leto = leto


      def prevozi(self, prevozil_km):
          self.razdalja += prevozil_km

      def je_za_na_servis(self):
          return self.razdalja < 20000

  >>> a = Avto("Yugo", 1978, 6234)  # self je a
  >>> a.je_za_na_servis()           # brez argumentov, saj se a samodejno poda kot self
  False
  >>> a.prevozil_km(5000)
  >>> a.je_za_na_servis()
  True

Operatorji
~~~~~~~~~~
Lepo je pisati na primer ``3 + 4``, namesto ``add(3, 4)``. Enako funkcionalnost
lahko dodamo tudi svojim tipom, z definicijo novih operatorjev. Nove operatorje
definiramo tako, da definiramo metode s posebnimi imeni, npr. ``__add__`` za
seštevanje ali ``__mul__`` za množenje. Seznam vseh takih metod najdete, če
napišete npr. ``dir(int)``, še bolj popoln seznam pa najdete `tukaj
<https://docs.python.org/3.4/reference/datamodel.html>`_.
Definiranje svojega obnašanja operatorjev imenujemo *operator overloading*.
Overloadati se da vse, kar obstaja. Za primer naredimo razred ``Vector``,
ki predstavlja vektor v :math:`\mathbb{R}^3`, ki ga lahko množimo s skalarjem, skalarno
množimo z vektorjem in seštevamo in lepo izpišemo na zaslon.

.. code-block:: python

  class Vector(object):

      def __init__(self, x, y, z):
          self.x = x
          self.y = y
          self.z = z

      def __add__(self, other):  # vrne nov objekt, ki je vsota podanih
          return Vector(self.x + other.x, self.y + other.y, self.y + other.z)

      def __mul__(self, other):
          if isinstance(other, Vector): # skalarni produkt
              return self.x * other.x + self.y * other.y + self.z * other.z
          else:
              return Vector(self.x * other, self.y * other, self.z * other)

      def __str__(self):
          return "Vector({0.x}, {0.y}, {0.z})".format(self)

  a = Vector(1, -3, 4.5)
  b = Vector(-1, 4.7, 2)
  print(a + b)
  # Vector(0, 1.7, 6.5)

S tem dosežemo, da se naši objekti po uporabi ne razlikujejo od že vgrajenih
objektov. Te metode sicer lahko kličemo tudi direktno (tudi na Pythonovih tipih
recimo ``"asdf".__add__("ghjk")``), ampak tega noben priseben človek ne počne.
Pravzaprav je vsaka spremenljivka, ki jo naredite v Pythonu objekt, ki ni
popolnoma nič drugačen od takega, ki bi ga definirali mi. Ko na primer naredite
``int("1243")`` kličete konstruktor (metodo ``__init__``) razreda ``int``.

Pri množenju smo uporabili funkcijo ``isinstance``, ki se jo uporablja za
preverjanje tipov.

.. py:function:: isinstance(objekt, razred_ali_tuple_razredov)

  Vrne ``True``, če je ``objekt`` kateregakoli tipa izmed
  ``razred_ali_tuple_razredov``, sicer False.

Primer:

.. code-block:: python

  >>> isinstance(134, int)
  True
  >>> isinstance("abc", (int, list, bool))    # "abc" ni niti int niti bool niti list
  False

.. vim: spell spelllang=sl
