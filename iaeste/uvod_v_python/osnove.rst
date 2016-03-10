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
  :linenos:

  # -*- coding: utf-8 -*-

  x = 2
  y = 5
  ime = "Andreja"
  leta = x + y

.. HINT::

  Znak = v programiranju nima istega pomena kot v matematiki. = pravzaprav
  pomeni "vrednost na desni zapiši v spremenljivko na levi". Torej bo ukaz x =
  x + 2 dejansko pomenil "x povečaj za 2".

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
  :linenos:

  # -*- coding: utf-8 -*-

  """
  Dobiti želimo absolutno vrednost spremenljivke x.

  To naredimo tako da ...
  """

  ime = "Janez"  # ime naj bo brez presledkov in se začne z veliko začetnico
  # v absx shranimo absolutno vrednost x
  x = -8
  if x < 0:
      absx = -x
  else:
      absx = x

Input in output
---------------

Input in output pomeni branje uporabnikovega vpisa in izpisovanje na zaslon.
Uporabili smo funkcije ``input``, ``int``, ``print``, ``format``.

.. py:function:: input(niz_znakov)

  Izpiše ``niz_znakov`` in vrne niz znakov, ki ga je vtipkal uporabnik.

.. py:function:: print(objekt)

  Izpiše niz objekt ``objekt``. Objekt je lahko število, niz znakov, ...

.. py:class:: str

  .. py:method:: format(niz, p1, p2, p3, ...)

    Na mesto ki je v ``niz``-u označeno z '{0}' vstavi ``p1``, na '{1}' vstavi
    ``p2``, ...

Ogledate si lahko tudi, kaj počne funkcija :py:func:`int`.

Primer uporabe funkcije ``input`` in ``print``:

.. literalinclude:: /tutorialsPythonBasic/verybasic/input/input3.py
  :linenos:

Primer uporabe metode ``format``:

.. code-block:: python
  :linenos:

  # -*- coding: utf-8 -*-

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
  :linenos:

  if pogoj:
      # Se izvede če je izpolnjen pogoj
  elif pogoj2:
      # Se izvede če je izpolnjen pogoj2 (in ni izpolnjen pogoj)
  elif pogoj3:
      # Se izvede če je izpolnjen pogoj3 (in nista izpolnjena prejšnja pogoja)
  else:
      # Se izvede če ni izpolnjen noben od zgornjih pogojev

.. ATTENTION::

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
  :linenos:

  # -*- coding: utf-8 -*-

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
  :linenos:

  while pogoj:
      # Se izvaja dokler je pogoj izpolnjen

``while`` zanko uporabimo takrat, ko se mora nekaj izvajati dokler je pogoj
izpolnjen. Pri ``while`` zanki moramo biti zelo pozorni na neskončne zanke.
Neskončna zanka se zgodi takrat, ko je pogoj vedno izpolnjen, program pa bo
tekel v neskončnost. Če se nam to slučajno zgodi, pritisnemo kombinacijo tipk
``ctrl+c``, s čimer program prekinemo.

.. code-block:: python
  :linenos:

  # -*- coding: utf-8 -*-

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
  :linenos:

  # -*- coding: utf-8 -*-

  """
  Želeli smo spremenljivko x iz 0 manjšati dokler ni enaka -100 in takrat zanko
  prekiniti, a smo se zmotili in namesto - napisali +. Seveda smo dobili
  neskončno zanko, ki x povečuje (in izpisuje) v neskončnost.
  """

  x = 0
  while x != -100:
      print(x)
      x = x + 1

.. HINT::

  Če se kdaj zataknete v neskončno zanko, pritisnite ``CTRL + c``, ki prekine
  trenutno izvajani program.

For zanka
~~~~~~~~~

.. code-block:: python
  :linenos:

  for spremenljivka in zbirka:
      # Se izvaja dokler spremenljivka ne preteče vseh elementov zbirke.

``for`` zanko uporabimo takrat, ko želimo, da naša spremenljivka preteče vse
elemente neke zbirke. Zbirka je lahko seznam, niz znakov, slovar, iterator ali
kaj podobnega, bolj podrobno si bomo to pogledali pozneje. Zaenkrat bomo for
zanko večinoma uporabljali skupaj s funkcijo ``range(x)``, ki vrne vse elemente
od ``0`` do ``x-1`` (torej ``range(5)`` vrne ``[0, 1, 2, 3, 4]``).

Preprost primer:

.. code-block:: python
  :linenos:

  # -*- coding: utf-8 -*-

  """
  Program izpiše števila od 0 do 49.
  """

  for i in range(50):
      print(i)

Bolj kompliciran primer:

.. literalinclude:: /tutorialsPythonBasic/verybasic/loops/for.py
  :linenos:

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
  :linenos:

  # -*- coding: utf-8 -*-

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
  :linenos:

  # -*- coding: utf-8 -*-

  a = "sajkdfs adfjkhasdf jkasdkfjas dfkjhasd fasdlfkjsa dflkjsadf"
  veljavno = "aeiou"
  for i in a:
      if a not in veljavno:
          continue
      # tukaj zelo veliko kode, ki procesira veljavne podatke

Kot ste morda opazili, se da continue vedno nadomestiti z ustreznim ``if``
``else`` stavkom, a je to lahko veliko manj berljivo.

.. vim: spell spelllang=sl
