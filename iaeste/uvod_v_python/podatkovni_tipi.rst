Podatkovni tipi
===============

V tem poglavju bomo predstavili podatkovne tipe, kaj so in zakaj so pomembni,
kako jih uporabljamo in kateri obstajajo. Nekatere si bomo tudi podrobneje
ogledali. Bolj obsežno (in pravilno) dokumentacijo najdete `tukaj
<https://docs.python.org/3.4/library/stdtypes.html>`_.

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

.. py:function:: int(objetkt, [baza])

  Pretvori ``objekt`` v celo število. Če to ni mogoče, vrže izjemo. Pri
  decimalnem argumentu odreže decimalke. Če je podan
  parameter ``baza``, poskuša pretvoriti ``objekt``, kot bi bil zapisan v številskem
  sistemu z bazo ``baza``

.. py:function:: float(objetkt)

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

.. py:function:: complex(arg1, [arg2])

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

.. py:function:: bool(objekt)

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

.. HINT::

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

.. py:function:: list(objekt)

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

.. py:class:: list

  .. py:method:: append(vrednost)

    V seznam na koncu doda element z vrednostjo ``vrednost``.

  .. py:method:: insert(index, vrednost)

    V seznam pred ``index``-to mesto doda element z vrednostjo ``vrednost``.

  .. py:method:: pop(index)

    Iz seznama pobriše ``index``-ti element in vrne njegovo vrednost.

  .. py:method:: remove(vrednost)

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

.. py:function:: str(objekt)

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

.. py:function:: dict(objekt)

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

.. py:class:: dict

  .. py:method:: get(key, default)

    Vrne vrednost pri ključu ``key``, če obstaja, sicer vrne ``default``. Ne
    vrže izjeme.

  .. py:method:: update(slovar)

    V slovar doda nov slovar, pri čemer prepiše morebitne že obstoječe ključe z
    novimi.

  .. py:method:: pop(key, [default])

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

.. py:function:: set(objekt)

  Pretvori ``objekt`` v množico, če je to možno, sicer vrže izjemo. To pomeni,
  da se lahko vrsti red elementov premeša, duplikati pa se lahko odstranijo.

Ostale uporabne metode za manipulacijo množic:

.. py:class:: set

  .. py:method:: add(vrednost)

    Doda vrednost ``vrednost`` v množico, če ta že obstaja, se ne zgodi nič.

  .. py:method:: remove(vrednost)

    Odstrani vrednost ``vrednost`` iz množice, če ta ne obstaja, vrže izjemo
    ``KeyError``.

  .. py:method:: discard(vrednost)

    Odstrani vrednost ``vrednost`` iz množice, če ta ne obstaja, se ne zgodi
    nič.

  .. py:method:: pop()

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

.. vim: spell spelllang=sl
