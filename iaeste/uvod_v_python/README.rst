Delavnica Uvod v Python
=======================

Izvedena v okviru Iaeste, 10. 3. 2016 ob 17.00 v II/3B na Fakulteti za strojništvo.

Za izvedbo delavnice potrebujete neko verzijo Pythona, priporočljiva je najnovejša verzija Python
3, na voljo na https://www.python.org/downloads/.

Dokumentacija je na voljo na https://docs.python.org/3.5/.

Osnove
======

V tem poglavju si bomo ogledali osnove programiranja, s katerimi lahko
vzpostavimo osnovno komunikacijo z računalnikom in naredimo zelo enostavne
programe.

Spremenljivke
-------------

Spremenljivke so prostori v spominu z določenim imenom, v katere lahko spravimo
neko vrednost. Tako lahko npr. pod ime ``leta`` spravimo vrednost ``5``. V
osnovi ločimo več tipov spremenljivk, npr. ``float`` (realna števila), ``int``
(cela števila) in ``string`` (nize znakov). Začetek in konec ``stringa`` je
označen z dvojnim ali enojnim narekovajem (``"`` ali ``'``). Python tipe
spremenljivk določa samodejno.

Spremenljivke se definira na naslednji način:

.. code-block:: python

  # -*- coding: utf-8 -*-

  x = 2
  y = 5
  ime = "Andreja"
  leta = x + y


Znak = v programiranju nima istega pomena kot v matematiki. ``=``
pomeni "vrednost na desni zapiši v spremenljivko na levi". Torej bo ukaz
``x = x + 2`` dejansko pomenil "``x`` povečaj za 2".

Komentarji
----------

Komentarji so programerjeve opombe v kodi, namenjene bralcu -- sebi ali nekomu
drugemu, ki bo to bral za njim. Interpreter jih ignorira. V Pythonu (tako kot v
veliko drugih jezikih) obstajajo enovrstični in večvrstični komentarji.
Enovrstični komentarji se začnejo z znakom ``#``, vse za tem znakom v vrsti se
ignorira (tako lahko ``#`` uporabimo na začetku vrste ali pa pozneje).
Večvrstični komentarji se začnejo in končajo s trojnim narekovajem ``"""``, vse
med začetkom in koncem pa se ignorira.

Komentarje se ponavadi napiše za uvod/obrazložitev programa, pred manj
razumljiv del kode, da obrazložimo njeno delovanje, ali pa če želimo kakšen del
kode trenutno umakniti iz programa, ne da bi ga izbrisali. Komentarji pogosto
tudi obrazložijo in dokumentirajo kodo in narekujejo njeno uporabo.

Primer:

.. code-block:: python

  ime = "Janez"  # ime naj bo brez presledkov in se začne z veliko začetnico
  # v absx shranimo absolutno vrednost x
  x = -8
  if x < 0:
      absx = -x
  else:
      absx = x

Standard input in output
------------------------

Standardni input in output bosta za nas pomenila branje uporabnikovega vpisa in izpisovanje na zaslon.

Uporabljali bomo funkciji:

.. code::

  input(niz_znakov)

Izpiše ``niz_znakov`` in vrne niz znakov, ki ga je vtipkal uporabnik.

.. code::

  print(objekt)

Izpiše niz objekt ``objekt``. Objekt je lahko število, niz znakov, ...


Primer uporabe funkcije ``input`` in ``print``:

.. code-block:: python

  if __name__ == '__main__':
      # Get an integer from the user (will error on non-integer)
      x = int(input("Write an integer: "))
      print(x)

      # Get a float (will error on non-number)
      y = float(input("Write a float: "))
      print(y)

      # Get a string
      z = input("Write something: ")
      print(z)

Primer uporabe metode ``format``:

.. code-block:: python

  x = 5
  y = 10

  # Izpišimo '5 plus 10 je enako 15'
  print('{0} plus {1} je enako {2}'.format(x, y, x + y))

If stavki
---------

Če želimo, da se naš program pod drugačnimi pogoji obnaša različno, uporabimo
``if stavek``. Če je pogojev več, lahko za ``if`` uporabimo še ``elif`` (else
if), ki doda dodatne pogoje. Če imamo pogojev veliko, ``elif`` uporabimo
večkrat. Za konec pa lahko damo še ``else``, ki se izvede takrat, ko ni bil
izpolnjen noben od pogojev v ``if`` in ``elif`` stavkih. ``elif`` in ``else``
deli niso obvezni.

Sintaksa if stavkov je naslednja (pazljivi moramo biti na zamik po if stavku -
dobimo ga tako, da pritisnemo tabulator, ki se nahaja nad CAPS LOCK tipko na
tipkovnici):

.. code-block:: python

  if pogoj:
      # Se izvede če je izpolnjen pogoj
  elif pogoj2:
      # Se izvede če je izpolnjen pogoj2 (in ni izpolnjen pogoj)
  elif pogoj3:
      # Se izvede če je izpolnjen pogoj3 (in nista izpolnjena prejšnja pogoja)
  else:
      # Se izvede če ni izpolnjen noben od zgornjih pogojev


Bodite pazljivi na dvopičje za pogojem in zamik v naslednji vrsti. Zamiki so
v Pythonu zelo pomembni, saj z njimi označimo del kode, ki spada pod določen
``if stavek`` (in druge podobne stvari). Brez zamikov vaša koda ne bo
delovala! Kodo zamaknete z uporabo tabulatorja, ki se nahaja nad tipko caps
lock.

Pogoji
~~~~~~

Pogoji so lahko enostavni ali sestavljeni. Enostavni pogoji so npr. primerjanje
enakosti (je enako ``==``, ni enako ``!=``), primerjanje vrednosti (večje
``>``, večje ali enako ``>=``, manjše ``>``, manjše ali enako ``<=``),
sestavljeni pa so narejeni iz kombinacije enostavnih z uporabo logičnih
operacij ``not``, ``and``, ``or``, ``xor`` itd.

Primer:

.. code-block:: python

  x = int(input("Vpisite stevilo: "))
  if x > 0:
      if x > 100:
          print("x je vecji od 100")
      else:
          print("x je pozitiven in manjsi ali enak 100")
  elif x == -5:
      print("x je -5")
  else:
      print("x je negativen in ni enak -5")

Zanke
-----

Zanke se uporablja takrat, ko moramo neko stvar ponoviti večkrat. Če moramo
npr. izpisati vsa števila med 1 in 100 uporabimo zanko. Če hočemo isto stvar
ponoviti 3-krat, uporabimo zanko. Če bi radi, da se nekaj dogaja, dokler ni
izpolnjen nek pogoj (npr. vtipkavaj geslo, dokler ne vtipkaš pravilnega),
uporabimo zanko.

While zanka
~~~~~~~~~~~

.. code-block:: python

  while pogoj:
      # Se izvaja dokler je pogoj izpolnjen

``while`` zanko uporabimo takrat, ko se mora nekaj izvajati dokler je pogoj
izpolnjen. Pri ``while`` zanki moramo biti zelo pozorni na neskončne zanke.
Neskončna zanka se zgodi takrat, ko je pogoj vedno izpolnjen, program pa bo
tekel v neskončnost. Če se nam to slučajno zgodi, pritisnemo kombinacijo tipk
``ctrl+c``, s čimer program prekinemo.

.. code-block:: python

  """
  Uporabnik vpisuje geslo.
  """

  geslo = 123
  x = int(input("Vpisi geslo: "))

  while x != geslo:
      x = int(input("Ponovno vpisi: "))

  print("Bravo!")

Primer neskončne zanke:

.. code-block:: python

  """
  Želeli smo spremenljivko x iz 0 manjšati dokler ni enaka -100 in takrat zanko
  prekiniti, a smo se zmotili in namesto - napisali +. Seveda smo dobili
  neskončno zanko, ki x povečuje (in izpisuje) v neskončnost.
  """

  x = 0
  while x != -100:
      print(x)
      x = x + 1

Če se kdaj zataknete v neskončno zanko, pritisnite ``CTRL + c``, ki prekine
trenutno izvajani program.

For zanka
~~~~~~~~~

.. code-block:: python

  for spremenljivka in zbirka:
      # Se izvaja dokler spremenljivka ne preteče vseh elementov zbirke.

``for`` zanko uporabimo takrat, ko želimo, da naša spremenljivka preteče vse
elemente neke zbirke. Zbirka je lahko seznam, niz znakov, slovar, iterator ali
kaj podobnega, bolj podrobno si bomo to pogledali pozneje. Zaenkrat bomo for
zanko večinoma uporabljali skupaj s funkcijo ``range(x)``, ki vrne vse elemente
od ``0`` do ``x-1`` (torej ``range(5)`` vrne ``[0, 1, 2, 3, 4]``).

Preprost primer:

.. code-block:: python

  """
  Program izpiše števila od 0 do 49.
  """

  for i in range(50):
      print(i)

Bolj kompliciran primer:

.. code-block:: python
  """
  A for loop is usually used when we want to repeat a piece of code 'n' number of
  times, or when we want to iterate through the elements of a list (or something
  similar).

  In this example our program will 'sing' out the 99 bottles of beer song
  (http://en.wikipedia.org/wiki/99_Bottles_of_Beer). We use .format() to put the
  number of bottles in the text and we use an if sentance for the last two
  verses.
  """

  for i in range(100):
      bottle_num = 99 - i
      song = ("{0} bottles of beer on the wall, {0} bottles of beer.\n" +
              "Take one down, pass it around, {1} bottles of beer on the " +
              "wall ...\n")
      song_one = ("1 bottle of beer on the wall, 1 bottle of beer.\n" +
                  "Take it down, pass it around, there are no bottles " +
                  "left on the wall ...\n")
      song_no = ("No more bottles of beer on the wall, no more bottles of " +
                 "beer.\nGo to the store and buy us some more, 99 bottles " +
                 "of beer on the wall ...\n")
      if i == 99:
          print(song_no)
      elif i == 98:
          print(song_one)
      else:
          print(song.format(bottle_num, bottle_num - 1))
Break
~~~~~

Če kjerkoli v zanki napišemo ukaz ``break``, bo zanka takrat prekinjena.
Občasno se programira tudi tako, da zanalašč naredimo neskončno zanko, in potem
ob določenih pogojih pokličemo ``break``.

Ukaz break prekine le 'najbližjo' zanko -- če imamo gnezdenih več zank (npr.
for zanka znotraj while zanke) se bo prekinila le notranja zanka (v našem
primeru for zanka).

Primer:

.. code-block:: python

  """
  Uporabnik vpisuje geslo. Če 5x zaporedoma vpiše napačno geslo je izključen iz
  sistema (za to poskrbi spremenljivka stevec)
  """

  geslo = 123
  stevec = 0
  x = int(input("Vpisi geslo: "))

  while x != geslo:
      stevec = stevec + 1
      if stevec > 4:
          break
      x = int(input("Ponovno vpisi: "))

  if x != geslo:
      print("Preveckrat si poskusil, zaklenjen si iz sistema!")
  else:
      print("Bravo!")

Continue
~~~~~~~~

Continue je podoben stavku ``break``, le da ne prekine najbolj notranje zanke,
ampak preskoči vse do konca trenutne iteracije in takoj začne izvajanje
naslednje. To je uporabno na primer za filtriranje neveljavnih podatkov:

.. code-block:: python

  a = "sajkdfs adfjkhasdf jkasdkfjas dfkjhasd fasdlfkjsa dflkjsadf"
  veljavno = "aeiou"
  for i in a:
      if a not in veljavno:
          continue
      # tukaj zelo veliko kode, ki procesira veljavne podatke

Kot ste morda opazili, se da continue vedno nadomestiti z ustreznim ``if``
``else`` stavkom, a je to lahko veliko manj berljivo.


Podatkovni tipi
===============

V tem poglavju bomo predstavili podatkovne tipe, kaj so in zakaj so pomembni,
kako jih uporabljamo in kateri obstajajo. Nekatere si bomo tudi podrobneje
ogledali. Bolj obsežno (in pravilno) dokumentacijo najdete na
https://docs.python.org/3.5/library/stdtypes.html.

Uvod
----

Program za svoje delovanje potrebuje podatke, števila, besede, slike, tabele,
... Take in drugačne tipe podatkov računalnik hrani v pomnilniku, v programu pa
imamo podatke na voljo kot spremenljivke. Python ima veliko podatkovnih tipov,
na kratko smo si že pogledali števila in nize znakov. Različni tipi podpirajo
različne operacije in so primerni za različne priložnosti, zato jih je potrebno
poznati, da jih znamo pravilno izbirati.

Števila
-------

Python podpira (na grobo) dve vrsti števil -- cela števila (integer, int) in
decimalna (float, double) števila. Za cela števila ni omejitve na dolžino,
decimalna števila pa imajo standardne omejitve, a so za naše računanje dovolj
dobra. Veljavne vrednosti decimalnih števila sta tudi obe neskončnosti in
``nan``, ki pomeni "Not a number". Cela števila dobimo iz drugih tipov s
funkcijo ``int``, decimalna pa s funkcijo ``float``.

.. code::

  int(objetkt, [baza])

Pretvori ``objekt`` v celo število. Če to ni mogoče, vrže izjemo. Pri
decimalnem argumentu odreže decimalke. Če je podan
parameter ``baza``, poskuša pretvoriti ``objekt``, kot bi bil zapisan v številskem
sistemu z bazo ``baza``

.. code::

  float(objetkt)

Pretvori ``objekt`` v decimalno število. Če to ni mogoče, vrže izjemo.

.. note::

  Vse "funkcije", ki so ime nekega podatkovnega tipa, niso v resnici funkcije,
  temveč kar direktno konstruktorji teh objektov. To za uporabo ni pomembno, če
  pa vas zanima, si lahko več o tem preberete v poglavju :ref:`konstruktorji`.

Primer:

.. code-block:: python

  a = 238743234
  b = 123.5324
  c = a + b    # rezultat je decimalno število
  k = -13
  r = -123.3223e12
  z = 0xdead   # z je sedaj 57005
  inf = float('inf')

S števili lahko računamo (duh), tip rezultata je odvisen od tipov operandov. Če
je eden izmed njiju decimalno število, potem je rezultat decimalen, Rezultat
operacije dveh celih števil je celo število. Izjema je deljenje, ki vedno vrne
decimalno število. Če želimo dobiti celoštevilsko deljenje, ki zaokrožuje proti
0, uporabimo operator ``//``.

Python naravno podpira tudi kompleksna števila s pomočjo tipa ``complex`` ali
imaginarne enote ``j``, npr. ``3.4 - 2.8j``.

.. code::

  complex(arg1, [arg2])

Če je dan samo en argument, ga poskuša pretvoriti v kompleksno število. Če
sta podana oba argumenta, potem ju interpretira kot realni in imaginarni del.

Logične vrednosti
-----------------

Logična vrednost (boolean) je spremenljivka, ki ima lahko le dve stanji:
resnično ali neresnično. V Pythonu se ti dve stanji imenujeta ``True`` in
``False`` (z veliko začetnico). V resnici sta to objekta tipa ``bool``, ki ju
lahko enačimo s številoma ``0`` in ``1``.  Z logičnimi vrednostmi lahko računamo
kot v matematiki, z uporabo logičnih veznikov ``not``, ``and`` in ``or``,
pojavijo pa se tudi kot rezultat primerjalnih operacij. Uporabljajo se v ``if``
stavkih in ``while`` zankah, za preverjanje pogojev, ali pa za na primer za
shranjevanje stanja stikal ... Vsak tip lahko pretvorimo v logično vrednost z
uporabo funkcije ``bool`` in skoraj vse se pretvori v ``True``, razen "praznih"
objektov -- ``[]``, ``()``, ``0``, ``{}`` se na primer pretvorijo v ``False``.

.. code::
  bool(objekt)

Poskuša pretvoriti objekt v logično vrednost, po pravilih omenjenih zgoraj.
Funkcija ne meče izjem.

.. code-block:: python

  >>> a = True
  >>> b = False
  >>> c = 7 > 1
  >>> 1 == c
  True
  >>> (a and not b or c) and (5 == 0)
  False

Vrstni red izvajanja operacij je enak kot v matematiki, torej ``not``, ``and``,
``or``. Vendar je zaradi nedvoumnosti priporočljivo uporabiti oklepaje.

Princip zastavic je eden izmed klasičnih prijemov v programiranju, s katerim
si lahko pomagamo v zelo veliko različnih primerih. Ideja je, da neko
"zastavico" (logično spremenljivko) postavimo na eno izmed vrednosti, potem pa
jo pod določenimi pogoji spremenimo. Primer bi bilo npr.  preverjanje če je
neko število praštevilo. Na začetku privzamemo, da število je praštevilo
(``zastavica = True``). Nato gremo preverjati, če kakšno število različno od
ena slučajno deli našo število. Če ga najdemo, zastavico nastavimo na
``False``.  Ko se ta del programa izvede, nam stanje zastavice pove, ali je
število praštevilo ali ne -- če smo našli vsaj enega delitelja je zastavica
``False``, če deliteljev nismo našli pa je ``True``. Ta princip je seveda
mogoče posplošiti na več kot dve vrednosti.

None
~~~~

Vredost ``None`` je vrednost, ki predstavlja prazno vrednost. Ta vrednost je
ena sama in vedno enaka. Pri pretvorbi v ``bool`` se pretvori v ``False``.
Ko preverjamo, ali je neka spremenljivka enaka ``None`` lahko uporabimo ``is``
operator.

.. code-block:: python

  >>> a = None
  >>> a  # vrednost None se v interpreterju ne pokaže
  >>> a is None
  True
  >>> a == None
  True

Seznami
-------

Največji problem enostavnih spremenljivk je v tem, da lahko vsebujejo le en
podatek. Tako moramo npr.  če hočemo od uporabnika dobiti 10 stvari, za to
narediti tudi 10 spremenljivk. Kaj pa, če hočemo stvari dobiti 1000? Ali pa
100.000?

Tu v poštev pridejo seznami. Sezname prav tako kot spremenljivko spravimo pod
neko ime, označujejo pa jih oglati oklepaji ``[`` in ``]``. Med oglatimi
oklepaji lahko navedemo poljubno število spremenljivk, ki bodo vse vsebovane v
seznamu

.. code-block:: python

  seznam = [1, 5, "abc", 66.12]

Kot vidimo, lahko seznam vsebuje mešane tipe spremenljivk - vsebuje lahko nekaj
celih števil, nekaj decimalnih števil in nekaj nizov znakov. Sezname iz drugih
tipov dobimo s funkcijo ``list``.

.. code::

  list(objekt)

Poskuša pretvoriti objekt v seznam. Objekt mora biti iterabilen, sicer
funkcija vrže izjemo.

Dostopanje elementov seznama
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dostopanje do elementov seznama je malce drugačno kot pri navadnih
spremenljivkah. Če namreč vpišemo samo ime seznama, bomo seveda dobili vse
elemente -- v seznamu. Če pa hočemo dostopati do elementov, moramo za imenom
seznama v oglatih oklepajih napisati njegovo mesto. Pozor, računalnik ponovno
šteje od 0 naprej (torej je prvo mesto označeno z nič, drugo z 1, ...). Če
poskusimo dostopati "prepozen" element (npr. št. 12 v seznamu s štirimi
elementi) dobimo izjemo. V številko elementa pa lahko vpišemo tudi negativno
število, kjer -1 pomeni zadnji element, -2 predzadnji itd.

.. code-block:: python

  >>> seznam [1, 5, 'abc', 66.12]
  >>> seznam[0]
  1
  >>> seznam[3]
  66.12
  >>> seznam[12]
  Traceback (most recent call last):
    File "<pyshell#6>", line 1, in <module> seznam[12]
  IndexError: list index out of range
  >>> seznam[-1]
  66.12

Dodajanje in odvzemanje elementov seznama
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V seznam seveda lahko dodajamo in iz njega odvzemamo elemente. Za te (in ostale
operacije na seznamih) uporabljamo metode. Do metod dostopamo tako, da po imenu
seznama napišemo ``.``, za njo pa ime metode (seznam.metoda()). Najbolj
uporabljane metode so naslednje:

.. code::

 list.append(vrednost)

V seznam na koncu doda element z vrednostjo ``vrednost``.

.. code::

  list.insert(index, vrednost)

V seznam pred ``index``-to mesto doda element z vrednostjo ``vrednost``.

.. code::

  list.pop(index)

Iz seznama pobriše ``index``-ti element in vrne njegovo vrednost.

.. code::

  list.remove(vrednost)

Iz seznama pobriše prvi element z vrednostjo ``vrednost``.

Še primeri uporabe metod

.. code-block:: python

  >>> seznam = [1, 5, 'abc', 66.12]
  >>> seznam.append(16)
  >>> seznam
  [1, 5, 'abc', 66.12, 16]
  >>> seznam.insert(2, "Hello World!")
  >>> seznam
  [1, 5, 'Hello World!', 'abc', 66.12, 16]
  >>> seznam.pop(0)
  1
  >>> seznam
  [5, 'Hello World!', 'abc', 66.12, 16]
  >>> seznam.pop(-2)
  66.12
  >>> seznam
  [5, 'Hello World!', 'abc', 16]
  >>> seznam.remove(5)
  >>> seznam
  ['Hello World!', 'abc', 16]

Nizi znakov
-----------

Niz znakov (string) v Pythonu naredimo tako da, damo besedilo v enojne ali
dvojne narekovaje. Mogoči so tudi trojni narekovaji, ki segajo čez več vrstic.
Niz pa lahko ustvarimo tudi iz kateregakoli drugega tipa s klicanjem funkcije
``str``. Primer:

.. code-block:: python

  ime = "Janez"
  priimek = 'Novak'
  kratek_zivljenjepis = """
    Rodil: 1934
    Živel na Primorkem.
    Umrl: 2001
  """
  stevilka_ampak_ne_cisto = str(12)
  stevilka_ampak_spet_ne_cisto = '134'

.. code::

  str(objekt)

Pretvori objekt v niz znakov. Ta funkcija se tudi implicitno kliče pri
klicanju funkcije ``print``.

Niz znakov ``"abcd"`` si lahko nekako predstavljamo kot seznam ``['a', 'b',
'c', 'd']``. Primerjava v Pythonu ni čisto popolna, saj elementov niza znakov
ne moremo spreminjati, pri branju elementov pa se obnaša popolnoma enako. Tako
npr. ``niz[2]`` pomeni tretji element niza znakov (torej tretja črka oz. znak).

Torej -- nize znakov beremo na isti način kot sezname, spreminjati njihovih
elementov pa ne moremo

.. code-block:: python

  >>> niz = "Dober dan!"
  >>> niz[2]
  'b'
  >>> niz[-1]
  '!'
  >>> niz[12]
  Traceback (most recent call last):
    File "<pyshell#3>", line 1, in <module> niz[12]
  IndexError: string index out of range
  >>> niz[1] = 'c'
  Traceback (most recent call last):
    File "<pyshell#4>", line 1, in <module> niz[1] = 'c'
  TypeError: 'str' object does not support item assignment

Brisanje in dodajanje v niz znakov
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Za razliko od seznamov nizi znakov nimajo metod ``.append``, ``.pop`` in
podobno. Znamo pa nize znakov "seštevati" (znak + dva niza zlepi skupaj). Torej
lahko dodajanje znakov na konec dobimo s prištevanjem na konec, dodajanje
znakov na začetek pa s prištevanjem na začetek. Seveda s tem originalnega niza
v resnici ne spremenimo na mestu, saj moramo vrednost spet dodeliti neki (lahko
isti) spremenljivki

.. code-block:: python

  >>> niz
  'Dober dan!'
  >>> niz = niz + " Kako se imate?"
  >>> niz 'Dober dan! Kako se imate?'
  >>> niz = "Lep pozdrav in " + niz
  >>> niz
  'Lep pozdrav in Dober dan! Kako se imate?'

Spreminjanje elementov niza znakov
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ker elementov ne moremo spremeniti direktno z ukazom ``niz[x] = 'a'`` ali
podobno, jih spreminjamo tako, da naredimo nov prazen niz, nato pa potujemo po
starem nizu in prepisujemo črko po črko v nov niz. Vsakič ko srečamo znak, ki
ga nočemo, ga preprosto ne prepišemo. Če pa srečamo znak, ki bi ga radi
zamenjali, ga preprosto zamenjamo. Spodaj primer programa, ki v našem nizu vse
samoglasnike nadomesti z zvezdico.

.. code-block:: python

  niz = "Lep pozdrav in Dober dan! Kako se imate?"
  nov_niz = ""
  samoglasniki = "aeiou"
  for i in niz:
      if i in samoglasniki:
          nov_niz = nov_niz + "*"
      else:
          nov_niz = nov_niz + i
  print(nov_niz)
  >>>
  L*p p*zdr*v *n D*b*r d*n! K*k* s* *m*t*?

Zadnji dve vrstici sta kopija tega, kar se pojavi, ko program izvedemo.

Slovarji
--------

Slovarji (asociativne tabele, dictionary, associative array, map) so posplošitev
seznamov, kjer lahko namesto ``a[0]`` naredimo na primer ``a["Janez"]``.
Torej bolj formalno: kot *ključ* v slovarju lahko uporabimo katerikoli
**nespremenljiv** objekt, in pod ta ključ lahko spravimo želeno vrednost.
Slovarje lahko naredimo na veliko načinov.

.. code::

  dict(objekt)

Pretvori ``objekt`` v slovar. Objekt je lahko na primer seznam dvojic, drug
slovar...

Primer:

.. code-block:: python

  ocene = {'janez': [2, 1, 2], 'metka': [5, 3, 4]}
  r = dict(a=3, b=4, c=5)
  h = dict([[1, 23], ["asdf", 3], [3, []]])
  k = {}

Tu smo po vrsti naredili slovarje: ``ocene`` s ključema ``janez`` in ``metka``,
``r`` s ključi ``a``, ``b``, ``c``, slovar ``h`` s ključi ``1``, ``asdf``, in
``3`` in prazen slovar.

Do elementov v slovarju dostopamo tako kot v seznamu, ``ocene["metka"]`` nam
vrne vrednost ``[5, 3, 4]``. Ključi v slovarju so lahko mešanih tipov, prav
tako vrednosti. Ključi niso urejeni in morajo biti enolični. S ``for`` zanko se
lahko zapeljemo čez vse ključe v slovarju (v nekem vrstnem redu):

.. code-block:: python

  for ime in ocene:
      print(ime, "=>", ocene[ime])

  janez => [2, 1, 2]
  metka => [5, 3, 4]

Z operatorjem ``in`` lahko preverimo, ali določen ključ obstaja v slovarju --
vrne nam logično vrednost. Če želimo dostopati do elementa, ki ga ni v
slovarju, Python vrže izjemo

.. code-block:: python

  >>> ocene['lojze']
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 'lojze'

Slovarji imajo zelo veliko metod podobnih seznamom.
Nove elemente dodamo kar s klicem ``ocene["piflar"] = [5, 5, 5]``.
Dolžino jim lahko izračunamo s pomočjo funkcije ``len``.

.. code::

  dict.get(key, default)

Vrne vrednost pri ključu ``key``, če obstaja, sicer vrne ``default``. Ne
vrže izjeme.

.. code::

  dict.update(slovar)

V slovar doda nov slovar, pri čemer prepiše morebitne že obstoječe ključe z
novimi.

.. code::

  dict.pop(key, [default])

Iz seznama pobriše element pri ključu ``key`` in vrne njegovo vrednost. Če
ne obstaja potem vrže izjemo, razen če je podan tudi parameter ``default``
(ki ni obvezen). V slednjem primeru vrne ``default``.


Množice
-------
Množice (set) implementirajo matematične množice, torej zbirko z neurejenimi
**nespremenljivimi** elementi, ki se ne smejo ponavljati. Množico ustvarimo s
pomočjo zavitih oklepajev ``{`` in ``}``, podobno kot seznam ali slovar (le da
tu ne pišemo ključev), ali pa iz katere koli druge zbirke s klicem funkcije
``set``.

.. code-block:: python

  >>> imena = {'janez', 'metka', 'lojze'}
  >>> stevila = set([1, 3, 1, 3, 5])
  >>> stevila
  {3, 1, 5}
  >>> {1, 2, 3} == {3, 1, 1, 2}
  True

Množice so tako zelo uporabne za odstranjevanje duplikatov. Podpirajo vrsto
matematičnih operacij, kot so unija ``|``, presek ``&``, "je podmnožica" ``<=``,
"je nadmnožica" ``>=`` (tudi "pravi" verziji ``<`` in ``>``), simetrična razlika
``^``.

.. code::

  set(objekt)

Pretvori ``objekt`` v množico, če je to možno, sicer vrže izjemo. To pomeni,
da se lahko vrsti red elementov premeša, duplikati pa se lahko odstranijo.

Ostale uporabne metode za manipulacijo množic:

.. code::

  set.add(vrednost)

Doda vrednost ``vrednost`` v množico, če ta že obstaja, se ne zgodi nič.

.. code::

  set.remove(vrednost)

Odstrani vrednost ``vrednost`` iz množice, če ta ne obstaja, vrže izjemo
``KeyError``.

.. code::

  set.discard(vrednost)

Odstrani vrednost ``vrednost`` iz množice, če ta ne obstaja, se ne zgodi
nič.

.. code::

  set.pop()

Odstrani in vrne nek element množice. Če je prazna, vrže izjemo ``KeyError``.

Množice so očitno spremenljivi objekti, nespremenljivo verzijo, ki jo lahko
uporabimo kot ključ slovarja ali element množice implementira ``frozenset``.

Nabori
------

Nabori so nespremenljivi seznami. Ustvarimo jih z okroglimi oklepaji ``(``,
``)`` ali klicem funkcije ``tuple``. Z njimi delamo podobno kot z nizi, in jih
lahko uporabljamo za ključe v slovarjih ali za elemente množic.

.. code-block:: python

  >>> a = (1, 3, 5)
  >>> b = tuple([3, 5, "sda"])
  >>> b[0]
  3
  >>> a[1] = 9
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment

.. py:function:: tuple(objekt)

  Pretvori ``objekt`` v nabor. Vrstni red elementov se ohrani. Če pretvorba ni
  mogoča, vrže izjemo.

Dodatek o vseh zbikah
---------------------

Vse podatkovne strukture, ki lahko hranijo več elementov so si podobne, a se
razlikujejo v pomembnih razlikah, ki jih naredijo uporabne za posamezne primere.
Zelo pogosto jih lahko med sabo pretvarjamo, npr. ``list`` v ``tuple`` in
podobno.

Vendar imajo vse veliko skupnega -- pri vseh dolžino dobimo s klicem funkcije
``len``, čez vse gremo lahko s ``for`` zanko in pri vseh preverjamo vsebovanost
elementov z operatorjem ``in``. Na podlagi zgoraj opisanih lastnosti se
odločite, katera najbolj ustreza vašemu problemu. Kasneje si bomo pogledali še
bolj specifične strukture, kot na primer ``deque``, ``defaultdict`` ali
``namedtuple``.

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

Za zelo podrobno razlago scopinga v Pythonu kliknite na
http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/scope_resolution_legb_rule.ipynb

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
napišete npr. ``dir(int)``, še bolj popoln seznam pa najdete na
https://docs.python.org/3.4/reference/datamodel.html.
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

Datoteke
========

Pomemben del programiranja je tudi delo z datotekami. Praktično vsak program, ki
ga imate na računalniku uporablja datoteke tako ali drugače, ali so to slike,
ki jih uporablja za izgled, zvok, video, tekst... V tem razdelku se bomo
pogledali, kako se Python obnaša pri delu z datotekami.

Odpiranje in zapiranje datotek
------------------------------

V Pythonu datoteko (kakršna koli že je, od teksta do zipa) odpremo s funkcijo
``open``. Datoteko lahko odpremo za branje, pisanje, oboje ali dodajanje.
Funkcija open sama po sebi ne naredi ničesar, preveri samo če tam datoteka
obstaja, če ne obstaja in smo izbrali pisanje, jo naredi in s sistemom izmenja
podatke za njeno branje. Če želimo brati datoteko, ki ne obstaja, potem Python
vrže izjemo. Odpiranje samo pripravi datoteko za operacije na njej in ne naredi
še nič resnega.

.. code::
  open(pot_do_datoteke[, način])

Najde datoteko in vrne objekt za delo z njo. Kaj lahko počne je odvisno od
``načina``, ki je ``r`` za branje, ``w`` za pisanje, ``+`` za branje in
pisanje ter ``a`` za dodajanje. Kratice pomenijo *read*, *write* in *append*.
Bolj natančno dokumentacijo najdete na
https://docs.python.org/3.5/library/functions.html#open.
Na windowsih moramo za netekstovne datoteke dodati še ``b``, ki pomeni *binary*.
Če način ni podan, je enak ``r``.  Pod do datoteke je podana kot zaporedje map
ločenih s ``/``, kjer ``..`` označuje *en mapo višje*. Npr.
``../slike/solata.jpg`` pomeni: odpri datoteko ``solata.jpg``, ki se nahaja eno
mapo višje v mapi slike.

Primer uporabe:

.. code-block:: python

  >>> f = open("besedilo.txt")  # recimo, da obstaja
  >>> f
  <_io.TextIOWrapper name='besedilo.txt' mode='r' encoding='UTF-8'>
  >>> g = open("asdf", "w")     # naredi novo datoteko, če ne obstaja
  >>> g
  <_io.TextIOWrapper name='asdf' mode='w' encoding='UTF-8'>
  >>> h = open("../slike/soalta.jpg")  # jejhata, zatipkali smo se
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  FileNotFoundError: [Errno 2] No such file or directory: '../slike/soalta.jpg'

Datoteko moramo po uporabi tudi zapreti, da sistemu povemo, da smo jo
zaključili uporabljati. Na Windowsih datoteke recimo ne moramo izbrisati, če jo
kakšen program uporablja (če je odprta).

Datoteko zapremo s klicem metode ``close``.

.. code::

  file.close()

Zapre datoteko in pove sistemu, da smo jo nehali uporabljati. To tudi napiše
vse morebitne še nenapisane podatke do konca (flusha datoteko).

.. code-block:: python

  >>> f.close()
  >>> g.close()
  >>> h.close()
  >>> f.read()   # ko je datoteka zaprta z njo ne moremo več delati
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: I/O operation on closed file.

Ko delamo z datotekami pazimo, da je vrsti red vedno enak: odpremo, delamo,
zapremo.

Branje datotek
--------------

Privzemimo, da smo datoteko odprli za branje. Za branje imamo na voljo veliko
načinov.

.. code::

  file.read([n])

Prebere celo datoteko kot niz, skupaj z vsemi posebnimi znaki (recimo
``\n``). Če je ``n`` podan, prebere samo prvih ``n`` bajtov.

.. code::

  file.readline()

Prebere naslednjo vrstico in jo vrne (vključno z ``\n``).

.. code::

  file.realines()

Prebere vse vrstice in jih vrne kot seznam (vključno z ``\n``)

Lahko beremo tudi s ``for`` zanko. Pri branju si datoteka zapomni, do kam smo jo
prebrali in naslednjič, ko kličemo kakšno funkcijo za branje nadaljuje, kjer
smo na zadnje ostali. To pomeni, da datoteko ponavadi preberemo le enkrat (dva
zaporedna klica ``.read()`` bosta povzročila da drugi vrne prazen niz, saj je
bilo vse že prebrano). Enako se obnašajo tudi druge metode za branje, če ni
ničesar več za prebrati, potem vrnejo prazen niz. Vsebino datoteke si moramo, če
jo želimo uporabljati celo, shraniti v spremenljivko.

.. warning::

  Pri uporabi ``.read()`` mentode je potrebno paziti na velikost datoteke, ne
  poskušajte prebrati celega filma, saj verjetno nimate 4GB prostega spomina, pa
  tudi če, bo to verjetno delovalo zelo počasi.

Primer:

.. code-block:: python

  >>> f = open("besedilo.txt")
  >>> f.readline()
  'Romeo: O, Julija!\n'
  >>> for line in f:
  ...     print(line)
  Julija: O, Romeo, zakaj si Romeo?

  Romeo: Ženska, to ni mel smisla.

  THE END

Vsebina datoteke ``besedilo.txt`` je seveda::

  Romeo: O Julija!
  Julija: O, Romeo, zakaj si Romeo?
  Romeo: Ženska, to ni mel smisla.
  THE END

Če se želimo znebiti nadležnih ``\n`` na koncu prebrane vrstice, uporabimo
metodo ``strip`` na stringih.

.. code::

  str.strip([znaki])

Poreže vse znake, ki se nahajajo v nizu ``znaki`` z začetka in konca
niza. Če ``znaki`` niso podani, potem poreče ves whitespace (presledke,
tabulatorje, ``\n`` in ostalo)

Obstajata tudi metodi ``lstrip`` in ``rstrip``, ki delujeta samo na levi
in desni strani niza.


Pisanje v datoteke
------------------

V datoteko, ki je odprta za pisanje, lahko pišemo. Duh. Če je ta datoteka že
obstajala, se njena prejšnja vsebina prepiše, kar je bilo prej noter je
izgubljeno. Če datoteka še ni obstajala, potem se ustvari nova datoteka.

Pišemo lahko na dva načina, z uporabo metode ``write`` ali ``writelines``.

.. code::

  file.write(niz)

Napiše niz v datoteko. Ne doda nobenih posebnih znakov.

.. code::

  file.writelines(seznam_nizov)

Napiše seznam nizov v datoteko, niz po niz. Ne doda nobenih vmesnih znakov.

Primer:

.. code-block:: python

  f = open("stevila.txt", "w")
  f.write(str(0))
  f.write(str(1))
  f.writelines(["to", "so", "stevila"])
  f.write("\nAja, treba je dodajati nove vrstice!")
  f.close()

Vsebina datoteke je sedaj::

  01tosostevila
  Aja, treba je dodajati nove vrstice!


Stavek ``with``
---------------

Kot smo videli je postopek za delo z datotekami vedno enak, odpri, delaj,
zapri. Python ta postopek malo poenostavi, z uporabo ``with`` stavka.

Namesto::

  f = open("asdf")
  # beremo in pišemo
  f.close()

lahko uporabljamo::

  with f as open("asdf"):
      # beremo in pišemo

Datoteka uporabljena v ``with`` stavku se avtomatsko zapre, ne glede na to, kaj
se dogaja v telesu stavka. To je bolje kot lahko trdimo za prvi primer, če se
tam nekje na sredi zgodi izjema, bo program prekinjen, datoteka pa bo ostala
nesrečno odprta. Zaradi tega je ``with`` stavek najboljši način za delo z
datotekami.


Dodatek: ``stdin`` in ``stdout`` kot datoteki
---------------------------------------------

Tudi standardni vhod in izhod se obnašata kot datoteki, vhod je odprt za
branje, izhod pa za pisanje. Če želimo bolj natančno kontrolo nad branjem in
pisanjem lahko namesto ``input`` in ``print`` uporabimo "datoteki"
``sys.stdin`` in ``sys.stdout``. Teh dveh "datotek" ni treba odpirati ali
zapirati, podpirata pa običajne metode za branje in pisanje. Če želite to
uporabljati, ne pozabite na začetku programa dodati ``import sys``, da boste
imeli dostop do teh dveh objektov.

Naključna števila
=================

Psevdonaključna števila dobimo z uporabo modula ``random``.
Če želimo uporabljat te funkcije moramo na začetku datoteke dodati stavek

.. code::

  import random

Lahko dobimo naključna cela števila, naključno decimalno število iz znanih
zveznih porazdelitev, naključno izbiro iz seznama ...

.. code::

  random.randint(a, b)

Vrne naključno celo število na intervalu ``[a, b]``.

.. code::

  random.gauss(mu, sigma)

Vrne naključno število iz Gaussove porazdelitve.

.. code::

  random.choice(seznam)

Vrne naključni element seznama.

.. vim: spell spelllang=sl
Jure Slak
